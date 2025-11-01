# Plan Review Prompt: Gap Analysis & Correction

**Purpose:** Review enhancement plan against actual codebase, flag gaps logically, and correct only what's wrong.

**Target Document:** `plan.md`

---

## Review Protocol

**[STRICT]** You are a **Plan Auditor** specialized in identifying gaps between plans and actual codebase implementation. Your mission is to:

1. **Analyze** the enhancement plan thoroughly
2. **Cross-reference** with actual codebase structure
3. **Flag gaps** logically and with common sense
4. **Correct** only what's actually wrong
5. **Preserve** what's correct without modification

---

## Step 1: Codebase Structure Verification

**[STRICT]** Verify these key structures exist in codebase:

### Artifact Locations
- [ ] `.artifacts/protocol-01/` directory exists
- [ ] `.artifacts/protocol-02/` directory exists
- [ ] Verify actual artifact files match plan references
- [ ] Check artifact file names (exact match required)

### Script Locations
- [ ] `.cursor/scripts/` directory exists
- [ ] Verify script files mentioned in plan exist
- [ ] Check script file names match plan
- [ ] Verify script functionality matches plan description

### Rule Locations
- [ ] `.cursor/rules/` directory structure matches plan
- [ ] `.cursor/common-rules/` directory exists
- [ ] `.cursorrules` file exists at root
- [ ] Verify rule file names match plan references

### Cache System
- [ ] `.cursor/cache/` directory exists
- [ ] `preload_context.json` structure matches plan
- [ ] Verify `load_context.py` script exists and works as described

---

## Step 2: Gap Detection Rules

### Rule 1: File Path Verification
**[STRICT]** For every file path mentioned in plan:
- Check if path actually exists in codebase
- Verify path structure matches actual directory structure
- Flag if path is incorrect or non-existent
- Flag if path uses wrong directory names

### Rule 2: Artifact Name Verification
**[STRICT]** For every artifact name mentioned:
- Check if artifact file actually exists
- Verify exact file name (case-sensitive)
- Flag if name is wrong (e.g., `client-context-notes.md` vs `discovery-call-notes.md`)
- Flag if extension is wrong (`.md` vs `.json`)

### Rule 3: Script Functionality Verification
**[STRICT]** For every script mentioned:
- Check if script exists
- Verify script actually does what plan says
- Flag if script functionality is incorrect
- Flag if script imports/dependencies are wrong

### Rule 4: Integration Point Verification
**[STRICT]** For every integration point mentioned:
- Verify integration actually exists in codebase
- Check if integration works as described
- Flag if integration point is incorrect
- Flag if integration dependencies are missing

### Rule 5: Data Structure Verification
**[STRICT]** For every data structure mentioned:
- Verify structure matches actual implementation
- Check JSON schema matches plan
- Flag if fields are missing or wrong
- Flag if data types are incorrect

---

## Step 3: Logical Gap Detection

### Common Sense Checks

#### Check 1: Directory Structure Consistency
- [ ] Plan mentions directories that don't exist
- [ ] Plan uses wrong directory names
- [ ] Plan references nested directories incorrectly
- [ ] Directory paths don't match actual structure

#### Check 2: File Naming Consistency
- [ ] Plan uses wrong file names
- [ ] Plan references files that don't exist
- [ ] File extensions don't match
- [ ] File names don't follow actual naming conventions

#### Check 3: Script Implementation Consistency
- [ ] Scripts mentioned don't exist
- [ ] Script functionality doesn't match plan
- [ ] Script imports/dependencies are wrong
- [ ] Script CLI arguments don't match plan

#### Check 4: Integration Consistency
- [ ] Integration points don't exist
- [ ] Integration flow doesn't match plan
- [ ] Dependencies between components are wrong
- [ ] Data flow doesn't match actual implementation

#### Check 5: Artifact Structure Consistency
- [ ] Artifact structure doesn't match plan
- [ ] Artifact fields are missing or wrong
- [ ] Artifact relationships are incorrect
- [ ] Artifact update flow doesn't match plan

---

## Step 4: Correction Protocol

**[STRICT]** When flagging issues, follow this format:

### Issue Format
```markdown
## Issue #N: [Issue Type] - [Brief Description]

**Location in Plan:** [Section, Subsection, Line Reference]

**What Plan Says:**
- [Exact quote from plan]

**What Codebase Actually Has:**
- [Actual codebase structure/reference]

**Impact:** [HIGH/MEDIUM/LOW]
- [Reason for impact level]

**Correction Needed:**
- [Specific correction required]
```

### Correction Rules

**[STRICT]** Only correct if:
1. ✅ File path is wrong
2. ✅ File name is wrong
3. ✅ Directory structure is wrong
4. ✅ Script functionality is incorrect
5. ✅ Integration point is wrong
6. ✅ Data structure is incorrect
7. ✅ Logic flow is wrong

**[STRICT]** DO NOT correct if:
1. ❌ Plan is correct but could be improved (enhancement suggestions only)
2. ❌ Plan is correct but implementation is missing (that's OK, plan is for future)
3. ❌ Plan is correct but uses different approach (both valid)
4. ❌ Plan is correct but terminology differs slightly (style difference)

---

## Step 5: Review Checklist

### File References
- [ ] All file paths exist in codebase
- [ ] All file names match exactly
- [ ] All directory structures match
- [ ] All extensions are correct

### Script References
- [ ] All scripts exist
- [ ] Script functionality matches plan
- [ ] Script imports are correct
- [ ] Script CLI arguments match

### Integration Points
- [ ] All integration points exist
- [ ] Integration flow matches plan
- [ ] Dependencies are correct
- [ ] Data flow matches implementation

### Artifact References
- [ ] All artifacts exist
- [ ] Artifact structure matches plan
- [ ] Artifact fields are correct
- [ ] Artifact relationships are correct

### Logic Flow
- [ ] Flow matches actual implementation
- [ ] Dependencies are correct
- [ ] Sequence is logical
- [ ] Edge cases are handled

---

## Step 6: Gap Report Format

**[STRICT]** Generate gap report in this format:

```markdown
# Gap Analysis Report: Enhancement Plan Review

**Date:** [Date]
**Plan Reviewed:** `.cursor/ENHANCEMENT-PLAN-agent-response-logic.md`
**Codebase:** `/home/haymayndz/.nv/`

---

## Summary

- **Total Issues Found:** [N]
- **Critical Issues:** [N]
- **High Priority Issues:** [N]
- **Medium Priority Issues:** [N]
- **Low Priority Issues:** [N]

---

## Issues Found

### Issue #1: [Title]
[Issue details following format above]

### Issue #2: [Title]
[Issue details following format above]

---

## Corrections Applied

### Correction #1: [Title]
**Changed:** [What was changed]
**From:** [Original]
**To:** [Corrected]

---

## Verified Correct

### Section 1: [Title]
- ✅ [What was verified correct]

### Section 2: [Title]
- ✅ [What was verified correct]

---

## Recommendations (Optional Enhancements)

### Enhancement #1: [Title]
**Note:** This is correct but could be improved...
**Suggestion:** [Enhancement suggestion]

---

## Status

- [ ] All critical issues corrected
- [ ] All high priority issues corrected
- [ ] Plan verified against codebase
- [ ] Corrections applied to plan document
```

---

## Step 7: Execution Protocol

**[STRICT]** Execute review in this order:

1. **Read Enhancement Plan**
   - Load `.cursor/ENHANCEMENT-PLAN-agent-response-logic.md`
   - Understand all sections and components

2. **Scan Codebase**
   - Verify all file paths mentioned
   - Verify all directory structures
   - Verify all scripts mentioned
   - Verify all artifacts mentioned

3. **Compare & Flag**
   - Compare plan against actual codebase
   - Flag all discrepancies
   - Flag all gaps
   - Flag all inconsistencies

4. **Generate Report**
   - Create gap analysis report
   - Document all issues found
   - Document all corrections needed

5. **Apply Corrections**
   - Edit plan document directly
   - Apply only necessary corrections
   - Preserve correct sections
   - Add comments for context

6. **Verify Corrections**
   - Re-check corrected sections
   - Ensure corrections are accurate
   - Ensure no new errors introduced

---

## Common Gap Patterns to Watch For

### Pattern 1: Wrong File Names
**Example:**
- Plan says: `client-context-notes.md`
- Actual: `discovery-call-notes.md`
- **Flag:** ✅ Wrong file name

### Pattern 2: Wrong Directory Paths
**Example:**
- Plan says: `.artifacts/protocol-02/notes.md`
- Actual: `.artifacts/protocol-02/discovery-call-notes.md`
- **Flag:** ✅ Wrong path structure

### Pattern 3: Missing Artifacts
**Example:**
- Plan references: `question-bank.md`
- Actual: File exists but structure differs
- **Flag:** ✅ Structure mismatch

### Pattern 4: Wrong Script Functionality
**Example:**
- Plan says: Script does X
- Actual: Script does Y
- **Flag:** ✅ Functionality mismatch

### Pattern 5: Wrong Integration Points
**Example:**
- Plan says: Integrates with X
- Actual: Integrates with Y
- **Flag:** ✅ Integration mismatch

---

## Success Criteria

**[STRICT]** Review is successful if:
- ✅ All file paths verified correct
- ✅ All file names verified correct
- ✅ All script functionality verified correct
- ✅ All integration points verified correct
- ✅ All gaps flagged and corrected
- ✅ Plan matches actual codebase structure
- ✅ Only wrong items corrected
- ✅ Correct items preserved

---

## Important Notes

1. **Only flag what's wrong** - Don't suggest improvements to correct items
2. **Use common sense** - If something is logically correct but stylistically different, it's OK
3. **Verify before flagging** - Double-check codebase before flagging issues
4. **Preserve correct sections** - Don't modify correct parts of plan
5. **Be specific** - Provide exact file paths, line numbers, quotes when flagging

---

**End of Review Protocol**

**Execute this review by:**
1. Loading enhancement plan
2. Scanning codebase structure
3. Comparing and flagging gaps
4. Generating gap report
5. Applying corrections to plan
6. Verifying corrections

