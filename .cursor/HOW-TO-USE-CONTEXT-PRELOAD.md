# How to Use Context Preload System

**Purpose:** Automatically load all Protocol 02 artifacts into AI memory before discovery calls  
**Location:** `/home/haymayndz/.nv/`

---

## 🎯 What This Does

Ang system na ito ay:
1. **Scans** lahat ng Protocol 02 files (rules, protocols, artifacts)
2. **Loads** them into `.cursor/cache/preload_context.json`
3. **Preloads** sa AI agent memory para instant access during calls

**Result:** AI may instant access sa lahat ng 42 files (313K+ characters) without manual loading!

---

## 📁 Files Created

### 1. Context Loader Script
**File:** `.cursor/scripts/load_context.py`  
**Purpose:** Scans and loads all Protocol 02 context files

**What it loads:**
- ✅ Master rules (4 files)
- ✅ AI-driven workflow protocols (3 files)
- ✅ Protocol 01 artifacts (9 files - upstream dependencies)
- ✅ Protocol 02 artifacts (25 files - discovery call)
- ✅ Resume.md (developer context)

**Total:** 42 files, 313,302 characters

### 2. Agent Configuration
**File:** `.cursor/agents/context-aware.json`  
**Purpose:** Configures AI agent to preload context

**Key Settings:**
- `preload`: Points to cache file
- `alwaysApply`: true (always use this context)
- `contextLoadMode`: "memory" (keep in memory)
- `contextRefresh`: "manual" (refresh when you run script)

### 3. Warm Start Command
**File:** `.cursor/commands/warm-start.json`  
**Purpose:** Quick command to reload context

**Shortcut:** Cmd+Shift+W (if supported)

### 4. Cache File (Generated)
**File:** `.cursor/cache/preload_context.json`  
**Purpose:** Stores all loaded context

**Structure:**
```json
{
  "metadata": {
    "total_files": 42,
    "total_size": 313302,
    "rules": 4,
    "protocols": 3,
    "artifacts": 34
  },
  "context": [
    {
      "path": "relative/path/to/file.md",
      "full_path": "/absolute/path/to/file.md",
      "content": "...",
      "size": 1234,
      "type": ".md"
    }
  ]
}
```

---

## 🚀 How to Use

### Before Discovery Call (One-Time Setup)

**Step 1: Run Context Loader**
```bash
cd /home/haymayndz/.nv
python3 .cursor/scripts/load_context.py
```

**Expected Output:**
```
🔄 Loading Protocol 02 Context Files...
📁 Base Directory: /home/haymayndz/.nv

📂 Scanning: .cursor/rules/**/*.md
  ✓ Loaded: .cursor/rules/english-speak.mdc (8632 chars)
  ✓ Loaded: .cursor/rules/master-rules/1-Live-Discovbery-Ghostwriter.mdc (5663 chars)
  ...

✅ Context Loading Complete!
   📊 Total Files: 42
   📏 Total Size: 313,302 characters
   📜 Rules: 4
   📋 Protocols: 3
   📦 Artifacts: 34
   💾 Cache File: /home/haymayndz/.nv/.cursor/cache/preload_context.json

🎯 Ready for Discovery Call!
```

**Step 2: Verify Cache File**
```bash
ls -lh /home/haymayndz/.nv/.cursor/cache/preload_context.json
```

Should show file size ~600KB-1MB

---

### During Discovery Call (Automatic)

**AI Agent Automatically:**
1. Loads `.cursor/cache/preload_context.json` on startup
2. Has instant access to all 42 Protocol 02 files
3. References question-bank.md, scenario-guides.md, discovery-brief.md automatically
4. No manual artifact loading needed!

**You Just:**
1. Type client statements to AI
2. AI generates responses (with full context)
3. Read AI responses to client

---

### When to Refresh Context

**Refresh context when:**
- ✅ You update Protocol 02 artifacts
- ✅ You add new test scenarios
- ✅ You modify question-bank.md or scenario-guides.md
- ✅ Before important client calls (to ensure latest context)

**How to Refresh:**
```bash
cd /home/haymayndz/.nv
python3 .cursor/scripts/load_context.py
```

Or use Cursor command (if configured):
```
Cmd+K → Warm Start Context
```

---

## 🔍 What Gets Loaded

### Master Rules (4 files)
- `english-speak.mdc` - English communication rules
- `1-Live-Discovbery-Ghostwriter.mdc` - Live ghostwriting protocol
- `common-rule-live-discovery-call-assistant.mdc` - Discovery call assistant
- `common-rule-live-interviews-discovery-context.mdc` - Interview context protocol

### AI-Driven Workflow Protocols (3 files)
- `01-client-proposal-generation.md` - Protocol 01 (upstream)
- `02-client-discovery-initiation.md` - Protocol 02 (main)
- `03-project-brief-creation.md` - Protocol 03 (downstream)

### Protocol 01 Artifacts (9 files - Upstream Dependencies)
**JSON Files:**
- `tone-map.json` - Client tone and language preferences
- `pricing-analysis.json` - Workload and pricing structure
- `jobpost-analysis.json` - Parsed job post
- `humanization-log.json` - Human voice strategy
- `proposal-summary.json` - Proposal highlights

**Markdown Files:**
- `PROPOSAL.md` - Accepted proposal content
- `job-post.md` - Original job post
- `notes.md` - Working notes
- `validation-report.md` - Proposal validation

### Protocol 02 Artifacts (25 files - Discovery Call)
**Pre-Call Intelligence:**
- `discovery-brief.md` - Business goals, users, metrics
- `question-bank.md` - 30+ prioritized questions
- `scenario-guides.md` - 6 scenario frameworks
- `assumptions-gaps.md` - Pending questions
- `integration-inventory.md` - Tech stack and systems
- `call-agenda.md` - Call structure
- `ready-for-call-summary.md` - Readiness confirmation

**Live Call Support:**
- `discovery-call-notes.md` - Real-time notes template
- `USER-GUIDE-during-client-call.md` - Step-by-step guide

**Post-Call Consolidation:**
- `client-discovery-form.md` - Confirmed requirements
- `scope-clarification.md` - Technical stack
- `timeline-discussion.md` - Milestones
- `communication-plan.md` - Collaboration expectations
- `discovery-recap.md` - Client-facing summary

**Test Framework:**
- `TEST-SCENARIOS.md` - 8 test cases
- `TEST-EXECUTION-LOG.md` - Results tracking
- `PAANO-MAG-TEST.md` - Testing guide
- `DEMO-TEST-RUN.md` - Demo results

**Reference Materials:**
- `QUICK-REFERENCE-CARD.md` - Live call cheat sheet
- `TROUBLESHOOTING-GUIDE.md` - Issue resolution
- `SYSTEM-ANALYSIS-SUMMARY.md` - Complete analysis

**Validation:**
- `discovery-approval-log.json` - Approval tracking
- `protocol-02-completion-review.md` - Completion checklist

### Developer Context (1 file)
- `resume.md` - Developer background and skills

---

## 📊 Context Statistics

**Total Context Loaded:**
- **Files:** 42
- **Size:** 313,302 characters (~313KB text)
- **Rules:** 4 files
- **Protocols:** 3 files
- **Artifacts:** 34 files
- **Cache Size:** ~600KB-1MB (with JSON structure)

**Breakdown by Type:**
- `.md` files: 33
- `.mdc` files: 4
- `.json` files: 5

**Breakdown by Category:**
- Master Rules: 4 files (45,747 chars)
- Protocols: 3 files (68,707 chars)
- Protocol 01 Artifacts: 9 files (14,078 chars)
- Protocol 02 Artifacts: 25 files (182,852 chars)
- Developer Context: 1 file (1,918 chars)

---

## ✅ Benefits

### Before Context Preload
**Manual Loading:**
```
You: "Load discovery-brief.md"
AI: [loads file]
You: "Load question-bank.md"
AI: [loads file]
You: "Load scenario-guides.md"
AI: [loads file]
... (repeat 42 times)
```
**Time:** 5-10 minutes of manual loading

### After Context Preload
**Automatic Loading:**
```
You: Run python script (once)
AI: [all 42 files loaded instantly]
You: Start discovery call
AI: [has full context, ready to go]
```
**Time:** 30 seconds (one-time setup)

### Key Benefits:
1. ✅ **Instant Access** - AI has all context immediately
2. ✅ **No Manual Loading** - No need to load files during call
3. ✅ **Consistent Context** - All files loaded every time
4. ✅ **Faster Responses** - AI doesn't need to search for files
5. ✅ **Better Quality** - AI references correct artifacts automatically

---

## 🔧 Troubleshooting

### Issue: Script Fails to Run
**Error:** `python3: command not found`

**Fix:**
```bash
# Try python instead
python .cursor/scripts/load_context.py

# Or install python3
sudo apt install python3  # Ubuntu/Debian
brew install python3      # macOS
```

### Issue: No Files Loaded
**Error:** `Total Files: 0`

**Fix:**
```bash
# Check if files exist
ls -la /home/haymayndz/.nv/.cursor/rules/
ls -la /home/haymayndz/.nv/.artifacts/protocol-02/

# If missing, files may be in different location
# Update paths in load_context.py
```

### Issue: Cache File Not Created
**Error:** `Cache file not found`

**Fix:**
```bash
# Create cache directory manually
mkdir -p /home/haymayndz/.nv/.cursor/cache

# Run script again
python3 .cursor/scripts/load_context.py
```

### Issue: AI Not Using Preloaded Context
**Error:** AI doesn't reference artifacts

**Fix:**
1. Check if `.cursor/agents/context-aware.json` exists
2. Verify `preload` field points to correct cache file
3. Restart AI agent/Cursor
4. Manually tell AI: "Load context from .cursor/cache/preload_context.json"

---

## 🎯 Quick Reference

**Load Context:**
```bash
cd /home/haymayndz/.nv
python3 .cursor/scripts/load_context.py
```

**Check Cache:**
```bash
ls -lh /home/haymayndz/.nv/.cursor/cache/preload_context.json
```

**View Stats:**
```bash
cat /home/haymayndz/.nv/.cursor/cache/preload_context.json | grep "total_files"
```

**Refresh Context:**
```bash
# After updating artifacts
cd /home/haymayndz/.nv
python3 .cursor/scripts/load_context.py
```

---

## 💡 Pro Tips

1. **Run before every important call** - Ensures latest context
2. **Check file count** - Should be 42 files (if less, something's missing)
3. **Verify cache size** - Should be ~600KB-1MB (if smaller, files may not be loaded)
4. **Update after changes** - Refresh context after modifying artifacts
5. **Keep cache in .gitignore** - Don't commit cache file to git

---

## 📝 Next Steps

1. ✅ **Test the system:**
   ```bash
   cd /home/haymayndz/.nv
   python3 .cursor/scripts/load_context.py
   ```

2. ✅ **Verify cache created:**
   ```bash
   ls -lh .cursor/cache/preload_context.json
   ```

3. ✅ **Start AI agent** with preloaded context

4. ✅ **Run test scenarios** from TEST-SCENARIOS.md

5. ✅ **Use during live calls** - AI has full context automatically!

---

**System is ready!** 🚀

Ang AI mo ngayon may instant access sa lahat ng 42 Protocol 02 files. No more manual loading during calls!
