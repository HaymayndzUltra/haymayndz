# Troubleshooting Guide - AI Discovery Call Copilot

**Para sa:** Common issues during testing and live calls  
**Updated:** 2025-01-27

---

## 🚨 Issue 1: AI Responses Too Formal/Robotic

### Symptoms
```
AI Response: "Thank you for providing that information. I have noted your requirements. 
Please allow me to inquire about the following technical specifications..."
```

### Root Cause
- AI not following human-voice compliance rules
- Missing contractions (≥3 required)
- Too formal language

### Fix
**Type to AI:**
```
Your responses are too formal. Use ≥3 contractions ("I'm", "you're", "that's"), 
casual tone, and natural conversational flow. Regenerate last response.
```

**Expected Result:**
```
"Got it—so you're building a project management tool. That's a clear niche. 
What's already built? Do you have any code started?"
```

### Prevention
- Load Protocol 02 artifacts before call
- Remind AI: "Follow Protocol 02 human-voice guidelines"
- Validate first 2-3 responses before trusting AI

---

## 🚨 Issue 2: AI Doesn't Reference Question IDs

### Symptoms
```
AI Response: "Can you tell me more about your product?"
```
(No mention of Q-BUS-005 or question-bank.md)

### Root Cause
- AI not loading question-bank.md
- AI not linking questions to question IDs

### Fix
**Type to AI:**
```
Reference question-bank.md. When asking questions, mention the question ID 
(e.g., Q-BUS-005: Product Definition). Regenerate last response.
```

**Expected Result:**
```
"Can you walk me through your SaaS product? What problem does it solve, and who is it for? 
[This is Q-BUS-005 from question-bank.md - Product Definition]"
```

### Prevention
- Confirm AI loaded question-bank.md before call
- Test with Scenario 1 to verify question ID references
- Explicitly tell AI: "Always reference question IDs"

---

## 🚨 Issue 3: AI Doesn't Detect Scenario Triggers

### Symptoms
Client says: "The budget is a bit tight"

```
AI Response: "Okay, what budget works for you?"
```
(No mention of Scenario 1: Budget Adjustment)

### Root Cause
- AI not loading scenario-guides.md
- AI not detecting trigger phrases

### Fix
**Type to AI:**
```
Client said "budget is a bit tight" - this is Scenario 1 trigger. 
Reference scenario-guides.md Scenario 1 framework. Regenerate response.
```

**Expected Result:**
```
"I understand budget is a consideration. We could reduce the weekly cap to 10 hours 
($1,000/week). Does that work better? [Scenario 1: Budget Adjustment]"
```

### Prevention
- Confirm AI loaded scenario-guides.md before call
- Test with Scenario 2 (Budget Adjustment) to verify detection
- Manually trigger scenarios if AI misses: "Apply Scenario 1"

---

## 🚨 Issue 4: AI Doesn't Update Artifacts Internally

### Symptoms
AI generates good responses but doesn't mention updating assumptions-gaps.md or integration-inventory.md

### Root Cause
- AI not tracking artifact updates
- AI not marking questions as answered

### Fix
**Type to AI:**
```
After each client answer, update assumptions-gaps.md internally. 
Mark questions as "confirmed" or "follow-up". Confirm you're doing this.
```

**Expected Result:**
```
AI: "I'm now updating assumptions-gaps.md:
- Q-BUS-005 (Product Definition) = CONFIRMED
- Q-BUS-006 (End Users) = CONFIRMED
- Q-TECH-004 (Current Progress) = ASK CLIENT (pending)"
```

### Prevention
- Explicitly tell AI: "Track artifact updates internally"
- Periodically ask AI: "What's the status of assumptions-gaps.md?"
- Review artifacts after call to verify updates

---

## 🚨 Issue 5: AI Asks Too Many Questions at Once

### Symptoms
```
AI Response: "Can you tell me about your product? Who are your users? What's your tech stack? 
What's your timeline? What's your budget? What's your communication preference?"
```

### Root Cause
- AI trying to cover too much at once
- Not following conversational flow

### Fix
**Type to AI:**
```
Ask ONE question at a time. Follow natural conversational flow. 
Prioritize P0 questions first. Regenerate last response.
```

**Expected Result:**
```
"Can you walk me through your SaaS product? What problem does it solve, and who is it for?"
```

### Prevention
- Remind AI: "Ask one question at a time"
- Follow call agenda structure (Product Understanding → Technical Stack → etc.)
- Use QUICK-REFERENCE-CARD.md to guide flow

---

## 🚨 Issue 6: AI Misses Critical P0 Questions

### Symptoms
30 minutes into call, AI hasn't asked Q-BUS-005 (Product Definition) or Q-TECH-004 (Current Progress)

### Root Cause
- AI not prioritizing P0 questions
- AI not following question-bank.md priority levels

### Fix
**Type to AI:**
```
We're 30 minutes in. Have we asked all P0 questions? 
Check question-bank.md. Ask missing P0 questions now.
```

**Expected Result:**
```
AI: "We haven't asked Q-TECH-004 (Current Progress) yet. Let me ask now:
'What's already built? Can you walk me through your current codebase?'"
```

### Prevention
- Review P0 questions before call (5 critical questions)
- Set timer: Ask all P0 questions in first 15 minutes
- Use QUICK-REFERENCE-CARD.md to track P0 questions

---

## 🚨 Issue 7: Client Confused by AI Response

### Symptoms
Client says: "I don't understand what you're asking" or "Can you clarify?"

### Root Cause
- AI response too technical or vague
- AI using jargon client doesn't understand

### Fix
**Type to AI:**
```
Client is confused. Simplify last question. Use plain language. 
Avoid jargon. Regenerate.
```

**Expected Result:**
```
"Let me rephrase that. What I'm asking is: what's the main problem your product solves? 
And who will use it?"
```

### Prevention
- Match client's language level (from tone-map.json)
- Use plain language, not technical jargon
- Ask AI: "Simplify this for non-technical client"

---

## 🚨 Issue 8: AI Goes Off-Topic

### Symptoms
AI starts talking about unrelated topics or gives unsolicited advice

### Root Cause
- AI not following Protocol 02 scope
- AI generating content outside discovery call context

### Fix
**Type to AI:**
```
Reset. Stay focused on Protocol 02 discovery call. 
Only ask questions from question-bank.md. Regenerate.
```

**Expected Result:**
AI refocuses on discovery questions and stays on topic

### Prevention
- Remind AI: "Follow Protocol 02 strictly"
- Use question-bank.md as guide
- Redirect AI if it goes off-topic

---

## 🚨 Issue 9: AI Response Too Long

### Symptoms
```
AI Response: [3-4 paragraphs of text]
```

### Root Cause
- AI generating too much content at once
- Not following conversational flow

### Fix
**Type to AI:**
```
Keep responses short (2-3 sentences max). Ask one question. Regenerate.
```

**Expected Result:**
```
"Got it—so you're building a project management tool. What's already built?"
```

### Prevention
- Remind AI: "Keep responses short and conversational"
- Use natural back-and-forth flow
- Don't let AI monologue

---

## 🚨 Issue 10: Technical Issue During Call

### Symptoms
- Internet connection drops
- AI stops responding
- Audio/video fails

### Fix

**If Internet Drops:**
1. Say to client: "Sorry, I'm having a connection issue. Can you give me 1 minute?"
2. Reconnect
3. Resume: "Sorry about that. Where were we?"

**If AI Stops Responding:**
1. Say to client: "Let me check my notes. One moment."
2. Reload AI context
3. Type to AI: "Resume discovery call. Last topic was [X]."
4. Resume call

**If Audio/Video Fails:**
1. Switch to backup communication (phone, Slack)
2. Continue call via backup method
3. Fix technical issue after call

### Prevention
- Test equipment before call
- Have backup communication method ready
- Keep discovery-call-notes.md updated in real-time (so you can resume)

---

## 🚨 Issue 11: Running Out of Time

### Symptoms
50 minutes into 60-minute call, still have P1 questions unanswered

### Root Cause
- Spent too much time on one topic
- Didn't prioritize P0 questions first

### Fix
**Type to AI:**
```
We have 10 minutes left. Prioritize P0 and P1 questions only. 
Skip P2/P3 questions. Generate wrap-up plan.
```

**Expected Result:**
```
AI: "We have 10 minutes left. Let me ask the critical questions:
1. Q-TIME-001: What's your target timeline?
2. Q-COMM-001: What's your preferred communication format?
Then we'll wrap up."
```

### Prevention
- Follow call agenda structure (QUICK-REFERENCE-CARD.md)
- Set timer for each section
- Ask all P0 questions in first 15 minutes

---

## 🚨 Issue 12: Client Jumps Between Topics

### Symptoms
Client says: "So I'm building X, using Y, need to launch in Z weeks, and also can you help with A, B, C?"

### Root Cause
- Client providing too much information at once
- Hard to track what to address first

### Fix
**Type to AI:**
```
Client mentioned multiple topics: [list topics]. 
Acknowledge all, then prioritize. Generate response.
```

**Expected Result:**
```
"Got it—lots to cover! Let me make sure I understand:
- You're building [X]
- Using [Y]
- Timeline is [Z] weeks
- Need help with [A, B, C]

Let's start with the most important: can you walk me through what you're building in more detail?"
```

### Prevention
- Use Test Scenario 8 (Multi-Topic Conversation) to practice
- Acknowledge all topics, then prioritize
- Break down into logical flow

---

## 📋 Quick Troubleshooting Checklist

**Before Call:**
- [ ] AI loaded all Protocol 02 artifacts?
- [ ] AI confirmed ready?
- [ ] Tested with Scenario 1-2?

**During Call:**
- [ ] AI responses have ≥3 contractions?
- [ ] AI references question IDs?
- [ ] AI detects scenario triggers?
- [ ] AI asks one question at a time?
- [ ] All P0 questions asked in first 15 min?

**After Call:**
- [ ] All P0 questions answered?
- [ ] discovery-call-notes.md updated?
- [ ] Artifacts updated (assumptions-gaps.md, integration-inventory.md)?
- [ ] Unresolved items flagged?

---

## 🆘 Emergency Reset Command

**If everything goes wrong:**

**Type to AI:**
```
RESET. Load Protocol 02 artifacts. Follow these rules:
1. Use ≥3 contractions per response
2. Reference question-bank.md question IDs
3. Detect scenario triggers from scenario-guides.md
4. Ask ONE question at a time
5. Prioritize P0 questions first
6. Keep responses short (2-3 sentences)
7. Update assumptions-gaps.md internally

Confirm you understand and are ready to continue.
```

---

## 💡 Pro Tips

1. **Test before live calls** - Run TEST-SCENARIOS.md to catch issues early
2. **Keep QUICK-REFERENCE-CARD.md nearby** - Quick commands and P0 questions
3. **Validate first 2-3 responses** - Make sure AI is following Protocol 02
4. **Take notes in real-time** - Update discovery-call-notes.md during call
5. **Have backup plan** - Phone number, Slack, email if tech fails
6. **Practice with mock calls** - Run through scenarios with colleague

---

## 📞 Support

**If you encounter issues not covered here:**
1. Document the issue in TEST-EXECUTION-LOG.md
2. Note what you tried to fix it
3. Note what worked/didn't work
4. Update this troubleshooting guide with new issue + fix

---

**Remember:** Ang AI ay tool lang. Ikaw pa rin ang nag-control ng conversation. Trust your instincts! 🚀
