#!/usr/bin/env python3
"""
Metrics aggregation and reporting system.
Aggregates metrics from telemetry and generates reports.
"""
import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from telemetry import Telemetry


class MetricsAggregator:
    """Aggregates and reports metrics."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize metrics aggregator.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.telemetry = Telemetry(base_dir=base_dir)
        self.reports_dir = base_dir / ".cursor" / "reports"
        self.reports_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_daily_report(self) -> Dict:
        """
        Generate daily metrics report.
        
        Returns:
            Dictionary with daily report data
        """
        metrics = self.telemetry.get_metrics_summary(last_n_minutes=24 * 60)
        
        report = {
            "date": datetime.now().date().isoformat(),
            "period": "daily",
            "metrics": metrics,
            "summary": self._generate_summary(metrics)
        }
        
        # Save report
        report_file = self.reports_dir / f"daily_report_{datetime.now().date().isoformat()}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        return report
    
    def generate_hourly_report(self) -> Dict:
        """
        Generate hourly metrics report.
        
        Returns:
            Dictionary with hourly report data
        """
        metrics = self.telemetry.get_metrics_summary(last_n_minutes=60)
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "period": "hourly",
            "metrics": metrics,
            "summary": self._generate_summary(metrics)
        }
        
        return report
    
    def _generate_summary(self, metrics: Dict) -> Dict:
        """
        Generate summary from metrics.
        
        Args:
            metrics: Metrics dictionary
            
        Returns:
            Summary dictionary
        """
        summary = {
            "total_operations": 0,
            "avg_response_time_ms": 0,
            "cache_hit_rate": 0,
            "error_rate": 0,
            "avg_validation_score": 0
        }
        
        # Calculate totals
        timing_metrics = [
            k for k in metrics.keys()
            if k.endswith("_duration_ms")
        ]
        
        if timing_metrics:
            total_time = sum(
                metrics[k]["sum"] for k in timing_metrics
            )
            total_count = sum(
                metrics[k]["count"] for k in timing_metrics
            )
            
            if total_count > 0:
                summary["avg_response_time_ms"] = total_time / total_count
                summary["total_operations"] = total_count
        
        # Calculate cache hit rate
        cache_hits = metrics.get("cache_hit", {}).get("count", 0)
        cache_misses = metrics.get("cache_miss", {}).get("count", 0)
        cache_total = cache_hits + cache_misses
        
        if cache_total > 0:
            summary["cache_hit_rate"] = (cache_hits / cache_total) * 100
        
        # Calculate error rate
        error_count = metrics.get("error_count", {}).get("sum", 0)
        if summary["total_operations"] > 0:
            summary["error_rate"] = (error_count / summary["total_operations"]) * 100
        
        # Calculate avg validation score
        validation_scores = metrics.get("validation_score", {})
        if validation_scores.get("count", 0) > 0:
            summary["avg_validation_score"] = validation_scores.get("avg", 0)
        
        return summary
    
    def get_health_status(self) -> Dict:
        """
        Get system health status.
        
        Returns:
            Dictionary with health status
        """
        metrics = self.telemetry.get_metrics_summary(last_n_minutes=60)
        summary = self._generate_summary(metrics)
        
        health = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "checks": {}
        }
        
        # Check response time
        if summary["avg_response_time_ms"] > 500:
            health["checks"]["response_time"] = {
                "status": "warning",
                "message": f"High response time: {summary['avg_response_time_ms']:.2f}ms"
            }
        else:
            health["checks"]["response_time"] = {
                "status": "ok",
                "value": summary["avg_response_time_ms"]
            }
        
        # Check cache hit rate
        if summary["cache_hit_rate"] < 90:
            health["checks"]["cache_hit_rate"] = {
                "status": "warning",
                "message": f"Low cache hit rate: {summary['cache_hit_rate']:.2f}%"
            }
        else:
            health["checks"]["cache_hit_rate"] = {
                "status": "ok",
                "value": summary["cache_hit_rate"]
            }
        
        # Check error rate
        if summary["error_rate"] > 5:
            health["checks"]["error_rate"] = {
                "status": "critical",
                "message": f"High error rate: {summary['error_rate']:.2f}%"
            }
            health["status"] = "unhealthy"
        elif summary["error_rate"] > 1:
            health["checks"]["error_rate"] = {
                "status": "warning",
                "message": f"Elevated error rate: {summary['error_rate']:.2f}%"
            }
        else:
            health["checks"]["error_rate"] = {
                "status": "ok",
                "value": summary["error_rate"]
            }
        
        # Check validation score
        if summary["avg_validation_score"] < 85:
            health["checks"]["validation_score"] = {
                "status": "warning",
                "message": f"Low validation score: {summary['avg_validation_score']:.2f}"
            }
        else:
            health["checks"]["validation_score"] = {
                "status": "ok",
                "value": summary["avg_validation_score"]
            }
        
        return health


if __name__ == "__main__":
    aggregator = MetricsAggregator()
    
    # Generate reports
    daily_report = aggregator.generate_daily_report()
    print("Daily Report:")
    print(json.dumps(daily_report["summary"], indent=2))
    
    health = aggregator.get_health_status()
    print("\nHealth Status:")
    print(json.dumps(health, indent=2))

