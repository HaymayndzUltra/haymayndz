#!/usr/bin/env python3
"""
Telemetry and metrics collection system.
Tracks performance metrics, error rates, and usage statistics.
"""
import json
import time
from pathlib import Path
from typing import Dict, Optional, Any
from datetime import datetime
from collections import defaultdict


class Telemetry:
    """Telemetry and metrics collection."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize telemetry system.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.metrics_file = base_dir / ".cursor" / "logs" / "metrics.json"
        self.metrics_file.parent.mkdir(parents=True, exist_ok=True)
        
        # In-memory metrics buffer
        self.metrics_buffer: Dict[str, list] = defaultdict(list)
    
    def record_metric(
        self,
        metric_name: str,
        value: float,
        tags: Optional[Dict[str, str]] = None,
        timestamp: Optional[datetime] = None
    ):
        """
        Record a metric value.
        
        Args:
            metric_name: Name of the metric
            value: Metric value
            tags: Optional tags for filtering
            timestamp: Optional timestamp (defaults to now)
        """
        if timestamp is None:
            timestamp = datetime.now()
        
        metric_entry = {
            "name": metric_name,
            "value": value,
            "timestamp": timestamp.isoformat(),
            "tags": tags or {}
        }
        
        self.metrics_buffer[metric_name].append(metric_entry)
    
    def record_timing(
        self,
        operation: str,
        duration_ms: float,
        tags: Optional[Dict[str, str]] = None
    ):
        """
        Record timing metric.
        
        Args:
            operation: Operation name
            duration_ms: Duration in milliseconds
            tags: Optional tags
        """
        self.record_metric(f"{operation}_duration_ms", duration_ms, tags)
        self.record_metric(f"{operation}_count", 1, tags)
    
    def record_error(
        self,
        error_type: str,
        error_message: str,
        tags: Optional[Dict[str, str]] = None
    ):
        """
        Record error occurrence.
        
        Args:
            error_type: Type of error
            error_message: Error message
            tags: Optional tags
        """
        tags = tags or {}
        tags["error_type"] = error_type
        
        self.record_metric("error_count", 1, tags)
        
        error_entry = {
            "error_type": error_type,
            "error_message": error_message,
            "timestamp": datetime.now().isoformat(),
            "tags": tags
        }
        
        if "errors" not in self.metrics_buffer:
            self.metrics_buffer["errors"] = []
        
        self.metrics_buffer["errors"].append(error_entry)
    
    def record_cache_hit(self, cache_type: str, hit: bool):
        """
        Record cache hit/miss.
        
        Args:
            cache_type: Type of cache
            hit: Whether it was a hit
        """
        tags = {"cache_type": cache_type}
        self.record_metric(
            "cache_hit" if hit else "cache_miss",
            1,
            tags
        )
    
    def record_validation_score(self, score: float, component: str):
        """
        Record validation score.
        
        Args:
            score: Validation score (0-100)
            component: Component name
        """
        self.record_metric(
            "validation_score",
            score,
            {"component": component}
        )
    
    def flush(self):
        """Flush metrics buffer to file."""
        if not self.metrics_buffer:
            return
        
        # Load existing metrics
        if self.metrics_file.exists():
            try:
                with open(self.metrics_file, 'r', encoding='utf-8') as f:
                    existing = json.load(f)
            except:
                existing = {}
        else:
            existing = {}
        
        # Merge metrics
        for metric_name, entries in self.metrics_buffer.items():
            if metric_name not in existing:
                existing[metric_name] = []
            existing[metric_name].extend(entries)
            
            # Keep only last 1000 entries per metric
            existing[metric_name] = existing[metric_name][-1000:]
        
        # Write back
        with open(self.metrics_file, 'w', encoding='utf-8') as f:
            json.dump(existing, f, indent=2)
        
        # Clear buffer
        self.metrics_buffer.clear()
    
    def get_metrics_summary(self, last_n_minutes: int = 60) -> Dict:
        """
        Get metrics summary for last N minutes.
        
        Args:
            last_n_minutes: Number of minutes to look back
            
        Returns:
            Dictionary with metric summaries
        """
        if not self.metrics_file.exists():
            return {}
        
        cutoff = datetime.now().timestamp() - (last_n_minutes * 60)
        
        try:
            with open(self.metrics_file, 'r', encoding='utf-8') as f:
                all_metrics = json.load(f)
        except:
            return {}
        
        summary = {}
        
        for metric_name, entries in all_metrics.items():
            if metric_name == "errors":
                continue
            
            # Filter by time
            recent = [
                e for e in entries
                if datetime.fromisoformat(e["timestamp"]).timestamp() > cutoff
            ]
            
            if not recent:
                continue
            
            values = [e["value"] for e in recent]
            
            summary[metric_name] = {
                "count": len(recent),
                "sum": sum(values),
                "avg": sum(values) / len(values) if values else 0,
                "min": min(values) if values else 0,
                "max": max(values) if values else 0
            }
        
        return summary


# Global telemetry instance
_telemetry = Telemetry()


def get_telemetry() -> Telemetry:
    """Get global telemetry instance."""
    return _telemetry


if __name__ == "__main__":
    # Test telemetry
    telemetry = Telemetry()
    
    # Record some metrics
    telemetry.record_timing("cache_refresh", 45.2)
    telemetry.record_timing("response_validation", 12.5)
    telemetry.record_cache_hit("artifact_cache", True)
    telemetry.record_cache_hit("artifact_cache", False)
    telemetry.record_validation_score(85.5, "response")
    telemetry.record_error("TimeoutError", "Cache refresh timeout")
    
    # Flush
    telemetry.flush()
    
    # Get summary
    summary = telemetry.get_metrics_summary()
    print(json.dumps(summary, indent=2))

