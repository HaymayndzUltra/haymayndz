#!/usr/bin/env python3
"""
Incremental context cache update system.
Only refreshes changed files in the cache instead of reloading everything.
"""
import os
import json
import time
from pathlib import Path
from typing import Dict, List, Set, Optional
from watch_artifacts import ArtifactWatcher


class IncrementalContextUpdater:
    """Manages incremental updates to context cache."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize incremental updater.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.cache_file = base_dir / ".cursor" / "cache" / "preload_context.json"
        self.watcher = ArtifactWatcher(base_dir=base_dir)
        
    def load_cache(self) -> Dict:
        """Load existing cache file."""
        if not self.cache_file.exists():
            return {"files": [], "metadata": {}}
        
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading cache: {e}")
            return {"files": [], "metadata": {}}
    
    def save_cache(self, cache_data: Dict):
        """Save cache to file."""
        cache_data["metadata"]["last_updated"] = time.time()
        
        if not self.cache_file.parent.exists():
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Create backup
        if self.cache_file.exists():
            backup_file = self.cache_file.with_suffix('.json.backup')
            import shutil
            shutil.copy2(self.cache_file, backup_file)
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, indent=2, ensure_ascii=False)
    
    def get_file_metadata(self, file_path: Path) -> Optional[Dict]:
        """
        Get metadata for a file.
        
        Args:
            file_path: Path to file
            
        Returns:
            Dictionary with file metadata or None if file doesn't exist
        """
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            rel_path = os.path.relpath(file_path, self.base_dir)
            
            return {
                "path": rel_path,
                "full_path": str(file_path),
                "content": content,
                "size": len(content),
                "type": file_path.suffix,
                "mtime": os.path.getmtime(file_path)
            }
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None
    
    def update_stale_files(self, stale_files: Set[str]) -> int:
        """
        Update stale files in cache.
        
        Args:
            stale_files: Set of file paths (relative to base_dir) that are stale
            
        Returns:
            Number of files updated
        """
        cache_data = self.load_cache()
        files_map = {f["path"]: idx for idx, f in enumerate(cache_data.get("files", []))}
        
        updated_count = 0
        
        for file_path in stale_files:
            full_path = self.base_dir / file_path
            
            if not full_path.exists():
                # File deleted - remove from cache
                if file_path in files_map:
                    del cache_data["files"][files_map[file_path]]
                    updated_count += 1
                continue
            
            # Get updated metadata
            metadata = self.get_file_metadata(full_path)
            
            if metadata:
                if file_path in files_map:
                    # Update existing entry
                    cache_data["files"][files_map[file_path]] = metadata
                else:
                    # Add new entry
                    cache_data["files"].append(metadata)
                
                updated_count += 1
                print(f"  ✓ Updated: {file_path}")
        
        # Recalculate metadata
        cache_data["metadata"] = {
            "total_files": len(cache_data["files"]),
            "total_size": sum(f.get("size", 0) for f in cache_data["files"]),
            "last_updated": time.time()
        }
        
        self.save_cache(cache_data)
        return updated_count
    
    def refresh_changed_files(self) -> int:
        """
        Check for stale files and refresh them.
        
        Returns:
            Number of files refreshed
        """
        print("🔍 Checking for stale files...")
        staleness_map = self.watcher.check_staleness()
        
        stale_files = {path for path, is_stale in staleness_map.items() if is_stale}
        
        if not stale_files:
            print("✅ No stale files found")
            return 0
        
        print(f"🔄 Found {len(stale_files)} stale file(s), updating...")
        updated_count = self.update_stale_files(stale_files)
        print(f"✅ Updated {updated_count} file(s)")
        
        return updated_count
    
    def add_file(self, file_path: Path) -> bool:
        """
        Add a new file to cache.
        
        Args:
            file_path: Path to file to add
            
        Returns:
            True if added successfully
        """
        metadata = self.get_file_metadata(file_path)
        
        if not metadata:
            return False
        
        cache_data = self.load_cache()
        files_map = {f["path"]: idx for idx, f in enumerate(cache_data.get("files", []))}
        
        rel_path = metadata["path"]
        
        if rel_path in files_map:
            # Update existing
            cache_data["files"][files_map[rel_path]] = metadata
        else:
            # Add new
            cache_data["files"].append(metadata)
        
        # Recalculate metadata
        cache_data["metadata"] = {
            "total_files": len(cache_data["files"]),
            "total_size": sum(f.get("size", 0) for f in cache_data["files"]),
            "last_updated": time.time()
        }
        
        self.save_cache(cache_data)
        return True


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Incremental context cache updater")
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Refresh stale files"
    )
    parser.add_argument(
        "--add",
        type=Path,
        help="Add specific file to cache"
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        help="Base directory (defaults to script's parent's parent)"
    )
    
    args = parser.parse_args()
    
    updater = IncrementalContextUpdater(base_dir=args.base_dir)
    
    if args.add:
        if updater.add_file(args.add):
            print(f"✅ Added {args.add} to cache")
            return 0
        else:
            print(f"❌ Failed to add {args.add}")
            return 1
    elif args.refresh:
        updated = updater.refresh_changed_files()
        return 0 if updated >= 0 else 1
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    main()

