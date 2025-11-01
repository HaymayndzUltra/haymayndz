#!/usr/bin/env python3
"""
Circuit breaker pattern implementation for external calls and artifact loading.
Prevents cascading failures by opening circuit after threshold failures.
"""
import time
from enum import Enum
from typing import Dict, Optional, Callable, Any
from datetime import datetime, timedelta


class CircuitState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"  # Normal operation
    OPEN = "open"  # Circuit open, failing fast
    HALF_OPEN = "half_open"  # Testing if service recovered


class CircuitBreaker:
    """Circuit breaker for protecting external calls."""
    
    def __init__(
        self,
        failure_threshold: int = 5,
        timeout: int = 60,
        half_open_timeout: int = 30,
        name: str = "default"
    ):
        """
        Initialize circuit breaker.
        
        Args:
            failure_threshold: Number of failures before opening circuit
            timeout: Seconds to keep circuit open
            half_open_timeout: Seconds to wait in half-open state
            name: Circuit breaker name for logging
        """
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.half_open_timeout = half_open_timeout
        self.name = name
        
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: Optional[datetime] = None
        self.opened_at: Optional[datetime] = None
        self.half_opened_at: Optional[datetime] = None
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function through circuit breaker.
        
        Args:
            func: Function to execute
            *args: Positional arguments
            **kwargs: Keyword arguments
            
        Returns:
            Function result
            
        Raises:
            Exception: If circuit is open or function fails
        """
        # Check circuit state
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                self.half_opened_at = datetime.now()
            else:
                raise Exception(
                    f"Circuit breaker '{self.name}' is OPEN. "
                    f"Too many failures detected."
                )
        
        # Execute function
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise
    
    def _should_attempt_reset(self) -> bool:
        """Check if circuit should attempt reset."""
        if self.state != CircuitState.OPEN:
            return False
        
        if self.opened_at is None:
            return False
        
        elapsed = (datetime.now() - self.opened_at).total_seconds()
        return elapsed >= self.timeout
    
    def _on_success(self):
        """Handle successful call."""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            # If we get success in half-open, close circuit
            if self.success_count >= 1:
                self._reset()
        elif self.state == CircuitState.CLOSED:
            # Reset failure count on success
            self.failure_count = 0
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.state == CircuitState.HALF_OPEN:
            # Failure in half-open, open circuit again
            self.state = CircuitState.OPEN
            self.opened_at = datetime.now()
            self.success_count = 0
        elif self.state == CircuitState.CLOSED:
            # Check if threshold reached
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
                self.opened_at = datetime.now()
    
    def _reset(self):
        """Reset circuit to closed state."""
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        self.opened_at = None
        self.half_opened_at = None
    
    def get_state(self) -> Dict:
        """Get current circuit state."""
        return {
            "state": self.state.value,
            "failure_count": self.failure_count,
            "success_count": self.success_count,
            "last_failure_time": (
                self.last_failure_time.isoformat()
                if self.last_failure_time else None
            ),
            "opened_at": (
                self.opened_at.isoformat()
                if self.opened_at else None
            )
        }


class CircuitBreakerManager:
    """Manages multiple circuit breakers."""
    
    def __init__(self):
        """Initialize circuit breaker manager."""
        self.circuits: Dict[str, CircuitBreaker] = {}
    
    def get_circuit(self, name: str, **kwargs) -> CircuitBreaker:
        """
        Get or create circuit breaker.
        
        Args:
            name: Circuit breaker name
            **kwargs: Circuit breaker configuration
            
        Returns:
            CircuitBreaker instance
        """
        if name not in self.circuits:
            self.circuits[name] = CircuitBreaker(name=name, **kwargs)
        
        return self.circuits[name]
    
    def call_with_circuit(
        self,
        circuit_name: str,
        func: Callable,
        *args,
        **kwargs
    ) -> Any:
        """
        Execute function through named circuit breaker.
        
        Args:
            circuit_name: Name of circuit breaker
            func: Function to execute
            *args: Positional arguments
            **kwargs: Keyword arguments
            
        Returns:
            Function result
        """
        circuit = self.get_circuit(circuit_name)
        return circuit.call(func, *args, **kwargs)


# Global manager instance
_manager = CircuitBreakerManager()


def get_circuit_breaker(name: str, **kwargs) -> CircuitBreaker:
    """Get circuit breaker instance."""
    return _manager.get_circuit(name, **kwargs)


def call_with_circuit(circuit_name: str, func: Callable, *args, **kwargs) -> Any:
    """Execute function through circuit breaker."""
    return _manager.call_with_circuit(circuit_name, func, *args, **kwargs)


if __name__ == "__main__":
    # Test circuit breaker
    breaker = CircuitBreaker(failure_threshold=3, timeout=5)
    
    def failing_func():
        raise Exception("Test failure")
    
    # Simulate failures
    for i in range(5):
        try:
            breaker.call(failing_func)
        except Exception as e:
            print(f"Attempt {i+1}: {e}")
            print(f"State: {breaker.get_state()}")
            time.sleep(0.5)

