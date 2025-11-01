# Agent Response Logic Enhancement - Implementation Plan

## Phase 1: Foundation (Weeks 1-2)

### Task 1.1: Dynamic Context Reload Mechanism

**Files to create:**

- `.cursor/scripts/watch_artifacts.py` - File watcher for artifact changes
- `.cursor/scripts/incremental_context_update.py` - Incremental cache updates
- `.cursor/rules/master-rules/7-master-rule-context-refresh.mdc` - Context refresh rule

**Dependencies:** None
**Key components:**

- File watcher using `watchdog` library
- Staleness detection logic comparing cache timestamps with artifact mtimes
- Incremental update function to refresh only changed files in cache

**Integration points:**

- Hook into `1-master-rule-context-discovery.mdc` Step 2
- Update `context-aware.json` with `autoRefresh: true` flag
- Modify `common-rule-live-discovery-call-assistant.mdc` to check freshness before responses

### Task 1.2: Hidden Rules Directory Structure

**Files to create:**

- `.cursor/rules/.hidden/.prompt-injections.mdc` - Silent prompt injections
- `.cursor/rules/.hidden/.behavior-overrides.mdc` - Behavior overrides
- `.cursor/rules/.hidden/.conversation-filters.mdc` - Conversation filters
- `.cursor/agents/.hidden-behaviors.json` - Hidden behavior configuration
- `.cursor/rules/master-rules/8-master-rule-hidden-injections.mdc` - Hidden rule loader

**Dependencies:** None
**Key components:**

- Hidden directory structure excluded from UI
- Frontmatter with `hidden: true` flag
- Silent prompt injection sections (pre-response, mid-response, post-response)
- Runtime prompt cache at `.cursor/cache/.injected-prompts.json`

**Security:**

- Add `.cursor/rules/.hidden/` to `.gitignore`
- Add `.cursor/agents/.hidden-behaviors.json` to `.gitignore`

### Task 1.3: Prompt Injection System

**Files to create:**

- `.cursor/scripts/inject_prompts.py` - Prompt injection loader

**Dependencies:** Task 1.2
**Key components:**

- `load_hidden_prompts()` function to parse hidden rules
- `inject_prompt()` function for runtime injection
- Cache generation for injected prompts
- Integration with agent configuration

**Integration points:**

- Update `context-aware.json` with `hiddenPrompts` and `silentInjections` config
- Hook into Context Discovery Protocol before rule loading

### Task 1.4: Response Validation Pipeline

**Files to create:**

- `.cursor/scripts/validate_response.py` - Response validation logic

**Dependencies:** None
**Key components:**

- `validate_response()` function checking contractions, warmth markers, sentence length
- `count_contractions()` and `count_warmth_markers()` helper functions
- `check_forbidden_phrases()` validation
- Scoring system for response quality

**Integration points:**

- Will be used in Phase 2 response generation pipeline
- Called before final response output

## Phase 2: Humanization (Weeks 3-4)

### Task 2.1: Tone Calibration System

**Files to create:**

- `.cursor/scripts/calibrate_tone.py` - Tone calibration logic

**Dependencies:** Phase 1
**Key components:**

- `calibrate_tone_for_response()` function loading tone-map.json
- `detect_client_tone()` function analyzing client input
- Tone instructions generation with register, frequencies, sentence limits

**Integration points:**

- Reads from `.artifacts/protocol-01/tone-map.json`
- Used in response generation pipeline Stage 1

### Task 2.2: Automatic Response Refinement

**Files to create:**

- `.cursor/scripts/refine_response.py` - Response refinement logic

**Dependencies:** Tasks 1.4, 2.1
**Key components:**

- `refine_response()` function applying fixes to draft
- `add_contractions()` replacing non-contractions
- `add_warmth_marker()` adding vocatives/tag questions
- `break_long_sentences()` splitting long sentences
- `remove_forbidden_phrases()` filtering forbidden patterns

**Integration points:**

- Called after validation if errors detected
- Uses tone_instructions from calibration

### Task 2.3: Unified Response Generation Rule

**Files to create:**

- `.cursor/rules/master-rules/9-master-rule-humanized-response-generation.mdc` - Unified pipeline rule

**Dependencies:** Tasks 2.1, 2.2, 1.4
**Key components:**

- 5-stage pipeline: Tone Calibration → Draft Generation → Validation → Refinement → Output
- Integration with FECS rules from `english-speak.mdc`
- Artifact referencing (resume, PROPOSAL, discovery-brief)
- Scenario pattern matching

**Integration points:**

- Replaces scattered response logic
- Integrates with Phase 1 prompt injections
- Uses Phase 3 gap detection (when available)

### Task 2.4: Humanization Testing

**Files to create:**

- `.cursor/scripts/test_humanization.py` - Test suite for humanization

**Dependencies:** All Phase 2 tasks
**Key components:**

- Unit tests for validation functions
- Integration tests for full pipeline
- Score calculation verification
- Forbidden phrase detection tests

## Phase 3: Adaptive Flow (Weeks 5-6)

### Task 3.1: Gap Detection System

**Files to create:**

- `.cursor/scripts/detect_gaps.py` - Gap detection logic

**Dependencies:** None
**Key components:**

- `detect_information_gaps()` analyzing conversation history
- `is_question_answered()` checking if question topics mentioned
- `prioritize_questions()` ordering by P0, critical gaps, dependencies
- Reads from `question-bank.md` and `assumptions-gaps.md`

**Integration points:**

- Used by GapTracker class
- Called after each client input

### Task 3.2: Real-Time Gap Tracking

**Files to create:**

- `.cursor/scripts/track_gaps.py` - GapTracker class

**Dependencies:** Task 3.1
**Key components:**

- `GapTracker` class maintaining conversation state
- `process_client_input()` updating answered questions
- `get_next_question()` prioritizing unanswered questions
- `get_gap_status()` returning completion metrics
- Updates assumptions-gaps.md mentally (not written, tracked)

**Integration points:**

- Used by ConversationStateMachine
- Integrated into response generation to inject questions

### Task 3.3: Scenario Detection System

**Files to create:**

- `.cursor/scripts/detect_scenario.py` - Scenario detection logic

**Dependencies:** None
**Key components:**

- `detect_scenario()` scoring client input against scenario triggers
- `get_response_pattern()` retrieving pattern for detected scenario
- Reads from `scenario-guides.md`
- Confidence threshold (≥3 for detection, ≥5 for high confidence)

**Integration points:**

- Used by ConversationStateMachine
- Influences response pattern selection

### Task 3.4: Conversation State Machine

**Files to create:**

- `.cursor/scripts/conversation_state.py` - ConversationStateMachine class

**Dependencies:** Tasks 3.2, 3.3
**Key components:**

- `ConversationStateMachine` managing phase transitions
- States: discovery_start, opening, deep_dive, wrapping_up
- `transition()` method updating state based on client input
- `_get_next_action()` determining next action (ask_question, apply_scenario_pattern, confirm_understanding)

**Integration points:**

- Used by adaptive question flow rule
- Informs response generation about conversation phase

### Task 3.5: Adaptive Question Flow Rule

**Files to create:**

- `.cursor/rules/master-rules/10-master-rule-adaptive-question-flow.mdc` - Adaptive flow rule

**Dependencies:** Tasks 3.1, 3.2, 3.4
**Key components:**

- Gap detection protocol after each client input
- Question injection logic with natural transitions
- FECS transformation for questions
- Example flow documentation

**Integration points:**

- Integrates with unified response generation rule
- Uses gap tracker and state machine

## Phase 4: Integration & Testing (Weeks 7-8)

### Task 4.1: Component Integration

**Files to modify:**

- `.cursor/agents/context-aware.json` - Add all new configuration flags
- `.cursor/rules/master-rules/1-master-rule-context-discovery.mdc` - Add refresh check
- `.cursor/common-rules/common-rule-live-discovery-call-assistant.mdc` - Integrate validation

**Dependencies:** All previous phases
**Key components:**

- Ensure all components work together
- Verify rule loading order
- Test context refresh integration
- Validate prompt injection flow

### Task 4.2: End-to-End Testing

**Files to create:**

- `.cursor/scripts/test_e2e.py` - End-to-end test suite

**Dependencies:** Task 4.1
**Key components:**

- Full conversation flow tests
- Response generation pipeline tests
- Context refresh tests
- Gap detection accuracy tests
- Scenario detection tests

### Task 4.3: Performance Optimization

**Files to modify:**

- All Phase 1-3 scripts - Add caching where needed

**Dependencies:** Task 4.2
**Key components:**

- Cache frequently accessed artifacts
- Optimize validation checks
- Lazy load less critical components
- Profile and optimize bottlenecks

### Task 4.4: Documentation Updates

**Files to create/modify:**

- `.cursor/docs/agent-enhancement-guide.md` - User guide
- Update existing rule documentation

**Dependencies:** All phases
**Key components:**

- Usage instructions for new features
- Configuration examples
- Troubleshooting guide
- API documentation for scripts

## Success Criteria

**Response Quality:**

- Humanization score ≥ 85%
- Forbidden phrase detection = 0%
- Sentence length compliance = 100%

**Context Management:**

- Refresh latency < 500ms
- Artifact freshness = 100%
- Cache hit rate ≥ 90%

**Adaptive Flow:**

- P0 questions asked in first 15 min = 100%
- Gap detection accuracy ≥ 90%
- Scenario detection confidence ≥ 70%

## Implementation Notes

1. **Backward Compatibility:** All changes maintain existing functionality
2. **Security:** Hidden files excluded from git, encrypted at rest
3. **Modularity:** Each component can be tested independently
4. **Error Handling:** Graceful degradation if components fail
5. **Performance:** Cache aggressively, lazy load where possible