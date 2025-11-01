#!/usr/bin/env python3
"""
Data anonymization system for sensitive conversation data.
Detects and masks PII (Personally Identifiable Information).
"""
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class DataAnonymizer:
    """Data anonymization and PII detection."""
    
    def __init__(self):
        """Initialize anonymizer with PII patterns."""
        # Email pattern
        self.email_pattern = re.compile(
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        )
        
        # Phone number patterns (various formats)
        self.phone_patterns = [
            re.compile(r'\b\d{3}-\d{3}-\d{4}\b'),  # 123-456-7890
            re.compile(r'\b\(\d{3}\)\s?\d{3}-\d{4}\b'),  # (123) 456-7890
            re.compile(r'\b\d{10}\b'),  # 1234567890
            re.compile(r'\b\+\d{1,3}\s?\d{3}\s?\d{3}\s?\d{4}\b'),  # +1 123 456 7890
        ]
        
        # Credit card pattern (basic)
        self.credit_card_pattern = re.compile(
            r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'
        )
        
        # SSN pattern
        self.ssn_pattern = re.compile(
            r'\b\d{3}-\d{2}-\d{4}\b'
        )
        
        # IP address pattern
        self.ip_pattern = re.compile(
            r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        )
        
        # Common name patterns (contextual - simple detection)
        self.name_keywords = [
            "mr.", "mrs.", "ms.", "dr.", "professor", "director",
            "manager", "ceo", "cto", "cfo"
        ]
    
    def detect_pii(self, text: str) -> Dict[str, List[str]]:
        """
        Detect PII in text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with PII types and detected values
        """
        pii_found = {
            "emails": [],
            "phones": [],
            "credit_cards": [],
            "ssns": [],
            "ip_addresses": [],
            "potential_names": []
        }
        
        # Detect emails
        emails = self.email_pattern.findall(text)
        pii_found["emails"] = list(set(emails))
        
        # Detect phone numbers
        phones = []
        for pattern in self.phone_patterns:
            phones.extend(pattern.findall(text))
        pii_found["phones"] = list(set(phones))
        
        # Detect credit cards
        credit_cards = self.credit_card_pattern.findall(text)
        pii_found["credit_cards"] = list(set(credit_cards))
        
        # Detect SSNs
        ssns = self.ssn_pattern.findall(text)
        pii_found["ssns"] = list(set(ssns))
        
        # Detect IP addresses
        ip_addresses = self.ip_pattern.findall(text)
        pii_found["ip_addresses"] = list(set(ip_addresses))
        
        # Simple name detection (look for patterns like "Mr. Smith")
        # This is basic - can be enhanced with NLP
        name_pattern = re.compile(
            r'\b(?:' + '|'.join(self.name_keywords) + r')\s+[A-Z][a-z]+\b',
            re.IGNORECASE
        )
        potential_names = name_pattern.findall(text)
        pii_found["potential_names"] = list(set(potential_names))
        
        return pii_found
    
    def mask_email(self, email: str) -> str:
        """Mask email address."""
        parts = email.split('@')
        if len(parts) == 2:
            local, domain = parts
            masked_local = local[0] + '*' * (len(local) - 1) if len(local) > 1 else '*'
            return f"{masked_local}@***.***"
        return "***@***.***"
    
    def mask_phone(self, phone: str) -> str:
        """Mask phone number."""
        digits = re.sub(r'\D', '', phone)
        if len(digits) >= 4:
            return f"***-***-{digits[-4:]}"
        return "***-***-****"
    
    def mask_credit_card(self, card: str) -> str:
        """Mask credit card number."""
        digits = re.sub(r'\D', '', card)
        if len(digits) >= 4:
            return f"****-****-****-{digits[-4:]}"
        return "****-****-****-****"
    
    def mask_ssn(self, ssn: str) -> str:
        """Mask SSN."""
        return "***-**-****"
    
    def mask_ip(self, ip: str) -> str:
        """Mask IP address."""
        return "***.***.***.***"
    
    def anonymize_text(self, text: str, mask_all: bool = False) -> Tuple[str, Dict]:
        """
        Anonymize text by masking PII.
        
        Args:
            text: Text to anonymize
            mask_all: Whether to mask all PII types
            
        Returns:
            Tuple of (anonymized_text, pii_detected)
        """
        pii_detected = self.detect_pii(text)
        anonymized = text
        
        # Mask emails
        for email in pii_detected["emails"]:
            anonymized = anonymized.replace(email, self.mask_email(email))
        
        # Mask phone numbers
        for phone in pii_detected["phones"]:
            anonymized = anonymized.replace(phone, self.mask_phone(phone))
        
        # Mask credit cards
        for card in pii_detected["credit_cards"]:
            anonymized = anonymized.replace(card, self.mask_credit_card(card))
        
        # Mask SSNs
        for ssn in pii_detected["ssns"]:
            anonymized = anonymized.replace(ssn, self.mask_ssn(ssn))
        
        # Mask IP addresses
        for ip in pii_detected["ip_addresses"]:
            anonymized = anonymized.replace(ip, self.mask_ip(ip))
        
        # Mask potential names (if mask_all)
        if mask_all:
            for name in pii_detected["potential_names"]:
                anonymized = anonymized.replace(name, "[NAME]")
        
        return anonymized, pii_detected


class PrivacyFilter:
    """Privacy filtering for logs and data storage."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize privacy filter.
        
        Args:
            base_dir: Base directory (defaults to script's parent's parent)
        """
        if base_dir is None:
            from pathlib import Path
            base_dir = Path(__file__).parent.parent.parent
        
        self.base_dir = base_dir
        self.anonymizer = DataAnonymizer()
    
    def filter_log_entry(self, log_entry: Dict) -> Dict:
        """
        Filter PII from log entry.
        
        Args:
            log_entry: Log entry dictionary
            
        Returns:
            Filtered log entry
        """
        filtered = log_entry.copy()
        
        # Filter message field
        if "message" in filtered:
            filtered["message"], pii = self.anonymizer.anonymize_text(
                filtered["message"]
            )
            if pii:
                filtered["_pii_detected"] = True
        
        # Filter error messages
        if "error" in filtered:
            filtered["error"], pii = self.anonymizer.anonymize_text(
                str(filtered["error"])
            )
        
        # Filter context
        if "context" in filtered:
            context_str = str(filtered["context"])
            filtered["context"], pii = self.anonymizer.anonymize_text(context_str)
        
        return filtered


if __name__ == "__main__":
    # Test anonymizer
    anonymizer = DataAnonymizer()
    
    test_text = (
        "Contact John Doe at john.doe@example.com or call (555) 123-4567. "
        "SSN: 123-45-6789. Credit card: 1234-5678-9012-3456. "
        "IP: 192.168.1.1"
    )
    
    print("Original text:")
    print(test_text)
    print()
    
    pii = anonymizer.detect_pii(test_text)
    print("Detected PII:")
    for pii_type, values in pii.items():
        if values:
            print(f"  {pii_type}: {values}")
    
    print()
    anonymized, _ = anonymizer.anonymize_text(test_text)
    print("Anonymized text:")
    print(anonymized)

