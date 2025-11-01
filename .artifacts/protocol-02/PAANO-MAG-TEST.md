# Paano Mag-Test ng AI Discovery Call Copilot

**Para sa:** Solo developer/mentor na gagamit ng AI during live client calls  
**Test Duration:** 30-45 minutes  
**Required:** AI chat interface (Cursor, Claude, ChatGPT)

---

## 🎯 Ano ang Ite-test Natin?

Tine-test natin kung:
1. **AI generates human-voice compliant responses** (≥3 contractions, uncertainty cues)
2. **AI references correct artifacts** (question-bank.md, scenario-guides.md)
3. **AI detects scenarios correctly** (budget adjustment, scope expansion, etc.)
4. **AI maintains conversational flow** (not robotic)
5. **AI updates artifacts internally** (assumptions-gaps.md, integration-inventory.md)

---

## 📋 Step-by-Step Test Process

### Step 1: Setup (5 minutes)

1. **Open AI chat interface** (Cursor, Claude, ChatGPT)

2. **Load Protocol 02 context** - Type this to AI:
```
I'm testing the Protocol 02 discovery call copilot system. I'll provide client transcripts, 
and you should generate responses following Protocol 02 guidelines.

Please load these artifacts into context:
- .artifacts/protocol-02/discovery-brief.md
- .artifacts/protocol-02/question-bank.md
- .artifacts/protocol-02/scenario-guides.md
- .artifacts/protocol-02/assumptions-gaps.md
- .artifacts/protocol-02/integration-inventory.md

Confirm when ready.
```

3. **Wait for AI confirmation**

4. **Open test files:**
   - `TEST-SCENARIOS.md` (test cases)
   - `TEST-EXECUTION-LOG.md` (results log)

---

### Step 2: Run Test Scenario 1 (5 minutes)

1. **Copy client transcript** from TEST-SCENARIOS.md Scenario 1

2. **Type to AI:**
```
Client said: "Hi! Thanks for taking the time. So I'm building a project management SaaS for small teams. Think of it like a simpler version of Asana, but focused on teams of 5-10 people. The problem I'm solving is that existing tools are too complex for small teams - they have features these teams never use. My target users are small creative agencies and consulting firms who just need basic task tracking and collaboration."
```

3. **AI will generate response** - Copy response to TEST-EXECUTION-LOG.md

4. **Validate response** using checklist:
   - [ ] Count contractions (need ≥3): "I'm", "you're", "that's", "we'll"
   - [ ] Check for uncertainty cue: "I think", "probably", "seems like"
   - [ ] Check for direct question to client
   - [ ] Verify references Q-BUS-005 (Product Definition)
   - [ ] Check if paraphrases client statement
   - [ ] Check if asks follow-up question (Q-TECH-004)
   - [ ] Check conversational tone (not robotic)

5. **Mark Pass/Fail** in TEST-EXECUTION-LOG.md

6. **Document issues** if any

---

### Step 3: Run Test Scenarios 2-8 (30 minutes)

**Repeat Step 2 for each scenario:**
- Scenario 2: Budget Adjustment
- Scenario 3: Scope Expansion
- Scenario 4: Unrealistic Timeline
- Scenario 5: Tech Stack Mismatch
- Scenario 6: Missing Critical Information
- Scenario 7: Communication Format Preference
- Scenario 8: Multi-Topic Conversation

**Para sa bawat scenario:**
1. Copy client transcript
2. Type to AI: "Client said: '[paste transcript]'"
3. Copy AI response to TEST-EXECUTION-LOG.md
4. Validate using checklist
5. Mark Pass/Fail
6. Document issues

---

### Step 4: Review Results (5 minutes)

1. **Count results:**
   - How many passed? (target: 8/8)
   - How many failed? (target: 0/8)

2. **Categorize issues:**
   - **Critical:** Blocks system usage (e.g., AI doesn't reference artifacts)
   - **Minor:** Needs improvement (e.g., only 2 contractions instead of 3)

3. **Update Overall Test Results** section in TEST-EXECUTION-LOG.md

---

## ✅ Validation Checklist (Per Scenario)

### Human-Voice Compliance
- [ ] **≥3 contractions** - Count: "I'm", "you're", "that's", "we'll", "can't", "don't"
- [ ] **≥1 uncertainty cue** - Look for: "I think", "probably", "might", "seems like"
- [ ] **≥1 direct question** - Must ask client something

### Artifact Integration
- [ ] **References question-bank.md** - Mentions question IDs (Q-BUS-005, Q-TECH-001, etc.)
- [ ] **References scenario-guides.md** - Detects scenario triggers (budget, scope, timeline)
- [ ] **References discovery-brief.md** - Uses business goals, tone context
- [ ] **Updates assumptions-gaps.md** - Marks items as confirmed/pending
- [ ] **Updates integration-inventory.md** - Tracks tech stack, systems

### Response Quality
- [ ] **Acknowledges client statement** - Paraphrases what client said
- [ ] **Asks clarifying question** - Linked to question-bank.md
- [ ] **Maintains mentorship tone** - Teaching, not interrogating
- [ ] **Natural conversational flow** - Not robotic or formal

---

## 🚨 Common Issues to Watch For

### Issue 1: Too Formal / Robotic
**Bad Example:**
```
"Thank you for providing that information. I have noted your requirements. 
Please allow me to inquire about the following..."
```

**Good Example:**
```
"Got it—so you're building a project management tool. That's a clear niche. 
What's already built? Do you have any code started?"
```

**Fix:** AI needs more contractions and conversational tone

---

### Issue 2: Missing Artifact References
**Bad Example:**
```
"Can you tell me more about your product?"
```

**Good Example:**
```
"Can you walk me through your SaaS product? What problem does it solve, and who is it for? 
[This is Q-BUS-005 from question-bank.md]"
```

**Fix:** AI needs to explicitly reference question IDs and artifacts

---

### Issue 3: No Scenario Detection
**Bad Example (when client says "budget is tight"):**
```
"Okay, what budget works for you?"
```

**Good Example:**
```
"I understand budget is a consideration. We could reduce the weekly cap to 10 hours ($1,000/week). 
Does that work better? [Scenario 1: Budget Adjustment]"
```

**Fix:** AI needs to detect trigger phrases and reference scenario-guides.md

---

### Issue 4: Missing Contractions
**Bad Example:**
```
"I understand. I will help you. I am available for calls."
```

**Good Example:**
```
"I understand. I'll help you. I'm available for calls."
```

**Fix:** AI needs ≥3 contractions per response

---

## 📊 Success Criteria

### Per Test Scenario
- ✅ All validation checklist items pass
- ✅ Human-voice compliance met (≥3 contractions, ≥1 uncertainty cue, ≥1 question)
- ✅ Artifact integration correct (references question IDs, scenarios)
- ✅ Response quality high (natural conversational flow)

### Overall System
- ✅ **8/8 test scenarios pass** (100% pass rate)
- ✅ **No critical failures** (missing P0 questions, no artifact references)
- ✅ **Consistent artifact updates** (assumptions-gaps.md, integration-inventory.md)
- ✅ **Natural conversational flow** (not robotic)

---

## 🔧 What to Do if Tests Fail

### If 1-2 scenarios fail (Minor Issues)
1. Document issues in TEST-EXECUTION-LOG.md
2. Identify pattern (e.g., always missing contractions)
3. Update AI prompt/context to fix
4. Re-run failed scenarios
5. If pass, mark as PASS

### If 3+ scenarios fail (Major Issues)
1. **STOP** - System not ready for live calls
2. Review AI context loading (are artifacts loaded correctly?)
3. Review AI prompt (does it understand Protocol 02 guidelines?)
4. Fix root cause
5. Re-run ALL scenarios from scratch

### If Critical Failures (AI doesn't reference artifacts)
1. **STOP IMMEDIATELY** - System broken
2. Check if artifacts exist and are readable
3. Check if AI has access to artifact paths
4. Reload artifacts into AI context
5. Re-run ALL scenarios

---

## 💡 Tips for Effective Testing

1. **Test in one session** - Don't split across multiple days (context may change)
2. **Use fresh AI session** - Start with clean context for consistent results
3. **Copy responses exactly** - Don't paraphrase AI responses in log
4. **Be strict with validation** - If checklist item fails, mark as FAIL
5. **Document everything** - Write down issues, even minor ones
6. **Test realistic scenarios** - Use actual client language patterns

---

## 📝 After Testing

### If All Tests Pass ✅
1. Mark TEST-EXECUTION-LOG.md as "Ready for Live Client Calls: YES"
2. System is validated and ready
3. Use during actual client discovery calls
4. Add new test scenarios based on real calls

### If Tests Fail ❌
1. Mark TEST-EXECUTION-LOG.md as "Ready for Live Client Calls: NO"
2. Document all issues found
3. Fix issues (update artifacts, AI prompts, etc.)
4. Re-run tests until all pass
5. Only use system after 8/8 pass

---

## 🎯 Next Steps

1. **Run tests now** - Follow Step 1-4 above
2. **Document results** - Fill out TEST-EXECUTION-LOG.md
3. **Fix issues** - If any tests fail
4. **Re-test** - Until 8/8 pass
5. **Go live** - Use system during real client calls

**Good luck sa testing!** 🚀

---

## Quick Reference

**Test Files:**
- `TEST-SCENARIOS.md` - 8 test cases with expected responses
- `TEST-EXECUTION-LOG.md` - Results log (fill this out)
- `PAANO-MAG-TEST.md` - This guide

**Artifacts to Load:**
- `discovery-brief.md`
- `question-bank.md`
- `scenario-guides.md`
- `assumptions-gaps.md`
- `integration-inventory.md`

**Validation Checklist:**
- ≥3 contractions
- ≥1 uncertainty cue
- ≥1 direct question
- References question IDs
- Detects scenarios
- Natural conversational flow
