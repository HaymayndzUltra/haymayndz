# Quick Start Guide - Protocol 02 Discovery Call System

**Location:** `/home/haymayndz/.nv/`  
**Purpose:** Get started with AI-powered discovery calls in 5 minutes

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Load Context (30 seconds)
```bash
cd /home/haymayndz/.nv
python3 .cursor/scripts/load_context.py
```

**Expected Output:**
```
✅ Context Loading Complete!
   📊 Total Files: 42
   📏 Total Size: 313,302 characters
   🎯 Ready for Discovery Call!
```

### Step 2: Review Critical Files (2 minutes)
```bash
# P0 Critical Questions (must ask in first 15 min)
cat .artifacts/protocol-02/question-bank.md | grep "P0"

# Scenario Triggers (watch for these phrases)
cat .artifacts/protocol-02/scenario-guides.md | grep "Trigger Phrases"

# Quick Reference Card (print this!)
cat .artifacts/protocol-02/QUICK-REFERENCE-CARD.md
```

### Step 3: Test System (2 minutes)
```bash
# Run one test scenario to verify AI works
# Open TEST-SCENARIOS.md and try Scenario 1
```

**Test Input:**
```
Client said: "Hi! I'm building a project management SaaS for small teams."
```

**Expected AI Response:**
- ✅ Has ≥3 contractions
- ✅ References Q-BUS-005 (Product Definition)
- ✅ Asks follow-up question
- ✅ Natural conversational tone

### Step 4: Start Discovery Call! 🎯
You're ready! Use QUICK-REFERENCE-CARD.md during call.

---

## 📁 Key Files

### Before Call
- ✅ `QUICK-REFERENCE-CARD.md` - Print and keep beside you
- ✅ `question-bank.md` - 30+ prioritized questions
- ✅ `scenario-guides.md` - 6 scenario frameworks
- ✅ `discovery-brief.md` - Business goals and context

### During Call
- ✅ `discovery-call-notes.md` - Real-time notes template
- ✅ `USER-GUIDE-during-client-call.md` - Step-by-step guide

### After Call
- ✅ `discovery-recap.md` - Client-facing summary
- ✅ `client-discovery-form.md` - Confirmed requirements

### Testing
- ✅ `TEST-SCENARIOS.md` - 8 test cases
- ✅ `PAANO-MAG-TEST.md` - Testing guide
- ✅ `TROUBLESHOOTING-GUIDE.md` - Issue resolution

### Context System
- ✅ `HOW-TO-USE-CONTEXT-PRELOAD.md` - Complete guide
- ✅ `.cursor/scripts/load_context.py` - Context loader
- ✅ `.cursor/cache/preload_context.json` - Loaded context

---

## 🎯 P0 Critical Questions (Must Ask First 15 Min)

1. **Q-BUS-005: Product Definition**
   "Can you walk me through what you're building? What problem does it solve, and who is it for?"

2. **Q-BUS-006: End Users**
   "Who are the end users of your SaaS product?"

3. **Q-TECH-004: Current Progress**
   "What's already built? Can you walk me through your current codebase?"

4. **Q-BUS-001: Weekly Time Commitment**
   "What's your expected weekly time commitment? 5-10 hours, 10-15 hours, or something else?"

5. **Q-TIME-001: Timeline & Milestones**
   "What's your target timeline for MVP launch? And when do you need to be production-ready?"

---

## 🚨 Scenario Triggers (Watch For These)

### Scenario 1: Budget Adjustment
**Triggers:** "budget is tight", "can we do this for less?", "start smaller"  
**Response:** Offer 10-hour option ($1,000/week), maintain $100/hr rate

### Scenario 2: Scope Expansion
**Triggers:** "write some code", "help with implementation", "can you build"  
**Response:** Clarify expectations, offer hybrid approach

### Scenario 4: Unrealistic Timeline
**Triggers:** "launch in X weeks", "is this realistic?", "move faster"  
**Response:** Reality check, focus on MVP scope

### Scenario 5: Tech Stack Mismatch
**Triggers:** "using different tech", "switching to", "are you familiar with"  
**Response:** Honest about expertise, offer general guidance

---

## ✅ Pre-Call Checklist

- [ ] Context loaded (`python3 .cursor/scripts/load_context.py`)
- [ ] QUICK-REFERENCE-CARD.md printed
- [ ] P0 questions reviewed
- [ ] Scenario triggers memorized
- [ ] discovery-call-notes.md template open
- [ ] Audio/video tested
- [ ] AI agent ready

---

## 🎤 During Call Flow

```
Client speaks → You type to AI → AI generates response → You read to client
```

**Example:**
```
Client: "We're building a SaaS for project management."

You type: "Client said: 'We're building a SaaS for project management.'"

AI generates: "Got it—so you're building a project management SaaS. 
Can you walk me through what problem it solves? And who are your target users?"

You read: [Read AI response to client]
```

---

## 📊 Success Criteria

**Call is successful if:**
- ✅ All P0 questions answered (5 critical questions)
- ✅ AI responses are human-voice compliant (≥3 contractions)
- ✅ discovery-call-notes.md updated in real-time
- ✅ Client feels heard and understood
- ✅ Clear next steps established

---

## 🆘 Emergency Commands

### If AI Goes Off-Track
```
Reset. Follow Protocol 02. Reference question-bank.md.
```

### If Client Confused
```
Client seems confused. Simplify and clarify.
```

### If Running Out of Time
```
We have 10 minutes left. Prioritize P0 questions only.
```

---

## 📞 Support

**Need help?**
1. Check `TROUBLESHOOTING-GUIDE.md` first
2. Review `HOW-TO-USE-CONTEXT-PRELOAD.md`
3. Test with `TEST-SCENARIOS.md`

---

## 🎯 Next Steps

1. ✅ **Load context** - Run load_context.py
2. ✅ **Test system** - Try Scenario 1 from TEST-SCENARIOS.md
3. ✅ **Print reference card** - QUICK-REFERENCE-CARD.md
4. ✅ **Practice** - Run 2-3 mock calls
5. ✅ **Go live** - Use during real discovery call!

---

**You're ready!** 🚀

Ang system mo ngayon may:
- ✅ 42 files preloaded (313K+ characters)
- ✅ 30+ prioritized questions
- ✅ 6 scenario frameworks
- ✅ 8 test cases
- ✅ Complete troubleshooting guide

**Good luck sa discovery call!** 💪
