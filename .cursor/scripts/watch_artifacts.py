#!/usr/bin/env python3
"""
File watcher for artifact changes in Protocol 02 discovery call system.
Monitors artifacts directory for changes and triggers incremental cache updates.
"""
import os
import json
import time
from pathlib import Path
from typing import Dict, Set, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent, FileCreatedEvent, FileDeletedEvent


class ArtifactChangeHandler(FileSystemEventHandler):
    """Handler for artifact file system events."""
    
    def __init__(self, cache_file: Path, artifacts_base: Path, callback=None):
        """
        Initialize handler.
        
        Args:
            cache_file: Path to cache file that tracks metadata
            artifacts_base: Base directory for artifacts
            callback: Optional callback function to call when changes detected
        """
        self.cache_file = cache_file
        self.artifacts_base = artifacts_base
        self.callback = callback
        self.changed_files: Set[str] = set()
        
    def on_modified(self, event):
        """Handle file modification events."""
        if not event.is_directory:
            self._handle_file_change(event.src_path)
    
    def on_created(self, event):
        """Handle file creation events."""
        if not event.is_directory:
            self._handle_file_change(event.src_path)
    
    def on_deleted(self, event):
        """Handle file deletion events."""
        if not event.is_directory:
            self._handle_file_change(event.src_path)
    
    def _handle_file_change(self, file_path: str):
        """Process file change event."""
        try:
            rel_path = os.path.relpath(file_path, self.artifacts_base.parent)
            # Only track artifact files
            if 'artifacts' in rel_path or 'rules' in rel_path or 'protocol' in rel_path.lower():
                self.changed_files.add(rel_path)
                if self.callback:
                    self.callback(rel_path)
        except Exception as e:
            print(f"Error handling file change for {file_path}: {e}")
    
    def get_changed_files(self) -> Set[str]:
        """Get set of changed files since last check."""
        changed = self.changed_files.copy()
        self.changed_files.clear()
        return changed


class ArtifactWatcher:
    """File watcher for monitoring artifact changes."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize artifact watcher.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.cache_file = base_dir / ".cursor" / "cache" / "preload_context.json"
        self.artifacts_base = base_dir / ".artifacts"
        self.rules_base = base_dir / ".cursor" / "rules"
        self.protocols_base = base_dir / ".cursor" / "ai-driven-workflow"
        
        self.observer = Observer()
        self.handler: Optional[ArtifactChangeHandler] = None
        
    def start(self):
        """Start watching for file changes."""
        if not self.cache_file.parent.exists():
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Create handler with callback
        callback = lambda path: self._on_change_detected(path)
        self.handler = ArtifactChangeHandler(
            self.cache_file,
            self.artifacts_base,
            callback=callback
        )
        
        # Watch multiple directories
        watch_dirs = []
        if self.artifacts_base.exists():
            watch_dirs.append(str(self.artifacts_base))
        if self.rules_base.exists():
            watch_dirs.append(str(self.rules_base))
        if self.protocols_base.exists():
            watch_dirs.append(str(self.protocols_base))
        
        for watch_dir in watch_dirs:
            self.observer.schedule(self.handler, watch_dir, recursive=True)
        
        self.observer.start()
        print(f"✅ Watching for changes in: {', '.join(watch_dirs)}")
        
    def stop(self):
        """Stop watching for file changes."""
        self.observer.stop()
        self.observer.join()
        
    def _on_change_detected(self, file_path: str):
        """Handle change detection callback."""
        print(f"🔄 Change detected: {file_path}")
        
    def check_staleness(self) -> Dict[str, bool]:
        """
        Check if cached files are stale compared to source artifacts.
        
        Returns:
            Dictionary mapping file paths to staleness status (True = stale)
        """
        if not self.cache_file.exists():
            return {}
        
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            staleness_map = {}
            
            # Check each file in cache
            for file_entry in cache_data.get('files', []):
                cache_path = file_entry.get('path')
                cache_mtime = file_entry.get('mtime', 0)
                
                # Find corresponding source file
                source_path = self.base_dir / cache_path
                
                if source_path.exists():
                    source_mtime = os.path.getmtime(source_path)
                    is_stale = source_mtime > cache_mtime
                    staleness_map[cache_path] = is_stale
                else:
                    # File deleted
                    staleness_map[cache_path] = True
            
            return staleness_map
            
        except Exception as e:
            print(f"Error checking staleness: {e}")
            return {}
    
    def run_forever(self):
        """Run watcher indefinitely."""
        try:
            self.start()
            print("🔄 Watcher running. Press Ctrl+C to stop.")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n⏹️  Stopping watcher...")
            self.stop()


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Watch for artifact changes")
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Check staleness and exit (don't watch)"
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        help="Base directory (defaults to script's parent's parent)"
    )
    
    args = parser.parse_args()
    
    watcher = ArtifactWatcher(base_dir=args.base_dir)
    
    if args.check_only:
        staleness = watcher.check_staleness()
        stale_count = sum(1 for is_stale in staleness.values() if is_stale)
        
        if stale_count > 0:
            print(f"⚠️  {stale_count} file(s) are stale:")
            for path, is_stale in staleness.items():
                if is_stale:
                    print(f"  - {path}")
            return 1
        else:
            print("✅ All files are up to date")
            return 0
    else:
        watcher.run_forever()


if __name__ == "__main__":
    main()

