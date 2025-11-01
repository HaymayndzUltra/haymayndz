# Quick Reference Card - AI Discovery Call Copilot

**Para sa:** Live client discovery calls  
**Print this:** Keep beside you during video calls

---

## 🎯 HOW IT WORKS

```
Client speaks → You type to AI → AI generates response → You read to client
```

**Your Role:**
1. **Listen** to client during video call
2. **Type** client statements to AI (transcribe)
3. **Read** AI-generated responses to client
4. **Update** discovery-call-notes.md in real-time

---

## 📋 BEFORE CALL CHECKLIST

- [ ] Load Protocol 02 artifacts into AI
- [ ] Review discovery-brief.md (5 min)
- [ ] Review question-bank.md (5 min)
- [ ] Review scenario-guides.md (5 min)
- [ ] Open discovery-call-notes.md template
- [ ] Test audio/video equipment
- [ ] Tell AI: "I'm starting a discovery call. Generate responses following Protocol 02."

---

## 🎤 DURING CALL - QUICK COMMANDS

### When Client Speaks
**Type to AI:**
```
Client said: "[paste what client said]"
```

### When You Need Specific Question
**Type to AI:**
```
Ask Q-BUS-005 (Product Definition)
```

### When Scenario Detected
**Type to AI:**
```
Client mentioned budget is tight. Apply Scenario 1.
```

### When You Need Summary
**Type to AI:**
```
Summarize key decisions so far.
```

---

## 🚨 CRITICAL QUESTIONS (P0) - MUST ASK FIRST 15 MIN

1. **Q-BUS-005:** Product Definition  
   "Can you walk me through what you're building? What problem does it solve, and who is it for?"

2. **Q-BUS-006:** End Users  
   "Who are the end users of your SaaS product?"

3. **Q-TECH-004:** Current Progress  
   "What's already built? Can you walk me through your current codebase?"

4. **Q-BUS-001:** Weekly Time Commitment  
   "What's your expected weekly time commitment? 5-10 hours, 10-15 hours, or something else?"

5. **Q-TIME-001:** Timeline & Milestones  
   "What's your target timeline for MVP launch? And when do you need to be production-ready?"

---

## 🎭 SCENARIO TRIGGERS - WATCH FOR THESE PHRASES

### Scenario 1: Budget Adjustment
**Triggers:** "budget is tight", "can we do this for less?", "start smaller"  
**Response:** Offer 10-hour option ($1,000/week), maintain $100/hr rate

### Scenario 2: Scope Expansion
**Triggers:** "write some code", "help with implementation", "can you build"  
**Response:** Clarify expectations, offer hybrid approach, maintain mentorship focus

### Scenario 3: Compliance Gap
**Triggers:** "handle sensitive data", "need HIPAA", "GDPR", "compliance"  
**Response:** Assess gap, evaluate impact, provide architectural guidance (not legal)

### Scenario 4: Unrealistic Timeline
**Triggers:** "launch in X weeks", "is this realistic?", "move faster"  
**Response:** Reality check, focus on MVP scope, prioritize features

### Scenario 5: Tech Stack Mismatch
**Triggers:** "using different tech", "switching to", "are you familiar with"  
**Response:** Honest about expertise, offer general guidance, evaluate tech decisions

### Scenario 6: Communication Format
**Triggers:** "prefer async", "not great with calls", "different format"  
**Response:** Show flexibility, establish expectations, confirm response times

---

## ✅ VALIDATION - CHECK EVERY AI RESPONSE

**Human-Voice Compliance:**
- [ ] ≥3 contractions ("I'm", "you're", "that's")
- [ ] ≥1 uncertainty cue ("I think", "probably", "seems like")
- [ ] ≥1 direct question to client

**Artifact Integration:**
- [ ] References question IDs (Q-BUS-005, Q-TECH-001, etc.)
- [ ] Detects scenario triggers (budget, scope, timeline)
- [ ] Natural conversational flow (not robotic)

**If AI response fails validation:**
1. Don't read it to client
2. Type to AI: "Regenerate with more contractions and natural tone"
3. Validate again before reading

---

## 📝 REAL-TIME NOTE-TAKING

**Update discovery-call-notes.md:**
```markdown
## Product Understanding
- Client Answer: [what client said]
- Status: confirmed | follow-up | risk
- Question ID: Q-BUS-005
- Next Action: [if needed]

## Technical Stack
- Tech Stack: React + Firebase (confirmed)
- Status: confirmed
- Question ID: Q-TECH-001
- Notes: [any concerns]
```

---

## 🎯 CALL STRUCTURE (60 minutes)

### Introductions (5 min)
- Introduce yourself
- Ask for note-taking consent
- Set expectations

### Product Understanding (15 min) ⚠️ CRITICAL
- Q-BUS-005: Product Definition
- Q-BUS-006: End Users
- Q-TECH-004: Current Progress

### Technical Stack (15 min)
- Q-TECH-001: Tech Stack Validation
- Q-TECH-002: AI/LLM Integrations
- Q-INT-001: Third-Party Integrations

### Engagement Structure (10 min)
- Q-FUNC-001: Role Boundaries
- Q-BUS-002: Budget & Pricing
- Q-COMM-001: Communication Format

### Timeline & Milestones (10 min)
- Q-TIME-001: Timeline & Milestones
- Q-TIME-003: MVP Scope

### Wrap-up (5-10 min)
- Summarize key decisions
- Confirm next steps
- Set follow-up date

---

## 🚨 EMERGENCY COMMANDS

### If AI Goes Off-Track
**Type to AI:**
```
Reset. Follow Protocol 02. Reference question-bank.md.
```

### If Client Confused
**Type to AI:**
```
Client seems confused. Simplify and clarify.
```

### If Running Out of Time
**Type to AI:**
```
We have 10 minutes left. Prioritize P0 questions only.
```

### If Technical Issue
**Say to client:**
```
"Sorry, I'm having a technical issue. Can you give me 30 seconds?"
```
**Then fix issue, resume**

---

## ✅ AFTER CALL CHECKLIST

### Immediate (< 1 hour)
- [ ] Tell AI: "Call ended. Generate post-call summary."
- [ ] Review discovery-call-notes.md completeness
- [ ] Verify all P0 questions answered
- [ ] Flag unresolved items

### Within 24 Hours
- [ ] Tell AI: "Draft discovery-recap.md based on call notes."
- [ ] Review AI-generated recap
- [ ] Send recap to client via email
- [ ] Update discovery-approval-log.json

### Within 48 Hours
- [ ] Update all post-call artifacts:
  - client-discovery-form.md
  - scope-clarification.md
  - timeline-discussion.md
  - communication-plan.md
- [ ] Archive call transcript
- [ ] Mark Protocol 02 complete

---

## 💡 QUICK TIPS

1. **Type fast** - Transcribe client statements ASAP for real-time AI responses
2. **Read naturally** - Don't sound robotic when reading AI responses
3. **Take notes** - Update discovery-call-notes.md during call
4. **Trust AI** - AI references Protocol 02 artifacts automatically
5. **Stay organized** - Follow call agenda structure
6. **Capture tone** - Note client communication style for AI reference

---

## 📞 EXAMPLE EXCHANGE

**Client:** "We're building a SaaS for project management."

**You type to AI:** "Client said: 'We're building a SaaS for project management.'"

**AI generates:** "Got it—so you're building a project management SaaS. Can you walk me through what problem it solves? And who are your target users?"

**You read to client:** "Got it—so you're building a project management SaaS. Can you walk me through what problem it solves? And who are your target users?"

**Client responds** → **You type to AI** → **AI generates** → **You read to client**

**Repeat this pattern for entire call.**

---

## 🎯 SUCCESS CRITERIA

**Call is successful if:**
- ✅ All P0 questions answered (5 critical questions)
- ✅ AI responses are human-voice compliant
- ✅ discovery-call-notes.md updated in real-time
- ✅ Client feels heard and understood
- ✅ Clear next steps established

---

**Print this card and keep it beside you during calls!** 🚀
