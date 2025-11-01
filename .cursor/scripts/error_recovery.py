#!/usr/bin/env python3
"""
Error recovery orchestration system.
Handles error classification, retry strategies, and fallback mechanisms.
"""
import json
import time
import logging
from pathlib import Path
from typing import Dict, Optional, Callable, Any
from enum import Enum
from datetime import datetime


class ErrorType(Enum):
    """Error classification types."""
    TRANSIENT = "transient"  # Temporary, can retry
    PERMANENT = "permanent"  # Cannot recover, need fallback
    NETWORK = "network"  # Network-related issues
    FILE_SYSTEM = "file_system"  # File operations
    PERMISSION = "permission"  # Permission denied
    VALIDATION = "validation"  # Data validation errors
    UNKNOWN = "unknown"  # Unknown error type


class ErrorRecovery:
    """Error recovery orchestration system."""
    
    def __init__(self, config_file: Optional[Path] = None, base_dir: Optional[Path] = None):
        """
        Initialize error recovery system.
        
        Args:
            config_file: Path to error configuration file
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        
        if config_file is None:
            config_file = base_dir / ".cursor" / "config" / "error_config.json"
        
        self.config_file = config_file
        self.config = self.load_config()
        
        # Setup logging
        log_dir = base_dir / ".cursor" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / "error_log.json"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def load_config(self) -> Dict:
        """Load error configuration."""
        if not self.config_file.exists():
            return self._default_config()
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return self._default_config()
    
    def _default_config(self) -> Dict:
        """Return default configuration."""
        return {
            "retry": {
                "max_attempts": 3,
                "initial_delay": 1.0,
                "max_delay": 10.0,
                "exponential_base": 2.0
            },
            "circuit_breaker": {
                "failure_threshold": 5,
                "timeout": 60,
                "half_open_timeout": 30
            },
            "fallback": {
                "enabled": True,
                "timeout_ms": 100
            },
            "error_classification": {
                "transient_patterns": [
                    "timeout", "connection", "network", "temporary",
                    "retry", "busy", "unavailable"
                ],
                "permanent_patterns": [
                    "not found", "permission denied", "invalid",
                    "forbidden", "unauthorized"
                ]
            }
        }
    
    def classify_error(self, error: Exception) -> ErrorType:
        """
        Classify error type.
        
        Args:
            error: Exception to classify
            
        Returns:
            ErrorType enum value
        """
        error_str = str(error).lower()
        error_type = type(error).__name__.lower()
        
        config = self.config.get("error_classification", {})
        transient_patterns = config.get("transient_patterns", [])
        permanent_patterns = config.get("permanent_patterns", [])
        
        # Check for transient patterns
        for pattern in transient_patterns:
            if pattern in error_str or pattern in error_type:
                return ErrorType.TRANSIENT
        
        # Check for permanent patterns
        for pattern in permanent_patterns:
            if pattern in error_str or pattern in error_type:
                return ErrorType.PERMANENT
        
        # Check specific error types
        if "timeout" in error_str or "network" in error_str:
            return ErrorType.NETWORK
        elif "file" in error_str or "directory" in error_str:
            return ErrorType.FILE_SYSTEM
        elif "permission" in error_str or "access" in error_str:
            return ErrorType.PERMISSION
        
        return ErrorType.UNKNOWN
    
    def retry_with_backoff(
        self,
        func: Callable,
        *args,
        max_attempts: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Execute function with exponential backoff retry.
        
        Args:
            func: Function to execute
            *args: Positional arguments for function
            max_attempts: Maximum retry attempts (uses config if None)
            **kwargs: Keyword arguments for function
            
        Returns:
            Function result
            
        Raises:
            Exception: If all retries fail
        """
        retry_config = self.config.get("retry", {})
        max_attempts = max_attempts or retry_config.get("max_attempts", 3)
        initial_delay = retry_config.get("initial_delay", 1.0)
        max_delay = retry_config.get("max_delay", 10.0)
        exponential_base = retry_config.get("exponential_base", 2.0)
        
        last_error = None
        
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_error = e
                error_type = self.classify_error(e)
                
                # Don't retry permanent errors
                if error_type == ErrorType.PERMANENT:
                    self.logger.error(f"Permanent error, not retrying: {e}")
                    raise
                
                # Calculate delay
                if attempt < max_attempts - 1:
                    delay = min(initial_delay * (exponential_base ** attempt), max_delay)
                    self.logger.warning(
                        f"Attempt {attempt + 1}/{max_attempts} failed: {e}. "
                        f"Retrying in {delay:.2f}s..."
                    )
                    time.sleep(delay)
                else:
                    self.logger.error(f"All {max_attempts} attempts failed")
        
        raise last_error
    
    def execute_with_fallback(
        self,
        primary_func: Callable,
        fallback_func: Callable,
        *args,
        timeout_ms: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Execute function with fallback if primary fails.
        
        Args:
            primary_func: Primary function to execute
            fallback_func: Fallback function if primary fails
            *args: Positional arguments for functions
            timeout_ms: Timeout in milliseconds (uses config if None)
            **kwargs: Keyword arguments for functions
            
        Returns:
            Function result (from primary or fallback)
        """
        fallback_config = self.config.get("fallback", {})
        if not fallback_config.get("enabled", True):
            return primary_func(*args, **kwargs)
        
        timeout_ms = timeout_ms or fallback_config.get("timeout_ms", 100)
        start_time = time.time()
        
        try:
            result = primary_func(*args, **kwargs)
            elapsed_ms = (time.time() - start_time) * 1000
            
            if elapsed_ms > timeout_ms:
                self.logger.warning(
                    f"Primary function took {elapsed_ms:.2f}ms (threshold: {timeout_ms}ms)"
                )
            
            return result
            
        except Exception as e:
            error_type = self.classify_error(e)
            self.logger.warning(
                f"Primary function failed ({error_type.value}): {e}. "
                f"Using fallback..."
            )
            
            try:
                return fallback_func(*args, **kwargs)
            except Exception as fallback_error:
                self.logger.error(f"Fallback also failed: {fallback_error}")
                raise
    
    def log_error(
        self,
        error: Exception,
        context: Optional[Dict] = None,
        severity: str = "error"
    ):
        """
        Log error with context.
        
        Args:
            error: Exception to log
            context: Additional context dictionary
            severity: Log severity level
        """
        error_data = {
            "timestamp": datetime.now().isoformat(),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "error_classification": self.classify_error(error).value,
            "context": context or {}
        }
        
        log_file = self.base_dir / ".cursor" / "logs" / "error_log.json"
        
        # Append to error log
        if log_file.exists():
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    errors = json.load(f)
            except:
                errors = []
        else:
            errors = []
        
        errors.append(error_data)
        
        # Keep only last 1000 errors
        errors = errors[-1000:]
        
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(errors, f, indent=2)
        
        # Also log via logger
        log_method = getattr(self.logger, severity.lower(), self.logger.error)
        log_method(f"{error}: {context}")


def main():
    """Main entry point for testing."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Error recovery system")
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run test scenarios"
    )
    
    args = parser.parse_args()
    
    if args.test:
        recovery = ErrorRecovery()
        
        # Test retry
        def failing_func():
            raise ConnectionError("Connection timeout")
        
        try:
            recovery.retry_with_backoff(failing_func, max_attempts=2)
        except Exception as e:
            print(f"Expected failure: {e}")
        
        # Test fallback
        def primary():
            raise FileNotFoundError("File not found")
        
        def fallback():
            return "fallback_result"
        
        result = recovery.execute_with_fallback(primary, fallback)
        print(f"Fallback result: {result}")
    
    return 0


if __name__ == "__main__":
    main()

