# Load Discovery Call Context

**Purpose:** Load all Protocol 02 artifacts into Cursor Composer for discovery call support

---

## Instructions for Cursor Composer

Please load the following files into your context:

### Master Rules (4 files)
1. Read `.cursor/rules/english-speak.mdc`
2. Read `.cursor/rules/master-rules/1-Live-Discovbery-Ghostwriter.mdc`
3. Read `.cursor/common-rules/common-rule-live-discovery-call-assistant.mdc`
4. Read `.cursor/common-rules/common-rule-live-interviews-discovery-context.mdc`

### Protocols (3 files)
5. Read `.cursor/ai-driven-workflow/01-client-proposal-generation.md`
6. Read `.cursor/ai-driven-workflow/02-client-discovery-initiation.md`
7. Read `.cursor/ai-driven-workflow/03-project-brief-creation.md`

### Protocol 01 Artifacts (9 files)
8. Read `.artifacts/protocol-01/PROPOSAL.md`
9. Read `.artifacts/protocol-01/tone-map.json`
10. Read `.artifacts/protocol-01/jobpost-analysis.json`
11. Read `.artifacts/protocol-01/humanization-log.json`
12. Read `.artifacts/protocol-01/proposal-summary.json`
13. Read `.artifacts/protocol-01/job-post.md`
14. Read `.artifacts/protocol-01/notes.md`
15. Read `.artifacts/protocol-01/pricing-analysis.json`
16. Read `.artifacts/protocol-01/validation-report.md`

### Protocol 02 Critical Artifacts (10 files)
17. Read `.artifacts/protocol-02/discovery-brief.md`
18. Read `.artifacts/protocol-02/question-bank.md`
19. Read `.artifacts/protocol-02/scenario-guides.md`
20. Read `.artifacts/protocol-02/assumptions-gaps.md`
21. Read `.artifacts/protocol-02/integration-inventory.md`
22. Read `.artifacts/protocol-02/call-agenda.md`
23. Read `.artifacts/protocol-02/ready-for-call-summary.md`
24. Read `.artifacts/protocol-02/discovery-call-notes.md`
25. Read `.artifacts/protocol-02/USER-GUIDE-during-client-call.md`
26. Read `.artifacts/protocol-02/QUICK-REFERENCE-CARD.md`

### Developer Context
27. Read `resume.md`

---

## After Loading Context

Once all files are loaded, confirm by saying:

"✅ Context loaded. I have access to:
- 4 Master Rules
- 3 Protocols (01, 02, 03)
- 9 Protocol 01 Artifacts
- 10 Protocol 02 Critical Artifacts
- 1 Developer Context

Total: 27 critical files loaded.

I'm ready to assist with Protocol 02 - Client Discovery Initiation. I will:
- Generate human-voice compliant responses (≥3 contractions)
- Reference question-bank.md question IDs
- Detect scenario triggers from scenario-guides.md
- Maintain conversational tone
- Update assumptions-gaps.md internally

Ready for discovery call!"

---

## Usage

**To load context, type in Composer:**
```
@load-discovery-context.md
```

Or manually say:
```
Load all Protocol 02 context files following the instructions in 
.cursor/commands/load-discovery-context.md
```
