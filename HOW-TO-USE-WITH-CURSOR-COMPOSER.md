# How to Use Protocol 02 with Cursor Composer

**Issue:** Cursor Composer doesn't automatically load context from `.cursor/cache/preload_context.json`

**Solution:** Manual context loading using generated prompts

---

## 🚀 Quick Start (2 Methods)

### **Method 1: Copy-Paste Prompt (Fastest)**

**Step 1: Generate Prompt**
```bash
cd /home/haymayndz/.nv
python3 .cursor/scripts/generate_composer_prompt.py
```

**Step 2: Copy Prompt**
```bash
cat .cursor/cache/composer_prompt.txt
```

**Step 3: Paste to Composer**
- Open Cursor Composer (Cmd+I or Ctrl+I)
- Paste the entire prompt
- Wait for Composer to load all 15 files
- Composer will confirm: "✅ Context loaded. Ready for discovery call!"

**Time:** ~1-2 minutes

---

### **Method 2: Use @-mention Command**

**Step 1: Open Composer**
- Press Cmd+I (Mac) or Ctrl+I (Windows/Linux)

**Step 2: Type**
```
@.cursor/commands/load-discovery-context.md
```

**Step 3: Wait for Context Load**
- Composer will read the command file
- Composer will load all 27 files listed
- Composer will confirm when ready

**Time:** ~2-3 minutes

---

## 📋 What Gets Loaded

### Method 1 (Quick - 15 files)
**Critical files only:**
- 3 Master Rules
- 1 Main Protocol (02)
- 3 Protocol 01 Context
- 7 Protocol 02 Critical Artifacts
- 1 Developer Context

### Method 2 (Complete - 27 files)
**All files:**
- 4 Master Rules
- 3 Protocols (01, 02, 03)
- 9 Protocol 01 Artifacts
- 10 Protocol 02 Artifacts
- 1 Developer Context

---

## ✅ Verification

**After loading, Composer should:**
1. Confirm context loaded
2. Understand Protocol 02 guidelines
3. Know response requirements (≥3 contractions, etc.)
4. Reference question IDs (Q-BUS-005, etc.)
5. Detect scenario triggers

**Test it:**
```
Client said: "We're building a SaaS for project management."
```

**Expected Response:**
- ✅ Has ≥3 contractions
- ✅ References Q-BUS-005 (Product Definition)
- ✅ Asks follow-up question
- ✅ Natural conversational tone

---

## 🎯 During Discovery Call

### Workflow
```
Client speaks → You type to Composer → Composer generates → You read to client
```

### Example
```
You type: Client said: "We're building a project management tool."

Composer: "Got it—so you're building a project management tool. 
Can you walk me through what problem it solves? And who are your target users?"

You read: [Read Composer's response to client]
```

### Quick Commands
```
# Ask specific question
Ask Q-BUS-005 (Product Definition)

# Apply scenario
Client mentioned budget is tight. Apply Scenario 1.

# Get summary
Summarize key decisions so far.
```

---

## 🔄 When to Reload Context

**Reload context when:**
- ✅ Starting new Composer session
- ✅ After updating artifacts
- ✅ Before important client calls
- ✅ If Composer seems to "forget" context

**How to Reload:**
```bash
# Generate new prompt
python3 .cursor/scripts/generate_composer_prompt.py

# Copy and paste to Composer
cat .cursor/cache/composer_prompt.txt
```

---

## 🆘 Troubleshooting

### Issue: Composer Doesn't Load Files
**Symptoms:** Composer says "I can't access that file"

**Fix:**
1. Check file paths are correct
2. Make sure you're in `/home/haymayndz/.nv/` directory
3. Use absolute paths if needed:
   ```
   Read `/home/haymayndz/.nv/.artifacts/protocol-02/question-bank.md`
   ```

### Issue: Composer Forgets Context Mid-Call
**Symptoms:** Composer stops referencing question IDs or scenarios

**Fix:**
1. Remind Composer:
   ```
   Reference question-bank.md. Use question IDs (Q-BUS-005, etc.)
   ```
2. Or reload context (paste prompt again)

### Issue: Responses Too Formal
**Symptoms:** Composer generates formal/robotic responses

**Fix:**
```
Your responses are too formal. Use ≥3 contractions ("I'm", "you're", "that's"), 
casual tone, and natural conversational flow. Regenerate last response.
```

---

## 💡 Pro Tips

1. **Load context at start of day** - Don't wait until call starts
2. **Keep prompt file handy** - Save `.cursor/cache/composer_prompt.txt` for quick access
3. **Test before live calls** - Run 1-2 test scenarios to verify context
4. **Use QUICK-REFERENCE-CARD.md** - Keep beside you during calls
5. **Reload if needed** - Don't hesitate to reload context mid-call

---

## 📊 Comparison: Preload vs Manual Loading

### Preload System (Original)
**Pros:**
- ✅ Automatic loading
- ✅ Loads all 42 files
- ✅ Consistent context

**Cons:**
- ❌ Doesn't work with Cursor Composer
- ❌ Only works with custom AI agents

### Manual Loading (This Method)
**Pros:**
- ✅ Works with Cursor Composer
- ✅ Fast (1-2 minutes)
- ✅ Flexible (load what you need)

**Cons:**
- ❌ Manual process (need to paste prompt)
- ❌ Need to reload each session
- ❌ Loads fewer files (15 vs 42)

---

## 🎯 Recommended Workflow

### Before Call (5 minutes)
1. Generate prompt: `python3 .cursor/scripts/generate_composer_prompt.py`
2. Copy prompt: `cat .cursor/cache/composer_prompt.txt`
3. Open Composer (Cmd+I)
4. Paste prompt
5. Wait for confirmation
6. Test with Scenario 1

### During Call (60 minutes)
1. Type client statements to Composer
2. Read Composer's responses to client
3. Update discovery-call-notes.md
4. Use QUICK-REFERENCE-CARD.md

### After Call (30 minutes)
1. Tell Composer: "Call ended. Generate post-call summary."
2. Review discovery-call-notes.md
3. Draft discovery-recap.md
4. Send to client

---

## 📁 Files Reference

**Context Loading:**
- `.cursor/scripts/generate_composer_prompt.py` - Prompt generator
- `.cursor/cache/composer_prompt.txt` - Generated prompt (copy this)
- `.cursor/commands/load-discovery-context.md` - @-mention command

**Quick Reference:**
- `QUICK-REFERENCE-CARD.md` - P0 questions, scenario triggers
- `USER-GUIDE-during-client-call.md` - Step-by-step guide
- `TROUBLESHOOTING-GUIDE.md` - Common issues

**Testing:**
- `TEST-SCENARIOS.md` - 8 test cases
- `PAANO-MAG-TEST.md` - Testing guide

---

## 🚀 Quick Reference Commands

**Generate Prompt:**
```bash
cd /home/haymayndz/.nv
python3 .cursor/scripts/generate_composer_prompt.py
```

**Copy Prompt:**
```bash
cat .cursor/cache/composer_prompt.txt | pbcopy  # Mac
cat .cursor/cache/composer_prompt.txt | xclip   # Linux
```

**View Prompt:**
```bash
cat .cursor/cache/composer_prompt.txt
```

**Test Composer:**
```
Client said: "We're building a SaaS for project management."
```

---

## ✅ Success Criteria

**Context is loaded when:**
- ✅ Composer confirms: "✅ Context loaded. Ready for discovery call!"
- ✅ Composer references question IDs (Q-BUS-005, etc.)
- ✅ Composer detects scenario triggers
- ✅ Responses have ≥3 contractions
- ✅ Natural conversational tone

**Call is successful when:**
- ✅ All P0 questions answered
- ✅ Composer responses human-voice compliant
- ✅ discovery-call-notes.md updated
- ✅ Client feels heard
- ✅ Clear next steps established

---

**You're ready!** 🎉

Generate the prompt, paste to Composer, and start your discovery call. Composer will have full Protocol 02 context!

**Good luck!** 🚀
