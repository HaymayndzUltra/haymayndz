---
status: draft
last_updated: 2025-01-27
prepared_by: Protocol 02 AI Assistant
---

# Call Agenda & Checklist

**Purpose:** Structured meeting agenda with reminders and checkpoints

**Scheduled Duration:** 45-60 minutes  
**Meeting Type:** Discovery Call  
**Attendees:** Client + Solo Developer (Mentor)

---

## Pre-Call Checklist

### Technical Setup
- [ ] Cursor workspace loaded with discovery artifacts
- [ ] Question bank reviewed and prioritized
- [ ] Integration inventory template ready
- [ ] Live notes template prepared
- [ ] Screen-sharing capability tested
- [ ] Recording capability ready (if consent obtained)

### Context Preparation
- [ ] Discovery brief reviewed
- [ ] Assumptions tracker reviewed
- [ ] Risk & opportunity list reviewed
- [ ] Scenario guides reviewed
- [ ] Proposal and job post refreshed in memory

### Equipment Check
- [ ] Audio/video working
- [ ] Internet connection stable
- [ ] Backup communication method available
- [ ] Note-taking tool ready (or use discovery-call-notes.md template)

---

## Meeting Agenda

### 0. Introductions & Setup (5 minutes)

**Objectives:**
- Build rapport
- Set meeting expectations
- Confirm recording consent (if applicable)

**Script:**
- "Thanks for taking the time. I'm excited to learn more about what you're building."
- "The goal today is to understand your product, technical needs, and how I can best support you."
- "I'd like to take notes during our call—are you okay with that? [If recording:] And would you be okay with me recording this for my reference?"

**Outcome:** Comfortable, transparent start

---

### 1. Product Understanding (15 minutes) ⚠️ CRITICAL

**Objectives:**
- Understand what product is being built
- Identify target users
- Clarify MVP scope

**Key Questions:**
- Q-BUS-005: Product Definition ⚠️ CRITICAL
- Q-BUS-006: End Users
- Q-TECH-004: Current Progress & Codebase

**Script:**
- "I don't see details about the SaaS product you're building in the job post. Can you walk me through what you're building?"
- "What problem does it solve, and who is it for?"
- "What's already built? What's your current progress?"

**Notes:** Capture in discovery-call-notes.md under Product Understanding section

**Success Criteria:** Clear understanding of product, users, and current state

---

### 2. Technical Stack & Architecture (15 minutes)

**Objectives:**
- Validate tech stack assumptions
- Understand current architecture
- Identify integration needs

**Key Questions:**
- Q-TECH-001: Current Tech Stack Validation
- Q-TECH-002: AI/LLM Integrations
- Q-TECH-004: Current Progress & Codebase
- Q-INT-001: Third-Party Integrations

**Script:**
- "The job post mentions Next.js, Node, Supabase, Postgres. Is that your current stack?"
- "What integrations do you need? Payment processors, email services, etc.?"
- "Are you integrating AI/LLM features into your product?"

**Notes:** Capture in discovery-call-notes.md and update integration-inventory.md

**Success Criteria:** Tech stack validated, integrations identified, architecture understood

---

### 3. Engagement Structure (10 minutes)

**Objectives:**
- Clarify role boundaries
- Align on communication format
- Confirm time commitment and pricing

**Key Questions:**
- Q-BUS-001: Weekly Time Commitment
- Q-BUS-002: Budget & Pricing Acceptance
- Q-FUNC-001: Role Boundaries (Guidance vs Implementation)
- Q-COMM-001: Communication Format Preference

**Script:**
- "The job post mentions this is a guidance role, not code-heavy. Help me understand the boundaries—what does 'guidance' mean to you?"
- "I proposed $100/hr with a $1,500 weekly cap (15 hours). Does that work for your budget?"
- "How do you prefer to communicate? Weekly calls, async, or a mix?"

**Notes:** Capture in discovery-call-notes.md under Engagement Structure section

**Success Criteria:** Role boundaries clear, pricing accepted, communication format agreed

---

### 4. Timeline & Milestones (10 minutes)

**Objectives:**
- Understand MVP timeline
- Identify critical milestones
- Set expectations for production readiness

**Key Questions:**
- Q-TIME-001: Timeline & Milestones
- Q-TIME-003: MVP Scope & Timeline
- Q-TIME-002: Getting Started Timeline

**Script:**
- "What's your target timeline for MVP launch?"
- "When do you need to be production-ready?"
- "What's included in your MVP scope?"

**Notes:** Capture in discovery-call-notes.md and prepare for timeline-discussion.md

**Success Criteria:** Timeline understood, MVP scope clear, milestones identified

---

### 5. Wrap-up & Next Steps (5-10 minutes)

**Objectives:**
- Summarize key decisions
- Confirm next steps
- Set expectations for follow-up

**Script:**
- "Let me summarize what I heard: [key points]"
- "Does that sound right?"
- "Next steps: I'll send a recap email within [timeframe] with our discussion and next actions."
- "When would you like to get started?"

**Notes:** Capture in discovery-call-notes.md under Wrap-up section

**Success Criteria:** Clear next steps, recap commitment, start date confirmed

---

## Post-Call Checklist

### Immediate Actions (< 1 hour)
- [ ] Review discovery-call-notes.md for completeness
- [ ] Update assumptions-gaps.md with confirmed items
- [ ] Update integration-inventory.md with confirmed systems
- [ ] Flag any unresolved items for follow-up

### Within 24 Hours
- [ ] Draft discovery-recap.md
- [ ] Update client-discovery-form.md with confirmed details
- [ ] Update scope-clarification.md with technical decisions
- [ ] Update timeline-discussion.md with agreed milestones
- [ ] Update communication-plan.md with agreed format
- [ ] Send recap to client

### Follow-up Items
- [ ] Schedule follow-up call if needed
- [ ] Request access to codebase/repository if applicable
- [ ] Follow up on any pending questions
- [ ] Set up communication channels (Slack, email, etc.)

---

## Reminders & Notes

### Recording Consent
- **Reminder:** Always ask for consent before recording
- **If recording:** Save transcript to `.artifacts/protocol-02/transcripts/`
- **If not recording:** Take detailed notes in discovery-call-notes.md

### Recap Send Deadline
- **Target:** Within 24 hours of call
- **Format:** discovery-recap.md sent via email
- **Include:** Summary of decisions, open items, next steps

### Follow-up Owner
- **Developer/Mentor:** Owns recap send and follow-up
- **Client:** Owns approval of recap and responding to open items

### Cursor Context Load
- **Before Call:** Load discovery artifacts into `.cursor/rules/` for reference
- **During Call:** Use live notes template for real-time capture
- **After Call:** Update artifacts with confirmed information

---

## Validation

- [x] Agenda duration matches scheduled meeting (45-60 minutes)
- [x] Checklist covers Cursor context load, question bank review, equipment check
- [x] Critical questions prioritized in first 15 minutes
- [x] Reminders included for recording consent, recap deadline, follow-up owner
- [x] Success criteria defined for each section

---

## Execution Notes

**Meeting Flow:**
1. Start with introductions (5 min)
2. Product understanding (15 min) - CRITICAL
3. Technical stack (15 min)
4. Engagement structure (10 min)
5. Timeline (10 min)
6. Wrap-up (5-10 min)

**Flexibility:** Adjust time allocation based on client responses and priorities

**Critical Path:** Product understanding (Section 1) must be completed before proceeding

