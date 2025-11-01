#!/usr/bin/env python3
"""
Response validation pipeline for humanization compliance.
Validates responses against FECS rules and humanization requirements.
"""
import re
from typing import Dict, List, Tuple, Optional


class ResponseValidator:
    """Validates responses for humanization compliance."""
    
    def __init__(self):
        """Initialize validator with default thresholds."""
        self.min_contractions = 3
        self.max_sentence_length = 20
        self.max_technical_sentence_length = 25
        self.require_warmth_marker = True
        self.require_uncertainty_cue = True
        
        # Forbidden phrases (common examples - should be loaded from humanization-log.json)
        self.forbidden_phrases = [
            "I'm an AI",
            "as an AI",
            "I don't have",
            "I cannot",
            "I'm not able to",
            "I'm unable to",
            "I apologize, but",
            "I'm sorry, but"
        ]
        
        # Warmth markers
        self.warmth_markers = {
            "vocatives": ["sir", "ma'am", "boss", "ate", "kuya"],
            "tag_questions": ["no?", "right?", "di ba?", "okay?", "ok?"],
            "softeners": ["maybe", "I think", "probably", "seems like", "perhaps"]
        }
        
        # Contraction patterns
        self.contraction_patterns = [
            r"\bI'm\b", r"\byou're\b", r"\bthat's\b", r"\bit's\b",
            r"\bwe're\b", r"\bcan't\b", r"\bdon't\b", r"\bwon't\b",
            r"\bisn't\b", r"\baren't\b", r"\bhasn't\b", r"\bhaven't\b",
            r"\bdidn't\b", r"\bdoesn't\b", r"\bwouldn't\b", r"\bcouldn't\b",
            r"\bshouldn't\b", r"\bmustn't\b", r"\bmightn't\b", r"\bI'll\b",
            r"\byou'll\b", r"\bwe'll\b", r"\bthey'll\b", r"\bhe'll\b",
            r"\bshe'll\b", r"\bit'll\b"
        ]
    
    def validate_response(self, response: str, is_technical: bool = False) -> Dict:
        """
        Validate response against humanization requirements.
        
        Args:
            response: Response text to validate
            is_technical: Whether response contains technical content
            
        Returns:
            Dictionary with validation results and score
        """
        results = {
            "valid": True,
            "score": 0.0,
            "errors": [],
            "warnings": [],
            "metrics": {}
        }
        
        # Count contractions
        contraction_count = self.count_contractions(response)
        results["metrics"]["contractions"] = contraction_count
        
        if contraction_count < self.min_contractions:
            results["errors"].append(
                f"Too few contractions: {contraction_count}/{self.min_contractions} required"
            )
            results["valid"] = False
        
        # Check sentence length
        sentence_lengths = self.get_sentence_lengths(response)
        max_length = self.max_technical_sentence_length if is_technical else self.max_sentence_length
        long_sentences = [len for len in sentence_lengths if len > max_length]
        results["metrics"]["sentence_lengths"] = sentence_lengths
        results["metrics"]["max_length"] = max_length
        
        if long_sentences:
            results["errors"].append(
                f"Sentences too long: {len(long_sentences)} sentence(s) exceed {max_length} words"
            )
            results["valid"] = False
        
        # Check warmth markers
        warmth_count = self.count_warmth_markers(response)
        results["metrics"]["warmth_markers"] = warmth_count
        
        if self.require_warmth_marker and warmth_count == 0:
            results["warnings"].append("No warmth markers found (vocatives, tag questions, or softeners)")
        
        # Check for forbidden phrases
        forbidden_found = self.check_forbidden_phrases(response)
        results["metrics"]["forbidden_phrases"] = forbidden_found
        
        if forbidden_found:
            results["errors"].append(
                f"Forbidden phrases detected: {', '.join(forbidden_found)}"
            )
            results["valid"] = False
        
        # Check uncertainty cues
        uncertainty_count = self.count_uncertainty_cues(response)
        results["metrics"]["uncertainty_cues"] = uncertainty_count
        
        if self.require_uncertainty_cue and uncertainty_count == 0:
            results["warnings"].append("No uncertainty cues found")
        
        # Calculate score
        results["score"] = self.calculate_score(results)
        
        return results
    
    def count_contractions(self, text: str) -> int:
        """
        Count contractions in text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Number of contractions found
        """
        count = 0
        text_lower = text.lower()
        
        for pattern in self.contraction_patterns:
            matches = re.findall(pattern, text_lower)
            count += len(matches)
        
        return count
    
    def count_warmth_markers(self, text: str) -> int:
        """
        Count warmth markers in text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Number of warmth markers found
        """
        count = 0
        text_lower = text.lower()
        
        # Count vocatives
        for vocative in self.warmth_markers["vocatives"]:
            if vocative in text_lower:
                count += 1
                break  # Count once per type
        
        # Count tag questions
        for tag in self.warmth_markers["tag_questions"]:
            if tag in text_lower:
                count += 1
                break
        
        # Count softeners
        for softener in self.warmth_markers["softeners"]:
            if softener in text_lower:
                count += 1
                break
        
        return count
    
    def check_forbidden_phrases(self, text: str) -> List[str]:
        """
        Check for forbidden phrases in text.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of forbidden phrases found
        """
        found = []
        text_lower = text.lower()
        
        for phrase in self.forbidden_phrases:
            if phrase.lower() in text_lower:
                found.append(phrase)
        
        return found
    
    def count_uncertainty_cues(self, text: str) -> int:
        """
        Count uncertainty cues in text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Number of uncertainty cues found
        """
        uncertainty_patterns = [
            r"\bI think\b", r"\bmaybe\b", r"\bprobably\b", r"\bperhaps\b",
            r"\bseems like\b", r"\bmight\b", r"\bcould be\b", r"\bpossibly\b",
            r"\bI'm not sure\b", r"\bI guess\b", r"\bI suppose\b"
        ]
        
        count = 0
        text_lower = text.lower()
        
        for pattern in uncertainty_patterns:
            matches = re.findall(pattern, text_lower)
            count += len(matches)
        
        return count
    
    def get_sentence_lengths(self, text: str) -> List[int]:
        """
        Get word counts for each sentence.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of word counts per sentence
        """
        # Split by sentence-ending punctuation
        sentences = re.split(r'[.!?]+', text)
        
        lengths = []
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                words = sentence.split()
                lengths.append(len(words))
        
        return lengths
    
    def calculate_score(self, results: Dict) -> float:
        """
        Calculate overall validation score.
        
        Args:
            results: Validation results dictionary
            
        Returns:
            Score from 0.0 to 100.0
        """
        metrics = results.get("metrics", {})
        errors = results.get("errors", [])
        warnings = results.get("warnings", [])
        
        score = 100.0
        
        # Penalize for errors
        score -= len(errors) * 20.0
        
        # Penalize for warnings
        score -= len(warnings) * 5.0
        
        # Bonus for exceeding minimum contractions
        contractions = metrics.get("contractions", 0)
        if contractions > self.min_contractions:
            score += min(5.0, (contractions - self.min_contractions) * 2.0)
        
        # Bonus for warmth markers
        warmth = metrics.get("warmth_markers", 0)
        if warmth > 0:
            score += min(5.0, warmth * 2.5)
        
        # Ensure score is within bounds
        score = max(0.0, min(100.0, score))
        
        return score


def main():
    """Main entry point for CLI usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate response for humanization compliance")
    parser.add_argument(
        "response",
        nargs="?",
        help="Response text to validate (or read from stdin)"
    )
    parser.add_argument(
        "--technical",
        action="store_true",
        help="Response contains technical content"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    
    args = parser.parse_args()
    
    # Get response text
    if args.response:
        response_text = args.response
    else:
        import sys
        response_text = sys.stdin.read()
    
    if not response_text.strip():
        print("Error: No response text provided")
        return 1
    
    # Validate
    validator = ResponseValidator()
    results = validator.validate_response(response_text, is_technical=args.technical)
    
    # Output results
    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        print(f"Validation Score: {results['score']:.1f}/100")
        print(f"Valid: {'✅ Yes' if results['valid'] else '❌ No'}")
        
        if results['errors']:
            print("\nErrors:")
            for error in results['errors']:
                print(f"  - {error}")
        
        if results['warnings']:
            print("\nWarnings:")
            for warning in results['warnings']:
                print(f"  - {warning}")
        
        print(f"\nMetrics:")
        for key, value in results['metrics'].items():
            print(f"  - {key}: {value}")
    
    return 0 if results['valid'] else 1


if __name__ == "__main__":
    main()

