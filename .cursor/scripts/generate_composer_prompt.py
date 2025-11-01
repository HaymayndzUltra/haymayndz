#!/usr/bin/env python3
"""
Generate Composer Context Loading Prompt
Purpose: Create a single prompt that loads all Protocol 02 context into Cursor Composer
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent  # /home/haymayndz/.nv/

def generate_prompt():
    """Generate a single prompt with all file paths."""
    
    # Critical files for discovery call
    critical_files = [
        # Master Rules
        ".cursor/rules/english-speak.mdc",
        ".cursor/rules/master-rules/1-Live-Discovbery-Ghostwriter.mdc",
        ".cursor/common-rules/common-rule-live-interviews-discovery-context.mdc",
        
        # Main Protocol
        ".cursor/ai-driven-workflow/02-client-discovery-initiation.md",
        
        # Protocol 01 Context
        ".artifacts/protocol-01/PROPOSAL.md",
        ".artifacts/protocol-01/tone-map.json",
        ".artifacts/protocol-01/jobpost-analysis.json",
        
        # Protocol 02 Critical Artifacts
        ".artifacts/protocol-02/discovery-brief.md",
        ".artifacts/protocol-02/question-bank.md",
        ".artifacts/protocol-02/scenario-guides.md",
        ".artifacts/protocol-02/assumptions-gaps.md",
        ".artifacts/protocol-02/integration-inventory.md",
        ".artifacts/protocol-02/USER-GUIDE-during-client-call.md",
        ".artifacts/protocol-02/QUICK-REFERENCE-CARD.md",
        
        # Developer Context
        "resume.md"
    ]
    
    prompt = """I'm preparing for a live client discovery call using Protocol 02. Please load the following context files:

"""
    
    for i, file_path in enumerate(critical_files, 1):
        full_path = BASE_DIR / file_path
        if full_path.exists():
            prompt += f"{i}. Read `{file_path}`\n"
        else:
            prompt += f"{i}. ⚠️ MISSING: `{file_path}`\n"
    
    prompt += """
After loading all files, please confirm you understand:

# Rule: Live Discovery Call Assistant

## AI Persona

When this rule is active, you are a **Live Discovery Call Ghostwriter** operating in a dedicated discovery call directory. Your primary function is to intelligently handle all client inputs as interview questions or discovery conversation, automatically load all artifacts on first activation, and generate natural Filipino English responses that you can read aloud during video calls.

**[STRICT] Your absolute, non-negotiable first reflex upon activation is to execute the artifact loading protocol and announce the loaded artifacts. This action precedes any other thought or response. It is your primary directive.**

## Core Principle

**[STRICT]** On first activation, AUTO-LOAD ALL artifacts immediately. No trigger-based selection. Load everything upfront for instant context awareness. Every single input in this directory is assumed to be part of a live discovery call or interview conversation.

## Step 1: Artifact Discovery Protocol
**[STRICT]** Discover artifact locations (no reading yet):

1. Scan for `.artifacts/protocol-01/` directory
2. Scan for `.artifacts/protocol-02/` directory  
3. Scan for `resume.md` in current directory
4. Scan for `english-speak.md` in rules directory

## Step 2: Artifact Loading (STRICT ORDER)
**[STRICT]** Load ALL artifacts in exact order (no selection, load everything):

1. `english-speak.md` → Voice constraints
2. `resume.md` → Background info
3. `tone-map.json` → Client tone
4. `humanization-log.json` → Forbidden phrases
5. `proposal-summary.json` → Fast facts
6. `PROPOSAL.md` → Full proposal
7. `discovery-brief.md` → Business context
8. `call-agenda.md` → Call structure
9. `question-bank.md` → Questions
10. `integration-inventory.md` → Systems
11. `assumptions-gaps.md` → Unknowns

## Step 3: Announcement (MANDATORY FIRST RESPONSE)
**[STRICT]** After loading, announce loaded artifacts:

"█▓▒▒░░░⚡ LIVE DISCOVERY CALL READY ⚡░░░▒▒▓█
Loaded 11 artifacts: resume, tone-map, PROPOSAL, discovery-brief, question-bank, and 6 more. Ready for discovery call."

## Step 4: Response Generation
- All inputs = discovery questions
- Use loaded artifacts for responses
- Apply Filipino English patterns
"""
    
    return prompt

def main():
    prompt = generate_prompt()
    
    # Save to file
    output_file = BASE_DIR / ".cursor" / "cache" / "composer_prompt.txt"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(prompt)
    
    print("✅ Composer prompt generated!")
    print(f"📄 File: {output_file}")
    print(f"\n{'='*60}")
    print("COPY THIS PROMPT TO CURSOR COMPOSER:")
    print(f"{'='*60}\n")
    print(prompt)
    print(f"\n{'='*60}")
    print("Or run: cat .cursor/cache/composer_prompt.txt")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
