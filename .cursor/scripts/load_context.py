#!/usr/bin/env python3
"""
Context Preload Script for Protocol 02 Discovery Call Copilot
Purpose: Scan all rule, protocol, and artifact files → write to .cursor/cache/preload_context.json
"""
import os
import json
import glob
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent  # /home/haymayndz/.nv/

def load_files(pattern, base_dir):
    """Load all files matching pattern and return structured context."""
    context = []
    full_pattern = str(base_dir / pattern)
    
    for file_path in glob.glob(full_pattern, recursive=True):
        if file_path.endswith((".md", ".mdc", ".json", ".yaml", ".yml")):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    relative_path = os.path.relpath(file_path, base_dir)
                    
                    context.append({
                        "path": relative_path,
                        "full_path": file_path,
                        "content": content,
                        "size": len(content),
                        "type": Path(file_path).suffix
                    })
                    print(f"  ✓ Loaded: {relative_path} ({len(content)} chars)")
            except Exception as e:
                print(f"  ✗ Failed to load {file_path}: {e}")
    
    return context

def main():
    print("🔄 Loading Protocol 02 Context Files...")
    print(f"📁 Base Directory: {BASE_DIR}\n")
    
    # Define knowledge paths to scan
    knowledge_paths = [
        # Master Rules
        ".cursor/rules/**/*.md",
        ".cursor/rules/**/*.mdc",
        
        # Common Rules
        ".cursor/common-rules/**/*.md",
        ".cursor/common-rules/**/*.mdc",
        
        # AI-Driven Workflow Protocols
        ".cursor/ai-driven-workflow/**/*.md",
        
        # Protocol 01 Artifacts (Upstream Dependencies)
        ".artifacts/protocol-01/**/*.json",
        ".artifacts/protocol-01/**/*.md",
        
        # Protocol 02 Artifacts (Discovery Call)
        ".artifacts/protocol-02/**/*.json",
        ".artifacts/protocol-02/**/*.md",
        
        # Resume (Developer Context)
        "resume.md"
    ]
    
    all_context = []
    stats = {
        "rules": 0,
        "protocols": 0,
        "artifacts": 0,
        "total_size": 0
    }
    
    for path in knowledge_paths:
        print(f"\n📂 Scanning: {path}")
        files = load_files(path, BASE_DIR)
        all_context.extend(files)
        
        # Update stats
        for file in files:
            stats["total_size"] += file["size"]
            if "rules" in file["path"]:
                stats["rules"] += 1
            elif "ai-driven-workflow" in file["path"]:
                stats["protocols"] += 1
            elif "artifacts" in file["path"]:
                stats["artifacts"] += 1
    
    # Create cache directory if it doesn't exist
    cache_dir = BASE_DIR / ".cursor" / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # Write to cache
    cache_file = cache_dir / "preload_context.json"
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump({
            "metadata": {
                "total_files": len(all_context),
                "total_size": stats["total_size"],
                "rules": stats["rules"],
                "protocols": stats["protocols"],
                "artifacts": stats["artifacts"],
                "generated_at": "2025-01-27"
            },
            "context": all_context
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Context Loading Complete!")
    print(f"   📊 Total Files: {len(all_context)}")
    print(f"   📏 Total Size: {stats['total_size']:,} characters")
    print(f"   📜 Rules: {stats['rules']}")
    print(f"   📋 Protocols: {stats['protocols']}")
    print(f"   📦 Artifacts: {stats['artifacts']}")
    print(f"   💾 Cache File: {cache_file}")
    print(f"\n🎯 Ready for Discovery Call!")

if __name__ == "__main__":
    main()
