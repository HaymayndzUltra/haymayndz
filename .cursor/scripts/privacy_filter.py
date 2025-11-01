#!/usr/bin/env python3
"""
Privacy filtering for data storage and logging.
Applies privacy rules before storing sensitive data.
"""
import json
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime, timedelta
from anonymize_data import PrivacyFilter, DataAnonymizer


class PrivacyManager:
    """Privacy management and compliance."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize privacy manager.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.config_file = base_dir / ".cursor" / "config" / "privacy_config.json"
        self.config = self.load_config()
        self.filter = PrivacyFilter(base_dir=base_dir)
        self.anonymizer = DataAnonymizer()
    
    def load_config(self) -> Dict:
        """Load privacy configuration."""
        if not self.config_file.exists():
            return self._default_config()
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return self._default_config()
    
    def _default_config(self) -> Dict:
        """Return default privacy configuration."""
        return {
            "pii_detection": {
                "enabled": True,
                "mask_all": False
            },
            "data_retention": {
                "logs_days": 30,
                "cache_days": 90,
                "metrics_days": 365
            },
            "secure_deletion": {
                "enabled": True,
                "overwrite_count": 3
            },
            "compliance": {
                "gdpr": True,
                "ccpa": True
            }
        }
    
    def check_pii(self, text: str) -> bool:
        """
        Check if text contains PII.
        
        Args:
            text: Text to check
            
        Returns:
            True if PII detected
        """
        if not self.config.get("pii_detection", {}).get("enabled", True):
            return False
        
        pii = self.anonymizer.detect_pii(text)
        
        # Check if any PII types found
        for pii_type, values in pii.items():
            if pii_type != "potential_names" and values:
                return True
        
        return False
    
    def filter_for_storage(self, data: Dict) -> Dict:
        """
        Filter data before storage.
        
        Args:
            data: Data dictionary
            
        Returns:
            Filtered data dictionary
        """
        filtered = self.filter.filter_log_entry(data)
        return filtered
    
    def enforce_retention(self):
        """Enforce data retention policies."""
        retention = self.config.get("data_retention", {})
        logs_dir = self.base_dir / ".cursor" / "logs"
        cache_dir = self.base_dir / ".cursor" / "cache"
        
        cutoff = datetime.now() - timedelta(days=retention.get("logs_days", 30))
        
        # Clean old log files
        if logs_dir.exists():
            for log_file in logs_dir.glob("*.log"):
                if datetime.fromtimestamp(log_file.stat().st_mtime) < cutoff:
                    log_file.unlink()
        
        # Clean old cache files
        cache_cutoff = datetime.now() - timedelta(days=retention.get("cache_days", 90))
        if cache_dir.exists():
            for cache_file in cache_dir.glob("*.json.backup"):
                if datetime.fromtimestamp(cache_file.stat().st_mtime) < cache_cutoff:
                    cache_file.unlink()
    
    def secure_delete(self, file_path: Path):
        """
        Securely delete file (overwrite before deletion).
        
        Args:
            file_path: Path to file to delete
        """
        if not self.config.get("secure_deletion", {}).get("enabled", True):
            file_path.unlink()
            return
        
        overwrite_count = self.config.get("secure_deletion", {}).get("overwrite_count", 3)
        
        if file_path.exists():
            # Overwrite file multiple times
            file_size = file_path.stat().st_size
            with open(file_path, 'ba+', buffering=0) as f:
                for _ in range(overwrite_count):
                    f.seek(0)
                    f.write(b'\x00' * file_size)
                    f.flush()
            
            # Delete file
            file_path.unlink()


if __name__ == "__main__":
    privacy = PrivacyManager()
    
    # Test PII detection
    test_text = "Contact john@example.com or call 555-1234"
    has_pii = privacy.check_pii(test_text)
    print(f"PII detected: {has_pii}")
    
    # Test filtering
    log_entry = {
        "message": "User john@example.com called",
        "timestamp": datetime.now().isoformat()
    }
    filtered = privacy.filter_for_storage(log_entry)
    print(f"Filtered: {filtered}")

