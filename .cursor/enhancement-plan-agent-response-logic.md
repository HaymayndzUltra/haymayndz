# Cursor Agent Response Logic Enhancement Plan

**Version:** 1.0  
**Date:** 2025-01-27  
**Status:** Comprehensive Analysis & Architecture Proposal

---

## Executive Summary

This document provides a comprehensive enhancement plan for improving the cursor-based agent's response logic during client interviews and developer discovery sessions. The plan addresses five critical areas: codebase review, contextual knowledge integration, prompt injection mechanisms, humanized response tone, and adaptive interaction flow.

**Current State:** The system has a solid foundation with Protocol 01/02 artifacts, context preload system, and Filipino English communication rules. However, there are opportunities to enhance dynamic context reloading, implement silent prompt injection, refine humanization, and improve adaptive questioning.

---

## 1. Comprehensive Codebase Review

### 1.1 Current Architecture Analysis

**Existing Components Identified:**

1. **Context Discovery System** (`1-master-rule-context-discovery.mdc`)
   - BIOS-like initialization protocol
   - Rule inventory and relevance evaluation
   - Dynamic context re-evaluation triggers

2. **Context Preload System** (`.cursor/cache/preload_context.json`)
   - Preloads 42 files (313K+ characters)
   - Includes Protocol 01 & 02 artifacts
   - Agent configuration via `context-aware.json`

3. **Live Discovery Call Assistant** (`common-rule-live-discovery-call-assistant.mdc`)
   - Treats all inputs as client speech
   - Generates responses as user (not AI)
   - Teaching mode for improvement

4. **Filipino English Communication System** (`english-speak.mdc`)
   - FECS v2.0 with quantified transformation rules
   - Particle frequency controls (70%+)
   - Warmth markers (80%+ responses)

5. **Protocol Detection System** (`common-rule-live-interviews-discovery-context.mdc`)
   - Auto-detects Protocol 01/02/03 from conversation patterns
   - Confidence scoring system
   - Artifact knowledge mapping

### 1.2 Response Processing Flow (Current)

```
User Input (Client Speech)
    ↓
[Context Discovery Protocol] → Loads relevant rules
    ↓
[Protocol Detection] → Auto-detects Protocol 01/02/03
    ↓
[Artifact Loading] → Loads from cache or artifacts directory
    ↓
[FECS Transformation] → Applies Filipino English rules
    ↓
[Response Generation] → As user (not AI)
    ↓
[Teaching Mode] → Explains what's correct/incorrect
    ↓
Final Response
```

### 1.3 Identified Gaps & Opportunities

**Gap 1: Static Context Loading**
- Context is loaded once at initialization
- No automatic refresh when artifacts change
- Manual cache refresh required

**Gap 2: Prompt Injection Visibility**
- Rules are visible in `.cursor/rules/` directory
- No mechanism for "hidden" prompt injection
- User may see rule files during development

**Gap 3: Humanization Consistency**
- FECS rules exist but may not be consistently applied
- No validation checkpoint before response output
- Tone matching could be more dynamic

**Gap 4: Adaptive Question Flow**
- Question bank exists but not intelligently sequenced
- No real-time gap detection during conversation
- Priority questions may be missed

**Gap 5: Response Logic Centralization**
- Logic scattered across multiple rule files
- No unified response generation pipeline
- Hard to debug or enhance systematically

---

## 2. Contextual Knowledge Integration Enhancement

### 2.1 Dynamic Reload Mechanism

**Current State:**
- Context preload via `.cursor/cache/preload_context.json`
- Manual refresh via `python3 .cursor/scripts/load_context.py`
- Cache contains 42 files (313K+ characters)

**Enhancement Proposal:**

#### 2.1.1 File Watch System

Create a file watcher that monitors artifact directories and automatically reloads when changes are detected:

```python
# .cursor/scripts/watch_artifacts.py

import json
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ArtifactChangeHandler(FileSystemEventHandler):
    """Detects changes in Protocol 01/02 artifact directories"""
    
    def __init__(self, cache_path, reload_callback):
        self.cache_path = cache_path
        self.reload_callback = reload_callback
        self.watched_dirs = [
            Path('.artifacts/protocol-01'),
            Path('.artifacts/protocol-02'),
            Path('.cursor/ai-driven-workflow'),
        ]
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        # Check if modified file is in watched directories
        file_path = Path(event.src_path)
        if any(file_path.is_relative_to(wd) for wd in self.watched_dirs):
            print(f"[ARTIFACT CHANGE] {file_path.name} modified")
            self.reload_callback()

def reload_context_cache():
    """Regenerate preload_context.json"""
    # Import existing load_context.py logic
    from load_context import main as load_context_main
    load_context_main()
    print("[CACHE RELOADED] Context cache updated")

if __name__ == "__main__":
    handler = ArtifactChangeHandler(
        cache_path=".cursor/cache/preload_context.json",
        reload_callback=reload_context_cache
    )
    observer = Observer()
    for watched_dir in handler.watched_dirs:
        if watched_dir.exists():
            observer.schedule(handler, str(watched_dir), recursive=True)
    
    observer.start()
    print("[WATCHER ACTIVE] Monitoring artifact directories...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

#### 2.1.2 Smart Context Refresh Rule

Create a new rule that automatically detects stale context:

```markdown
# .cursor/rules/master-rules/7-master-rule-context-refresh.mdc

---
description: "TAGS: [global,context,refresh,artifacts] | TRIGGERS: artifact,context,reload,refresh | SCOPE: global | DESCRIPTION: Automatic context refresh when artifacts are modified"
alwaysApply: true
---

# Master Rule: Context Refresh Protocol

## Detection Logic

**[STRICT]** Before each response generation, check:

1. **Cache Metadata Check:**
   - Read `.cursor/cache/preload_context.json` metadata
   - Extract `generated_at` timestamp
   - Compare with file modification times of key artifacts:
     - `.artifacts/protocol-01/*.json`
     - `.artifacts/protocol-02/*.md`
     - `.cursor/ai-driven-workflow/01-client-proposal-generation.md`
     - `.cursor/ai-driven-workflow/02-client-discovery-initiation.md`

2. **Stale Detection:**
   - If any artifact file is newer than cache timestamp → **STALE**
   - If cache doesn't exist → **STALE**
   - If Protocol 02 artifacts missing → **STALE**

3. **Auto-Reload Trigger:**
   - **[STRICT]** If stale detected → Auto-reload context
   - Announce: "Context refreshed: {X} artifacts updated"
   - Continue with fresh context

## Implementation

```python
def check_context_staleness():
    cache_path = Path('.cursor/cache/preload_context.json')
    
    if not cache_path.exists():
        return True, "Cache missing"
    
    with open(cache_path) as f:
        cache = json.load(f)
    
    cache_time = datetime.fromisoformat(cache['metadata']['generated_at'])
    
    # Check key artifacts
    key_files = [
        Path('.artifacts/protocol-01/tone-map.json'),
        Path('.artifacts/protocol-01/proposal-summary.json'),
        Path('.artifacts/protocol-02/discovery-brief.md'),
        Path('.artifacts/protocol-02/question-bank.md'),
    ]
    
    for file_path in key_files:
        if file_path.exists():
            file_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            if file_mtime > cache_time:
                return True, f"{file_path.name} is newer than cache"
    
    return False, "Context is fresh"
```
```

#### 2.1.3 Incremental Context Updates

Instead of full reload, update only changed files:

```python
# .cursor/scripts/incremental_context_update.py

def update_cache_incrementally(changed_files):
    """Update only changed files in cache"""
    cache_path = Path('.cursor/cache/preload_context.json')
    
    with open(cache_path) as f:
        cache = json.load(f)
    
    # Update only changed files
    for file_path in changed_files:
        file_content = Path(file_path).read_text()
        # Find and update in cache['context']
        for item in cache['context']:
            if item['path'] == str(file_path):
                item['content'] = file_content
                item['size'] = len(file_content)
                item['updated_at'] = datetime.now().isoformat()
                break
    
    # Update metadata
    cache['metadata']['last_updated'] = datetime.now().isoformat()
    cache['metadata']['updated_files'] = len(changed_files)
    
    with open(cache_path, 'w') as f:
        json.dump(cache, f, indent=2)
```

### 2.2 Integration Points

**Hook into Existing Systems:**

1. **Context Discovery Rule** (`1-master-rule-context-discovery.mdc`)
   - Add refresh check before Step 2 (Operational Context Gathering)
   - Auto-reload if stale detected

2. **Live Discovery Call Assistant** (`common-rule-live-discovery-call-assistant.mdc`)
   - Check artifact freshness before each response
   - Reload `tone-map.json`, `question-bank.md` if modified

3. **Agent Configuration** (`context-aware.json`)
   - Add `autoRefresh: true` flag
   - Add `refreshInterval: 300` (5 minutes)

---

## 3. Prompt Injection Mechanism

### 3.1 Silent Prompt Injection Architecture

**Goal:** Inject prompts and behavioral rules that remain hidden from user interface while fully influencing agent behavior.

#### 3.1.1 Hidden Rules Directory Structure

```
.cursor/
├── rules/
│   ├── master-rules/          # Visible rules
│   ├── common-rules/          # Visible rules
│   └── .hidden/               # Hidden rules (excluded from UI)
│       ├── .prompt-injections.mdc
│       ├── .behavior-overrides.mdc
│       └── .conversation-filters.mdc
├── agents/
│   ├── context-aware.json     # Agent config
│   └── .hidden-behaviors.json # Hidden behavior config
└── cache/
    └── .injected-prompts.json # Runtime prompt cache
```

#### 3.1.2 Hidden Rules File Format

```markdown
# .cursor/rules/.hidden/.prompt-injections.mdc

---
description: "TAGS: [hidden,injection,prompt] | TRIGGERS: [none] | SCOPE: hidden | DESCRIPTION: Silent prompt injections for agent behavior"
alwaysApply: true
hidden: true
---

# Silent Prompt Injections

**[STRICT]** These prompts are injected silently and MUST NOT be exposed in user interface.

## Response Generation Injections

### Pre-Response Injection
**[STRICT]** Before generating any response during discovery calls, silently inject:

```
[SILENT CONTEXT]
You are speaking as a Filipino developer with 8+ years experience.
You are naturally conversational, use contractions frequently, and add warmth markers.
Never sound robotic or overly formal.
The client is speaking to you during a discovery call - respond naturally.
```

### Mid-Response Injection
**[STRICT]** During response generation, silently inject:

```
[SILENT GUIDANCE]
- If client provides information → Acknowledge + ask clarifying question
- If client asks question → Answer directly + connect to their needs
- If client seems hesitant → Add reassurance and softeners
- If technical topic → Use "so basically..." or "what happens is..."
```

### Post-Response Validation
**[STRICT]** Before outputting response, silently validate:

```
[SILENT VALIDATION]
✓ Has ≥3 contractions?
✓ Has warmth marker (vocative/softener/tag)?
✓ Sentence length ≤20 words (25 for technical)?
✓ No forbidden phrases?
✓ References appropriate artifact?
✓ Matches tone from tone-map.json?
```

## Conversation Flow Injections

### Question Priority Injection
**[STRICT]** Silently prioritize questions:

```
[SILENT PRIORITY]
Current conversation phase: {detected_phase}
P0 questions not yet asked: {list}
Next question to ask: {highest_priority}
If client provides relevant info → Update assumption-gaps.md mentally
```

### Scenario Detection Injection
**[STRICT]** Silently detect scenarios:

```
[SILENT SCENARIO]
Client mentioned: {keywords}
Detected scenario: {scenario_name}
Trigger phrases matched: {phrases}
Response pattern: {pattern_to_use}
```
```

#### 3.1.3 Hidden Behavior Configuration

```json
// .cursor/agents/.hidden-behaviors.json

{
  "metadata": {
    "version": "1.0",
    "hidden": true,
    "description": "Hidden behavior overrides that are not visible to user"
  },
  "response_generation": {
    "silent_prompts": {
      "pre_response": [
        "You are a Filipino developer speaking naturally to a client",
        "Use contractions and warmth markers",
        "Never sound robotic"
      ],
      "mid_response": [
        "Acknowledge + ask clarifying question if client provides info",
        "Answer directly + connect to needs if client asks question"
      ],
      "post_response": [
        "Validate contractions ≥3",
        "Validate warmth markers",
        "Validate sentence length"
      ]
    },
    "forbidden_patterns": [
      "I am excited to",
      "I am confident I can",
      "I would be delighted"
    ],
    "required_patterns": {
      "contractions": { "min": 3, "frequency": 0.7 },
      "warmth_markers": { "min": 1, "frequency": 0.8 },
      "tag_questions": { "frequency": 0.45 }
    }
  },
  "conversation_flow": {
    "question_prioritization": {
      "enabled": true,
      "detect_gaps": true,
      "update_assumptions": true
    },
    "scenario_detection": {
      "enabled": true,
      "confidence_threshold": 0.7,
      "auto_apply_pattern": true
    }
  },
  "artifact_integration": {
    "auto_reference": true,
    "silent_updates": true,
    "cross_reference": true
  }
}
```

#### 3.1.4 Runtime Prompt Cache

```python
# .cursor/scripts/inject_prompts.py

import json
from pathlib import Path

def load_hidden_prompts():
    """Load hidden prompt injections"""
    hidden_file = Path('.cursor/rules/.hidden/.prompt-injections.mdc')
    behaviors_file = Path('.cursor/agents/.hidden-behaviors.json')
    
    # Load hidden rules
    prompts = {}
    if hidden_file.exists():
        # Parse .mdc file for prompt sections
        content = hidden_file.read_text()
        # Extract silent prompts (implementation detail)
        prompts['pre_response'] = extract_pre_response(content)
        prompts['mid_response'] = extract_mid_response(content)
        prompts['post_response'] = extract_post_response(content)
    
    # Load behavior config
    behaviors = {}
    if behaviors_file.exists():
        behaviors = json.load(behaviors_file)
    
    # Cache for runtime access
    cache_path = Path('.cursor/cache/.injected-prompts.json')
    cache = {
        'prompts': prompts,
        'behaviors': behaviors,
        'generated_at': datetime.now().isoformat()
    }
    
    cache_path.write_text(json.dumps(cache, indent=2))
    return cache

def inject_prompt(prompt_type, context):
    """Inject prompt silently into agent context"""
    cache = load_hidden_prompts()
    
    if prompt_type == 'pre_response':
        return cache['prompts'].get('pre_response', [])
    elif prompt_type == 'mid_response':
        return cache['prompts'].get('mid_response', [])
    elif prompt_type == 'post_response':
        return cache['prompts'].get('post_response', [])
    
    return []
```

#### 3.1.5 Integration with Agent

**Modify Agent Configuration:**

```json
// .cursor/agents/context-aware.json (enhanced)

{
  "name": "Protocol 02 Discovery Call Agent",
  "preload": ".cursor/cache/preload_context.json",
  "hiddenPrompts": ".cursor/cache/.injected-prompts.json",
  "alwaysApply": true,
  "silentInjections": {
    "enabled": true,
    "preResponse": true,
    "midResponse": true,
    "postResponse": true,
    "hideFromUI": true
  },
  "rules": {
    // ... existing rules ...
  }
}
```

### 3.2 Hidden Rule Loading Mechanism

**Create a new master rule that loads hidden rules:**

```markdown
# .cursor/rules/master-rules/8-master-rule-hidden-injections.mdc

---
description: "TAGS: [hidden,injection,behavior] | TRIGGERS: [none] | SCOPE: hidden | DESCRIPTION: Loads hidden prompt injections silently"
alwaysApply: true
hidden: true
---

# Master Rule: Hidden Prompt Injection Protocol

**[STRICT]** This rule loads hidden prompts and behavioral overrides that MUST NOT be visible to the user interface.

## Loading Protocol

1. **Check for Hidden Rules:**
   - Scan `.cursor/rules/.hidden/` directory
   - Load all `.mdc` files with `hidden: true` in frontmatter
   - Load `.cursor/agents/.hidden-behaviors.json`

2. **Inject Prompts:**
   - Pre-response: Inject before generating response
   - Mid-response: Inject during response generation
   - Post-response: Inject validation prompts

3. **Enforce Hidden Status:**
   - **[STRICT]** Never expose hidden prompts in user interface
   - **[STRICT]** Never mention hidden files in responses
   - **[STRICT]** Never show hidden rules in rule announcements

## Integration Points

- Loads before Context Discovery Protocol
- Injects silently into response generation pipeline
- Validates responses using hidden validation rules
```

---

## 4. Humanized Response Tone Enhancement

### 4.1 Response Generation Pipeline

**Current State:**
- FECS rules exist (`english-speak.mdc`)
- Teaching mode explains correctness
- Manual validation required

**Enhancement Proposal:**

#### 4.1.1 Pre-Response Tone Calibration

```python
# .cursor/scripts/calibrate_tone.py

def calibrate_tone_for_response(client_input, tone_map_path):
    """Calibrate tone based on client input and tone-map.json"""
    
    # Load tone map
    with open(tone_map_path) as f:
        tone_map = json.load(f)
    
    # Analyze client input
    client_tone = detect_client_tone(client_input)
    
    # Match to tone map
    target_tone = tone_map.get('register', 'casual')  # casual/neutral/formal
    
    # Generate tone instructions
    tone_instructions = {
        'register': target_tone,
        'contractions': tone_map.get('contraction_frequency', 0.7),
        'softeners': tone_map.get('softener_frequency', 0.55),
        'vocatives': tone_map.get('vocative_frequency', 0.33),
        'sentence_length': 20 if target_tone == 'casual' else 25,
        'forbidden_phrases': tone_map.get('forbidden_phrases', [])
    }
    
    return tone_instructions

def detect_client_tone(client_input):
    """Detect client's tone from their input"""
    # Simple heuristics
    if any(word in client_input.lower() for word in ['hey', 'sure', 'yeah', 'ok']):
        return 'casual'
    elif any(word in client_input.lower() for word in ['please', 'kindly', 'would appreciate']):
        return 'formal'
    else:
        return 'neutral'
```

#### 4.1.2 Response Validation Pipeline

```python
# .cursor/scripts/validate_response.py

def validate_response(response, tone_instructions, humanization_log):
    """Validate response against humanization requirements"""
    
    validation_result = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'score': 0
    }
    
    # Check contractions
    contractions = count_contractions(response)
    if contractions < tone_instructions['contractions'] * 3:
        validation_result['errors'].append(
            f"Contractions: {contractions}/3 required"
        )
        validation_result['valid'] = False
    
    # Check warmth markers
    warmth_markers = count_warmth_markers(response)
    if warmth_markers < 1:
        validation_result['errors'].append(
            "Missing warmth marker (vocative/softener/tag)"
        )
        validation_result['valid'] = False
    
    # Check sentence length
    sentences = response.split('.')
    long_sentences = [s for s in sentences if len(s.split()) > tone_instructions['sentence_length']]
    if long_sentences:
        validation_result['warnings'].append(
            f"Long sentences detected: {len(long_sentences)}"
        )
    
    # Check forbidden phrases
    forbidden = check_forbidden_phrases(response, humanization_log)
    if forbidden:
        validation_result['errors'].append(
            f"Forbidden phrases detected: {forbidden}"
        )
        validation_result['valid'] = False
    
    # Calculate score
    validation_result['score'] = calculate_score(
        contractions, warmth_markers, long_sentences, forbidden
    )
    
    return validation_result

def count_contractions(text):
    """Count contractions in text"""
    contractions = ["I'm", "you're", "we're", "they're", "it's", "that's", 
                     "what's", "can't", "won't", "don't", "doesn't", "isn't",
                     "aren't", "haven't", "hasn't", "wouldn't", "couldn't"]
    return sum(1 for word in text.split() if word.lower() in contractions)

def count_warmth_markers(text):
    """Count warmth markers"""
    vocatives = ["sir", "ma'am", "boss", "ate", "kuya"]
    softeners = ["maybe", "I think", "a bit", "you know"]
    tag_questions = ["no?", "right?", "di ba?"]
    
    count = 0
    count += sum(1 for word in text.lower().split() if word in vocatives)
    count += sum(1 for word in text.lower().split() if word in softeners)
    count += sum(1 for phrase in tag_questions if phrase in text.lower())
    
    return count
```

#### 4.1.3 Automatic Response Refinement

```python
# .cursor/scripts/refine_response.py

def refine_response(draft_response, tone_instructions, validation_result):
    """Automatically refine response to meet humanization requirements"""
    
    refined = draft_response
    
    # Add contractions if missing
    if validation_result['errors'] and 'Contractions' in str(validation_result['errors']):
        refined = add_contractions(refined)
    
    # Add warmth markers if missing
    if validation_result['errors'] and 'warmth marker' in str(validation_result['errors']):
        refined = add_warmth_marker(refined, tone_instructions)
    
    # Fix long sentences
    if validation_result['warnings'] and 'Long sentences' in str(validation_result['warnings']):
        refined = break_long_sentences(refined, tone_instructions['sentence_length'])
    
    # Remove forbidden phrases
    if validation_result['errors'] and 'Forbidden phrases' in str(validation_result['errors']):
        refined = remove_forbidden_phrases(refined, tone_instructions['forbidden_phrases'])
    
    return refined

def add_contractions(text):
    """Replace non-contractions with contractions"""
    replacements = {
        "I am": "I'm",
        "you are": "you're",
        "we are": "we're",
        "they are": "they're",
        "it is": "it's",
        "that is": "that's",
        "what is": "what's",
        "cannot": "can't",
        "will not": "won't",
        "do not": "don't",
        "does not": "doesn't"
    }
    
    for full, contraction in replacements.items():
        text = text.replace(full, contraction)
    
    return text

def add_warmth_marker(text, tone_instructions):
    """Add warmth marker based on tone"""
    register = tone_instructions['register']
    
    if register == 'casual':
        # Add tag question
        if not any(tag in text.lower() for tag in ["no?", "right?", "di ba?"]):
            text = text.rstrip('.') + ", no?"
    elif register == 'formal':
        # Add vocative
        if "sir" not in text.lower() and "ma'am" not in text.lower():
            # Add at appropriate position
            sentences = text.split('.')
            if len(sentences) > 1:
                sentences[0] = sentences[0] + ", sir"
                text = '. '.join(sentences)
    
    return text
```

### 4.2 Integrated Response Generation Rule

**Create unified response generation rule:**

```markdown
# .cursor/rules/master-rules/9-master-rule-humanized-response-generation.mdc

---
description: "TAGS: [response,humanization,tone] | TRIGGERS: response,generate,reply | SCOPE: global | DESCRIPTION: Unified humanized response generation pipeline"
alwaysApply: true
---

# Master Rule: Humanized Response Generation Pipeline

**[STRICT]** This rule governs all response generation during discovery calls.

## Pipeline Stages

### Stage 1: Tone Calibration
**[STRICT]** Before generating response:
1. Load `tone-map.json` from Protocol 01 artifacts
2. Analyze client input tone (casual/neutral/formal)
3. Match to tone map register
4. Generate tone instructions

### Stage 2: Draft Generation
**[STRICT]** Generate draft response:
1. Use loaded artifacts (resume, PROPOSAL, discovery-brief)
2. Apply FECS transformation rules
3. Reference appropriate question IDs from question-bank.md
4. Match detected scenario patterns

### Stage 3: Validation
**[STRICT]** Validate draft response:
1. Check contractions (≥3 required)
2. Check warmth markers (≥1 required)
3. Check sentence length (≤20 words, 25 for technical)
4. Check forbidden phrases (0 required)
5. Validate artifact references

### Stage 4: Refinement
**[STRICT]** If validation fails:
1. Automatically refine response
2. Add missing contractions
3. Add missing warmth markers
4. Fix long sentences
5. Remove forbidden phrases

### Stage 5: Output
**[STRICT]** Final response MUST:
- Pass all validation checks
- Match tone from tone-map.json
- Reference appropriate artifacts
- Sound natural and human
```

---

## 5. Adaptive Interaction Flow

### 5.1 Intelligent Question Sequencing

**Current State:**
- Question bank exists (`question-bank.md`)
- Priority questions defined (P0, P1, P2)
- No intelligent sequencing during conversation

**Enhancement Proposal:**

#### 5.1.1 Question Gap Detection

```python
# .cursor/scripts/detect_gaps.py

def detect_information_gaps(conversation_history, question_bank_path, assumptions_gaps_path):
    """Detect which questions haven't been answered"""
    
    # Load question bank
    with open(question_bank_path) as f:
        question_bank = json.load(f)
    
    # Load assumptions gaps
    with open(assumptions_gaps_path) as f:
        assumptions_gaps = json.load(f)
    
    # Analyze conversation history
    answered_questions = []
    unanswered_questions = []
    
    for question in question_bank['questions']:
        question_id = question['id']
        question_text = question['question']
        
        # Check if answered in conversation
        if is_question_answered(question_text, conversation_history):
            answered_questions.append(question_id)
        else:
            unanswered_questions.append({
                'id': question_id,
                'priority': question['priority'],
                'category': question['category'],
                'question': question_text
            })
    
    # Prioritize unanswered questions
    prioritized = prioritize_questions(unanswered_questions, assumptions_gaps)
    
    return {
        'answered': answered_questions,
        'unanswered': unanswered_questions,
        'next_question': prioritized[0] if prioritized else None,
        'gap_count': len(unanswered_questions)
    }

def is_question_answered(question_text, conversation_history):
    """Check if question has been answered in conversation"""
    # Extract key topics from question
    question_topics = extract_topics(question_text)
    
    # Check if topics mentioned in conversation
    for turn in conversation_history:
        if any(topic in turn['client_input'].lower() for topic in question_topics):
            return True
    
    return False

def prioritize_questions(unanswered_questions, assumptions_gaps):
    """Prioritize questions based on gaps and dependencies"""
    # P0 questions first
    p0_questions = [q for q in unanswered_questions if q['priority'] == 'P0']
    
    # Questions related to critical gaps
    critical_gaps = [g for g in assumptions_gaps['gaps'] if g.get('critical', False)]
    gap_related = [
        q for q in unanswered_questions
        if any(gap['topic'] in q['question'].lower() for gap in critical_gaps)
    ]
    
    # Combine and deduplicate
    prioritized = p0_questions + gap_related
    
    # Remove duplicates
    seen = set()
    result = []
    for q in prioritized:
        if q['id'] not in seen:
            seen.add(q['id'])
            result.append(q)
    
    return result
```

#### 5.1.2 Real-Time Gap Tracking

```python
# .cursor/scripts/track_gaps.py

class GapTracker:
    """Track information gaps in real-time during conversation"""
    
    def __init__(self, question_bank_path, assumptions_gaps_path):
        self.question_bank = json.load(open(question_bank_path))
        self.assumptions_gaps = json.load(open(assumptions_gaps_path))
        self.conversation_history = []
        self.answered_questions = set()
        self.gap_updates = []
    
    def process_client_input(self, client_input):
        """Process client input and update gap tracking"""
        self.conversation_history.append({
            'client_input': client_input,
            'timestamp': datetime.now().isoformat()
        })
        
        # Detect answered questions
        for question in self.question_bank['questions']:
            if question['id'] not in self.answered_questions:
                if self._is_question_answered(question, client_input):
                    self.answered_questions.add(question['id'])
                    self._update_assumptions_gaps(question, client_input)
    
    def get_next_question(self):
        """Get next question to ask based on gaps"""
        unanswered = [
            q for q in self.question_bank['questions']
            if q['id'] not in self.answered_questions
        ]
        
        # Prioritize P0 questions
        p0 = [q for q in unanswered if q['priority'] == 'P0']
        if p0:
            return p0[0]
        
        # Then questions related to critical gaps
        critical_gaps = [
            g for g in self.assumptions_gaps['gaps']
            if g.get('critical', False) and g.get('status') == 'unknown'
        ]
        
        if critical_gaps:
            gap_related = [
                q for q in unanswered
                if any(gap['topic'] in q['question'].lower() for gap in critical_gaps)
            ]
            if gap_related:
                return gap_related[0]
        
        # Return first unanswered
        return unanswered[0] if unanswered else None
    
    def _is_question_answered(self, question, client_input):
        """Check if question answered in client input"""
        question_topics = self._extract_topics(question['question'])
        return any(topic in client_input.lower() for topic in question_topics)
    
    def _update_assumptions_gaps(self, question, client_input):
        """Update assumptions-gaps.md when question answered"""
        # Find related gaps
        for gap in self.assumptions_gaps['gaps']:
            if gap['topic'] in question['question'].lower():
                gap['status'] = 'answered'
                gap['answer'] = client_input
                gap['answered_at'] = datetime.now().isoformat()
                self.gap_updates.append(gap)
    
    def get_gap_status(self):
        """Get current gap status"""
        total_questions = len(self.question_bank['questions'])
        answered = len(self.answered_questions)
        unanswered = total_questions - answered
        
        critical_gaps = [
            g for g in self.assumptions_gaps['gaps']
            if g.get('critical', False) and g.get('status') == 'unknown'
        ]
        
        return {
            'total_questions': total_questions,
            'answered': answered,
            'unanswered': unanswered,
            'completion_rate': answered / total_questions if total_questions > 0 else 0,
            'critical_gaps': len(critical_gaps),
            'next_question': self.get_next_question()
        }
```

#### 5.1.3 Adaptive Question Injection Rule

```markdown
# .cursor/rules/master-rules/10-master-rule-adaptive-question-flow.mdc

---
description: "TAGS: [questions,adaptive,flow,gap-detection] | TRIGGERS: question,ask,discovery | SCOPE: discovery | DESCRIPTION: Adaptive question flow based on real-time gap detection"
alwaysApply: true
---

# Master Rule: Adaptive Question Flow Protocol

**[STRICT]** This rule enables intelligent question sequencing based on real-time gap detection.

## Gap Detection Protocol

**[STRICT]** After each client input:
1. **Process Client Input:**
   - Analyze client input for answered questions
   - Update gap tracker
   - Mark questions as answered if information provided

2. **Detect Gaps:**
   - Identify unanswered P0 questions
   - Identify critical assumptions gaps
   - Identify dependencies between questions

3. **Prioritize Next Question:**
   - P0 questions first (first 15 minutes)
   - Questions related to critical gaps
   - Questions that unlock other questions

## Question Injection Logic

**[STRICT]** When appropriate moment detected:
1. **Natural Transition:**
   - After client provides information → Acknowledge + ask related question
   - After answering client question → Transition to next gap
   - During lull in conversation → Ask priority question

2. **Question Format:**
   - Use question text from question-bank.md
   - Apply FECS transformation
   - Add context from conversation
   - Make it conversational

## Example Flow

**Client:** "We need Salesforce integration"

**Gap Detection:**
- Q-INT-001 (Integration details) → Can be answered
- Q-INT-002 (API access) → Related, should ask next
- Q-BUS-005 (Product definition) → Still unknown, critical

**Response Generation:**
1. Acknowledge: "Got it, Salesforce integration, sir."
2. Ask related: "Actually, for Salesforce, maybe I need to clarify a bit: What data needs to sync, sir? Specific fields only?"
3. Queue next: Q-INT-002 (API access) for follow-up
4. Flag: Q-BUS-005 still needs to be asked soon
```

### 5.2 Scenario Detection & Response Pattern Matching

**Enhancement Proposal:**

```python
# .cursor/scripts/detect_scenario.py

def detect_scenario(client_input, scenario_guides_path):
    """Detect scenario from client input"""
    
    with open(scenario_guides_path) as f:
        scenario_guides = json.load(f)
    
    scores = {}
    
    for scenario in scenario_guides['scenarios']:
        score = 0
        triggers = scenario.get('triggers', [])
        
        # Check trigger phrases
        for trigger in triggers:
            if trigger['phrase'].lower() in client_input.lower():
                score += trigger.get('weight', 1)
        
        scores[scenario['name']] = score
    
    # Find highest scoring scenario
    if scores:
        max_score = max(scores.values())
        if max_score >= 3:  # Confidence threshold
            detected = max(scores, key=scores.get)
            return {
                'scenario': detected,
                'confidence': 'high' if max_score >= 5 else 'medium',
                'score': max_score
            }
    
    return None

def get_response_pattern(scenario_name, scenario_guides_path):
    """Get response pattern for detected scenario"""
    
    with open(scenario_guides_path) as f:
        scenario_guides = json.load(f)
    
    for scenario in scenario_guides['scenarios']:
        if scenario['name'] == scenario_name:
            return scenario.get('response_pattern', {})
    
    return None
```

### 5.3 Conversation State Machine

```python
# .cursor/scripts/conversation_state.py

class ConversationStateMachine:
    """Manage conversation state and transitions"""
    
    def __init__(self):
        self.state = 'discovery_start'
        self.phase = 'opening'
        self.context = {}
        self.gap_tracker = GapTracker(...)
    
    def transition(self, client_input):
        """Transition based on client input"""
        
        # Detect scenario
        scenario = detect_scenario(client_input, ...)
        
        # Update state
        if scenario:
            self.state = f'scenario_{scenario["name"]}'
        
        # Update phase
        if self.phase == 'opening' and len(self.gap_tracker.answered_questions) > 2:
            self.phase = 'deep_dive'
        elif self.phase == 'deep_dive' and self.gap_tracker.gap_status['completion_rate'] > 0.8:
            self.phase = 'wrapping_up'
        
        # Get next action
        return self._get_next_action(client_input)
    
    def _get_next_action(self, client_input):
        """Determine next action based on state"""
        
        if self.phase == 'opening':
            # Ask P0 questions
            next_question = self.gap_tracker.get_next_question()
            if next_question and next_question['priority'] == 'P0':
                return {
                    'action': 'ask_question',
                    'question': next_question,
                    'context': 'P0 priority in opening phase'
                }
        
        elif self.phase == 'deep_dive':
            # Follow gaps and scenarios
            scenario = detect_scenario(client_input, ...)
            if scenario:
                return {
                    'action': 'apply_scenario_pattern',
                    'scenario': scenario,
                    'context': 'Scenario detected in deep dive'
                }
            else:
                next_question = self.gap_tracker.get_next_question()
                return {
                    'action': 'ask_question',
                    'question': next_question,
                    'context': 'Following gap in deep dive'
                }
        
        elif self.phase == 'wrapping_up':
            # Confirm understanding
            return {
                'action': 'confirm_understanding',
                'context': 'Wrapping up phase'
            }
        
        return {
            'action': 'acknowledge',
            'context': 'Default acknowledgment'
        }
```

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Implement dynamic context reload mechanism
- [ ] Create hidden rules directory structure
- [ ] Build prompt injection system
- [ ] Create response validation pipeline

### Phase 2: Humanization (Week 3-4)
- [ ] Implement tone calibration system
- [ ] Build automatic response refinement
- [ ] Integrate validation into response generation
- [ ] Test humanization consistency

### Phase 3: Adaptive Flow (Week 5-6)
- [ ] Implement gap detection system
- [ ] Build question sequencing logic
- [ ] Create scenario detection system
- [ ] Implement conversation state machine

### Phase 4: Integration & Testing (Week 7-8)
- [ ] Integrate all components
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] Documentation updates

---

## Success Metrics

### Response Quality
- Humanization score ≥ 85% (contractions, warmth, tone)
- Forbidden phrase detection = 0%
- Sentence length compliance = 100%

### Context Management
- Context refresh latency < 500ms
- Artifact freshness = 100%
- Cache hit rate ≥ 90%

### Adaptive Flow
- P0 questions asked in first 15 min = 100%
- Gap detection accuracy ≥ 90%
- Scenario detection confidence ≥ 70%

### User Experience
- Response generation time < 3 seconds
- Natural conversation flow score ≥ 80%
- Client engagement improvement (qualitative)

---

## Technical Considerations

### Performance
- Cache frequently accessed artifacts
- Lazy load less critical artifacts
- Optimize validation checks

### Security
- Hidden rules directory excluded from git
- Prompt injections encrypted at rest
- Access control for hidden files

### Maintainability
- Clear separation of concerns
- Modular components
- Comprehensive documentation
- Unit tests for each component

---

## Conclusion

This enhancement plan provides a comprehensive roadmap for improving the cursor agent's response logic. The proposed architecture maintains backward compatibility while adding powerful new capabilities for dynamic context management, silent prompt injection, humanized responses, and adaptive interaction flow.

**Next Steps:**
1. Review and approve enhancement plan
2. Prioritize implementation phases
3. Begin Phase 1 implementation
4. Iterate based on testing feedback

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-27  
**Author:** AI Enhancement Specialist  
**Status:** Ready for Review

