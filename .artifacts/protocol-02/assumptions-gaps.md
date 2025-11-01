---
status: draft
last_updated: 2025-01-27
prepared_by: Protocol 02 AI Assistant
---

# Assumptions & Gap Tracker

**Purpose:** Track all assumptions from proposal and identify missing data requiring client confirmation

---

## Status Legend
- `confirmed` - Validated with client
- `ASK CLIENT` - Must ask during discovery call
- `research` - Can research independently before asking
- `follow-up` - Requires follow-up after call

---

## Assumptions from Proposal

### 1. Time Commitment Assumptions
| Assumption | Source | Status | Question ID |
|------------|--------|--------|-------------|
| Weekly cap of 15 hours is acceptable | PROPOSAL.md line 7 | ASK CLIENT | Q-BUS-001 |
| Part-time engagement means ≤15 hrs/week | proposal-summary.json | ASK CLIENT | Q-BUS-001 |
| Weekly sessions preferred over async-only | PROPOSAL.md line 7 | ASK CLIENT | Q-COMM-001 |

### 2. Communication Format Assumptions
| Assumption | Source | Status | Question ID |
|------------|--------|--------|-------------|
| Weekly scheduled calls preferred | PROPOSAL.md line 7 | ASK CLIENT | Q-COMM-001 |
| Async is acceptable alternative | PROPOSAL.md line 7 | ASK CLIENT | Q-COMM-001 |
| Availability 9am-6pm EST matches client schedule | PROPOSAL.md line 20 | ASK CLIENT | Q-COMM-002 |

### 3. Scope & Role Assumptions
| Assumption | Source | Status | Question ID |
|------------|--------|--------|-------------|
| Guidance-only role (not code-heavy) | JOB-POST.md lines 9-10 | ASK CLIENT | Q-FUNC-001 |
| Architectural reviews expected | PROPOSAL.md line 7 | ASK CLIENT | Q-FUNC-002 |
| Live screen-share sessions expected | JOB-POST.md line 23 | ASK CLIENT | Q-FUNC-003 |
| Sounding board for technical decisions | JOB-POST.md line 26 | ASK CLIENT | Q-FUNC-004 |

### 4. Technical Stack Assumptions
| Assumption | Source | Status | Question ID |
|------------|--------|--------|-------------|
| Next.js, Node, Supabase, Postgres stack | JOB-POST.md line 17 | research | Q-TECH-001 |
| AI/LLM integrations involved | JOB-POST.md line 18 | ASK CLIENT | Q-TECH-002 |
| Automation platforms (Zapier/n8n) used | JOB-POST.md line 17 | ASK CLIENT | Q-TECH-003 |

### 5. Pricing Assumptions
| Assumption | Source | Status | Question ID |
|------------|--------|--------|-------------|
| $100/hr rate acceptable | proposal-summary.json | ASK CLIENT | Q-BUS-002 |
| Weekly cap structure preferred | proposal-summary.json | ASK CLIENT | Q-BUS-003 |
| Monthly budget ~$6,000 acceptable | proposal-summary.json | ASK CLIENT | Q-BUS-004 |

### 6. Timeline Assumptions
| Assumption | Source | Status | Question ID |
|------------|--------|--------|-------------|
| Ongoing support through MVP → production | PROPOSAL.md line 7 | ASK CLIENT | Q-TIME-001 |
| 15-20 min alignment call sufficient | PROPOSAL.md line 20 | confirmed | (initial call) |
| Timeline for getting started is flexible | PROPOSAL.md line 20 | ASK CLIENT | Q-TIME-002 |

---

## Missing Data (Gaps)

### Critical Gaps (Must Ask)

1. **Product Definition**
   - **Gap:** What SaaS product is being built?
   - **Status:** ASK CLIENT
   - **Question ID:** Q-BUS-005
   - **Impact:** HIGH - Cannot provide relevant guidance without product context

2. **End Users**
   - **Gap:** Who are the target end users of the SaaS?
   - **Status:** ASK CLIENT
   - **Question ID:** Q-BUS-006
   - **Impact:** HIGH - Architecture decisions depend on user needs

3. **Current Progress**
   - **Gap:** What progress has been made already? What's built?
   - **Status:** ASK CLIENT
   - **Question ID:** Q-TECH-004
   - **Impact:** HIGH - Need baseline to provide relevant guidance

4. **Weekly Time Commitment**
   - **Gap:** Specific hours/week expectation for part-time engagement
   - **Status:** ASK CLIENT
   - **Question ID:** Q-BUS-001
   - **Impact:** MEDIUM - Affects scope and pricing structure

5. **Communication Preferences**
   - **Gap:** Preferred format (scheduled calls vs async vs hybrid)
   - **Status:** ASK CLIENT
   - **Question ID:** Q-COMM-001
   - **Impact:** MEDIUM - Affects engagement structure

6. **Timeline & Milestones**
   - **Gap:** Target dates for MVP launch, production readiness
   - **Status:** ASK CLIENT
   - **Question ID:** Q-TIME-003
   - **Impact:** HIGH - Affects prioritization and guidance focus

### Medium Priority Gaps

7. **Technical Pain Points**
   - **Gap:** Specific technical challenges or concerns
   - **Status:** ASK CLIENT
   - **Question ID:** Q-FUNC-005
   - **Impact:** MEDIUM - Helps prioritize guidance areas

8. **Budget Constraints**
   - **Gap:** Actual budget vs proposed $1,500/week cap
   - **Status:** ASK CLIENT
   - **Question ID:** Q-BUS-002
   - **Impact:** MEDIUM - Affects engagement structure

9. **Success Criteria**
   - **Gap:** How will success be measured for the mentorship engagement?
   - **Status:** ASK CLIENT
   - **Question ID:** Q-BUS-007
   - **Impact:** MEDIUM - Enables outcome tracking

### Low Priority Gaps (Research First)

10. **Current Tech Stack Details**
    - **Gap:** Specific versions, configurations, integrations
    - **Status:** research
    - **Action:** Can research Next.js, Supabase, Postgres best practices before call
    - **Impact:** LOW - Can gather independently

---

## Validation Checklist

- [ ] All `ASK CLIENT` items mapped to questions in question-bank.md
- [ ] Critical gaps prioritized for discovery call
- [ ] Research items identified for pre-call preparation
- [ ] Follow-up items tracked with owners and due dates

---

## Next Actions

1. **Before Call:** Research technical stack best practices (Q-TECH-001)
2. **During Call:** Address all `ASK CLIENT` items marked Critical or High Impact
3. **After Call:** Update status to `confirmed` or `follow-up` with owner assignment

