#!/usr/bin/env python3
"""
Performance baseline measurement system.
Establishes baseline metrics before Phase 1 implementation.
"""
import json
import time
from pathlib import Path
from typing import Dict, Optional, Callable, Any
from datetime import datetime
from telemetry import Telemetry


class PerformanceBaseline:
    """Performance baseline measurement."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize baseline measurement.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.benchmarks_dir = base_dir / ".cursor" / "benchmarks"
        self.benchmarks_dir.mkdir(parents=True, exist_ok=True)
        self.baseline_file = self.benchmarks_dir / "baseline_metrics.json"
        self.telemetry = Telemetry(base_dir=base_dir)
    
    def measure_cache_refresh(self) -> Dict:
        """
        Measure cache refresh performance.
        
        Returns:
            Dictionary with timing metrics
        """
        from incremental_context_update import IncrementalContextUpdater
        
        updater = IncrementalContextUpdater(base_dir=self.base_dir)
        
        start_time = time.time()
        try:
            updated_count = updater.refresh_changed_files()
            duration_ms = (time.time() - start_time) * 1000
            
            return {
                "operation": "cache_refresh",
                "duration_ms": duration_ms,
                "files_updated": updated_count,
                "success": True
            }
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            return {
                "operation": "cache_refresh",
                "duration_ms": duration_ms,
                "success": False,
                "error": str(e)
            }
    
    def measure_validation(self, sample_response: str = None) -> Dict:
        """
        Measure validation performance.
        
        Args:
            sample_response: Sample response to validate (uses default if None)
            
        Returns:
            Dictionary with timing metrics
        """
        from validate_response import ResponseValidator
        
        if sample_response is None:
            sample_response = (
                "I think maybe we can finish this already, sir. "
                "The feature, we deploy it tomorrow, tomorrow. "
                "It's working already, no?"
            )
        
        validator = ResponseValidator()
        
        start_time = time.time()
        try:
            results = validator.validate_response(sample_response)
            duration_ms = (time.time() - start_time) * 1000
            
            return {
                "operation": "validation",
                "duration_ms": duration_ms,
                "score": results["score"],
                "valid": results["valid"],
                "success": True
            }
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            return {
                "operation": "validation",
                "duration_ms": duration_ms,
                "success": False,
                "error": str(e)
            }
    
    def measure_artifact_loading(self) -> Dict:
        """
        Measure artifact loading performance.
        
        Returns:
            Dictionary with timing metrics
        """
        from watch_artifacts import ArtifactWatcher
        
        watcher = ArtifactWatcher(base_dir=self.base_dir)
        
        start_time = time.time()
        try:
            staleness = watcher.check_staleness()
            duration_ms = (time.time() - start_time) * 1000
            
            return {
                "operation": "artifact_loading",
                "duration_ms": duration_ms,
                "files_checked": len(staleness),
                "stale_files": sum(1 for v in staleness.values() if v),
                "success": True
            }
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            return {
                "operation": "artifact_loading",
                "duration_ms": duration_ms,
                "success": False,
                "error": str(e)
            }
    
    def measure_prompt_injection(self) -> Dict:
        """
        Measure prompt injection loading performance.
        
        Returns:
            Dictionary with timing metrics
        """
        from inject_prompts import PromptInjector
        
        injector = PromptInjector(base_dir=self.base_dir)
        
        start_time = time.time()
        try:
            prompts = injector.load_hidden_prompts()
            duration_ms = (time.time() - start_time) * 1000
            
            prompt_count = sum(len(p) for p in prompts.get("prompts", {}).values())
            
            return {
                "operation": "prompt_injection",
                "duration_ms": duration_ms,
                "prompts_loaded": prompt_count,
                "success": True
            }
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            return {
                "operation": "prompt_injection",
                "duration_ms": duration_ms,
                "success": False,
                "error": str(e)
            }
    
    def establish_baseline(self) -> Dict:
        """
        Establish baseline metrics for all operations.
        
        Returns:
            Dictionary with baseline metrics
        """
        print("📊 Establishing performance baseline...")
        
        baseline = {
            "timestamp": datetime.now().isoformat(),
            "version": "pre-phase-1",
            "measurements": {}
        }
        
        # Measure cache refresh
        print("  Measuring cache refresh...")
        baseline["measurements"]["cache_refresh"] = self.measure_cache_refresh()
        
        # Measure validation
        print("  Measuring validation...")
        baseline["measurements"]["validation"] = self.measure_validation()
        
        # Measure artifact loading
        print("  Measuring artifact loading...")
        baseline["measurements"]["artifact_loading"] = self.measure_artifact_loading()
        
        # Measure prompt injection
        print("  Measuring prompt injection...")
        baseline["measurements"]["prompt_injection"] = self.measure_prompt_injection()
        
        # Calculate summary
        baseline["summary"] = self._calculate_summary(baseline["measurements"])
        
        # Save baseline
        with open(self.baseline_file, 'w', encoding='utf-8') as f:
            json.dump(baseline, f, indent=2)
        
        print(f"✅ Baseline established: {self.baseline_file}")
        print(f"   Summary: {baseline['summary']}")
        
        return baseline
    
    def _calculate_summary(self, measurements: Dict) -> Dict:
        """
        Calculate summary from measurements.
        
        Args:
            measurements: Measurements dictionary
            
        Returns:
            Summary dictionary
        """
        summary = {
            "total_operations": len(measurements),
            "successful_operations": 0,
            "failed_operations": 0,
            "avg_duration_ms": 0,
            "max_duration_ms": 0,
            "min_duration_ms": float('inf')
        }
        
        durations = []
        
        for operation, result in measurements.items():
            if result.get("success"):
                summary["successful_operations"] += 1
                duration = result.get("duration_ms", 0)
                durations.append(duration)
            else:
                summary["failed_operations"] += 1
        
        if durations:
            summary["avg_duration_ms"] = sum(durations) / len(durations)
            summary["max_duration_ms"] = max(durations)
            summary["min_duration_ms"] = min(durations)
        else:
            summary["min_duration_ms"] = 0
        
        return summary
    
    def load_baseline(self) -> Optional[Dict]:
        """
        Load baseline metrics.
        
        Returns:
            Baseline dictionary or None if not found
        """
        if not self.baseline_file.exists():
            return None
        
        try:
            with open(self.baseline_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading baseline: {e}")
            return None
    
    def compare_with_current(self) -> Dict:
        """
        Compare current performance with baseline.
        
        Returns:
            Dictionary with comparison results
        """
        baseline = self.load_baseline()
        
        if not baseline:
            return {
                "error": "Baseline not found. Run establish_baseline() first."
            }
        
        # Measure current performance
        current_measurements = {}
        current_measurements["cache_refresh"] = self.measure_cache_refresh()
        current_measurements["validation"] = self.measure_validation()
        current_measurements["artifact_loading"] = self.measure_artifact_loading()
        current_measurements["prompt_injection"] = self.measure_prompt_injection()
        
        # Compare
        comparison = {
            "baseline_timestamp": baseline["timestamp"],
            "current_timestamp": datetime.now().isoformat(),
            "comparisons": {}
        }
        
        for operation in baseline["measurements"]:
            baseline_metric = baseline["measurements"][operation]
            current_metric = current_measurements.get(operation)
            
            if not current_metric:
                continue
            
            baseline_duration = baseline_metric.get("duration_ms", 0)
            current_duration = current_metric.get("duration_ms", 0)
            
            if baseline_duration > 0:
                change_percent = ((current_duration - baseline_duration) / baseline_duration) * 100
            else:
                change_percent = 0
            
            comparison["comparisons"][operation] = {
                "baseline_ms": baseline_duration,
                "current_ms": current_duration,
                "change_percent": change_percent,
                "improvement": change_percent < 0
            }
        
        return comparison


if __name__ == "__main__":
    baseline = PerformanceBaseline()
    
    # Establish baseline
    baseline_metrics = baseline.establish_baseline()
    
    print("\nBaseline Metrics:")
    print(json.dumps(baseline_metrics["summary"], indent=2))

