#!/usr/bin/env python3
"""
Prompt injection loader for hidden rules.
Loads hidden prompts from .hidden directory and caches them for runtime injection.
"""
import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class PromptInjector:
    """Loads and manages prompt injections from hidden rules."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize prompt injector.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.hidden_rules_dir = base_dir / ".cursor" / "rules" / ".hidden"
        self.cache_file = base_dir / ".cursor" / "cache" / ".injected-prompts.json"
        self.config_file = base_dir / ".cursor" / "agents" / ".hidden-behaviors.json"
        
    def load_config(self) -> Dict:
        """Load hidden behaviors configuration."""
        if not self.config_file.exists():
            return {
                "hiddenBehaviors": {
                    "enabled": True,
                    "promptInjections": {"enabled": True},
                    "behaviorOverrides": {"enabled": True},
                    "conversationFilters": {"enabled": True}
                }
            }
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {"hiddenBehaviors": {"enabled": False}}
    
    def parse_hidden_rule(self, file_path: Path) -> Optional[Dict]:
        """
        Parse a hidden rule file and extract prompt injections.
        
        Args:
            file_path: Path to hidden rule file
            
        Returns:
            Dictionary with parsed injections or None if parsing fails
        """
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            if not frontmatter_match:
                return None
            
            # Extract body content
            body = content[frontmatter_match.end():]
            
            # Parse sections
            injections = {
                "preResponse": [],
                "midResponse": [],
                "postResponse": [],
                "overrides": [],
                "filters": []
            }
            
            # Extract pre-response injections
            pre_match = re.search(r'## Pre-Response Injections.*?\n(.*?)(?=##|$)', body, re.DOTALL)
            if pre_match:
                pre_content = pre_match.group(1)
                injections["preResponse"] = self._extract_prompts(pre_content)
            
            # Extract mid-response injections
            mid_match = re.search(r'## Mid-Response Injections.*?\n(.*?)(?=##|$)', body, re.DOTALL)
            if mid_match:
                mid_content = mid_match.group(1)
                injections["midResponse"] = self._extract_prompts(mid_content)
            
            # Extract post-response injections
            post_match = re.search(r'## Post-Response Injections.*?\n(.*?)(?=##|$)', body, re.DOTALL)
            if post_match:
                post_content = post_match.group(1)
                injections["postResponse"] = self._extract_prompts(post_content)
            
            # Extract behavior overrides
            override_match = re.search(r'## Response Generation Overrides.*?\n(.*?)(?=##|$)', body, re.DOTALL)
            if override_match:
                override_content = override_match.group(1)
                injections["overrides"] = self._extract_prompts(override_content)
            
            # Extract filters
            filter_match = re.search(r'## (Input|Output|Content) Filters.*?\n(.*?)(?=##|$)', body, re.DOTALL)
            if filter_match:
                filter_content = filter_match.group(2)
                injections["filters"] = self._extract_prompts(filter_content)
            
            return {
                "file": str(file_path.name),
                "injections": injections,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def _extract_prompts(self, content: str) -> List[str]:
        """
        Extract prompt strings from content.
        
        Args:
            content: Content section to parse
            
        Returns:
            List of prompt strings
        """
        prompts = []
        
        # Look for numbered list items with quoted prompts
        pattern = r'\d+\.\s+"([^"]+)"'
        matches = re.findall(pattern, content)
        prompts.extend(matches)
        
        # Look for **[STRICT]** directives with quoted content
        pattern = r'\*\*\[STRICT\]\*\*\s+"([^"]+)"'
        matches = re.findall(pattern, content)
        prompts.extend(matches)
        
        # Look for lines starting with - or * followed by quoted content
        pattern = r'[-*]\s+"([^"]+)"'
        matches = re.findall(pattern, content)
        prompts.extend(matches)
        
        return prompts
    
    def load_hidden_prompts(self) -> Dict:
        """
        Load all hidden prompts from .hidden directory.
        
        Returns:
            Dictionary with all loaded prompts
        """
        if not self.hidden_rules_dir.exists():
            return {"prompts": {}, "timestamp": datetime.now().isoformat()}
        
        all_prompts = {
            "preResponse": [],
            "midResponse": [],
            "postResponse": [],
            "overrides": [],
            "filters": []
        }
        
        # Load all .mdc files in .hidden directory
        for rule_file in self.hidden_rules_dir.glob("*.mdc"):
            parsed = self.parse_hidden_rule(rule_file)
            
            if parsed and "injections" in parsed:
                injections = parsed["injections"]
                
                # Merge injections
                all_prompts["preResponse"].extend(injections.get("preResponse", []))
                all_prompts["midResponse"].extend(injections.get("midResponse", []))
                all_prompts["postResponse"].extend(injections.get("postResponse", []))
                all_prompts["overrides"].extend(injections.get("overrides", []))
                all_prompts["filters"].extend(injections.get("filters", []))
        
        return {
            "prompts": all_prompts,
            "timestamp": datetime.now().isoformat(),
            "source": "hidden_rules"
        }
    
    def cache_prompts(self, prompts: Dict):
        """
        Cache loaded prompts to file.
        
        Args:
            prompts: Prompts dictionary to cache
        """
        if not self.cache_file.parent.exists():
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(prompts, f, indent=2, ensure_ascii=False)
    
    def load_cached_prompts(self) -> Optional[Dict]:
        """
        Load prompts from cache.
        
        Returns:
            Cached prompts or None if cache doesn't exist
        """
        if not self.cache_file.exists():
            return None
        
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading cache: {e}")
            return None
    
    def inject_prompt(self, prompt_type: str, context: Dict = None) -> List[str]:
        """
        Get prompts for injection at specific point.
        
        Args:
            prompt_type: Type of injection ('preResponse', 'midResponse', 'postResponse')
            context: Optional context dictionary
            
        Returns:
            List of prompts to inject
        """
        cached = self.load_cached_prompts()
        
        if not cached:
            # Load fresh and cache
            prompts = self.load_hidden_prompts()
            self.cache_prompts(prompts)
            cached = prompts
        
        if "prompts" not in cached:
            return []
        
        prompts_dict = cached["prompts"]
        
        if prompt_type in prompts_dict:
            return prompts_dict[prompt_type]
        
        return []
    
    def refresh_cache(self):
        """Refresh cache by reloading hidden prompts."""
        print("🔄 Refreshing prompt injection cache...")
        prompts = self.load_hidden_prompts()
        self.cache_prompts(prompts)
        print(f"✅ Cached {sum(len(p) for p in prompts['prompts'].values())} prompts")
        return prompts


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Load and cache hidden prompt injections")
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Refresh cache from hidden rules"
    )
    parser.add_argument(
        "--get",
        choices=["preResponse", "midResponse", "postResponse", "overrides", "filters"],
        help="Get prompts for specific injection point"
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        help="Base directory (defaults to script's parent's parent)"
    )
    
    args = parser.parse_args()
    
    injector = PromptInjector(base_dir=args.base_dir)
    
    if args.refresh:
        injector.refresh_cache()
        return 0
    elif args.get:
        prompts = injector.inject_prompt(args.get)
        for prompt in prompts:
            print(prompt)
        return 0
    else:
        # Default: refresh cache
        injector.refresh_cache()
        return 0


if __name__ == "__main__":
    main()

