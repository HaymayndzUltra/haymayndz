---
status: draft
last_updated: 2025-01-27
prepared_by: Protocol 02 AI Assistant
---

# Question Bank

**Purpose:** Prioritized discovery questions grouped by theme, linked to assumptions tracker

---

## Priority Legend
- **P0 (Critical)** - Must ask in first 15 minutes
- **P1 (High)** - Must ask during call
- **P2 (Medium)** - Ask if time permits
- **P3 (Low)** - Can defer to follow-up

---

## Business Outcomes

### Q-BUS-001: Weekly Time Commitment
**Priority:** P0 (Critical)  
**Linked Assumption:** assumptions-gaps.md #1 (Time Commitment)  
**Question:** "You mentioned part-time engagement. What's your expected weekly time commitment? Are you thinking 5-10 hours, 10-15 hours, or something else?"  
**Follow-up if <15 hrs:** "Great, that aligns with the proposed weekly cap of 15 hours. Does that structure work for you?"  
**Follow-up if >15 hrs:** "I proposed a 15-hour weekly cap. Would you prefer to adjust that, or should we prioritize what gets covered within that limit?"

---

### Q-BUS-002: Budget & Pricing Acceptance
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #5 (Pricing)  
**Question:** "I proposed $100/hour with a weekly cap of $1,500 (15 hours). Does that pricing structure work for your budget?"  
**Follow-up if yes:** "Perfect. Should we start with a weekly cap, or would you prefer a monthly retainer?"  
**Follow-up if no:** "What pricing structure would work better for you? I'm flexible on format."

---

### Q-BUS-003: Pricing Structure Preference
**Priority:** P2 (Medium)  
**Linked Assumption:** assumptions-gaps.md #5 (Pricing - Weekly cap structure)  
**Question:** "Do you prefer the weekly cap structure, or would a monthly retainer or project-based pricing work better for you?"  
**Context:** Only ask if Q-BUS-002 indicates pricing needs discussion.

---

### Q-BUS-004: Monthly Budget Validation
**Priority:** P2 (Medium)  
**Linked Assumption:** assumptions-gaps.md #5 (Pricing - Monthly estimate)  
**Question:** "At the proposed rate, monthly would be around $6,000 (60 hours). Does that fit within your budget?"  
**Context:** Only ask if monthly budget is relevant to client's planning.

---

### Q-BUS-005: Product Definition ⚠️ CRITICAL
**Priority:** P0 (Critical)  
**Linked Assumption:** assumptions-gaps.md #1 (Missing Data - Product Definition)  
**Question:** "I don't see details about the SaaS product you're building in the job post. Can you walk me through what you're building? What problem does it solve, and who is it for?"  
**Follow-up prompts:**
- "What's the core value proposition?"
- "Who are your target users?"
- "What's the current state—what's already built?"
- "What's the MVP scope vs future features?"

---

### Q-BUS-006: End Users
**Priority:** P0 (Critical)  
**Linked Assumption:** assumptions-gaps.md #2 (Missing Data - End Users)  
**Question:** "Who are the end users of your SaaS product? Are they individual consumers, businesses, developers, or something else?"  
**Follow-up:** "Understanding the user base helps me provide more relevant architectural guidance."

---

### Q-BUS-007: Success Criteria for Mentorship
**Priority:** P2 (Medium)  
**Linked Assumption:** assumptions-gaps.md #9 (Missing Data - Success Criteria)  
**Question:** "How will we know this mentorship engagement is successful? What outcomes are you hoping to achieve?"  
**Follow-up:** "This helps me tailor guidance to your specific goals."

---

## User Journeys

### Q-USER-001: User Personas & Use Cases
**Priority:** P1 (High)  
**Question:** "Can you describe your primary user personas? What are their main use cases with your product?"  
**Linked to:** Q-BUS-006 (End Users)  
**Context:** Only ask if Q-BUS-006 reveals user base.

---

### Q-USER-002: User Journey Priorities
**Priority:** P2 (Medium)  
**Question:** "Which user journeys are most critical for MVP? What can wait until post-MVP?"  
**Context:** Helps prioritize architectural decisions.

---

## Functional Scope

### Q-FUNC-001: Role Boundaries (Guidance vs Implementation)
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #3 (Scope & Role)  
**Question:** "The job post mentions this is a guidance role, not code-heavy. Help me understand the boundaries—are you looking for code reviews, architectural guidance, or would you also want me to write code in some cases?"  
**Follow-up:** "I want to make sure we're aligned on what 'guidance' means in practice."

---

### Q-FUNC-002: Architectural Review Process
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #3 (Scope & Role - Architectural reviews)  
**Question:** "You mentioned architectural reviews. How would you like that to work? Should I review code you've written, or discuss architecture before you build?"  
**Follow-up:** "I'm thinking we could do architectural reviews before major decisions to catch issues early—like the database scaling example I mentioned."

---

### Q-FUNC-003: Screen-Share Sessions
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #3 (Scope & Role - Live sessions)  
**Question:** "You mentioned joining live or recorded screen-share sessions. How often are you thinking? Weekly? As-needed?"  
**Follow-up:** "I'm available for scheduled calls or async review—what works better for your workflow?"

---

### Q-FUNC-004: Sounding Board for Technical Decisions
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #3 (Scope & Role - Sounding board)  
**Question:** "You want a sounding board for 'is this the right approach?' questions. How do you envision that working? Real-time during sessions, async via messages, or both?"  
**Follow-up:** "I can provide quick async feedback for smaller decisions and deeper analysis for bigger architectural choices."

---

### Q-FUNC-005: Technical Pain Points
**Priority:** P2 (Medium)  
**Linked Assumption:** assumptions-gaps.md #7 (Missing Data - Technical Pain Points)  
**Question:** "What are your biggest technical concerns or challenges right now? Where do you feel most uncertain?"  
**Context:** Helps prioritize initial guidance focus areas.

---

## Technical Stack

### Q-TECH-001: Current Tech Stack Validation
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #4 (Technical Stack)  
**Question:** "The job post mentions Next.js, Node, Supabase, and Postgres. Is that your current stack, or are you planning to use those?"  
**Follow-up:** "What versions are you using? Any specific configurations or constraints I should know about?"

---

### Q-TECH-002: AI/LLM Integrations
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #4 (Technical Stack - AI/LLM)  
**Question:** "You mentioned using ChatGPT and Claude for development. Are you also integrating AI/LLM features into your SaaS product itself?"  
**Follow-up:** "Understanding AI integrations helps me provide relevant architectural guidance."

---

### Q-TECH-003: Automation Platforms
**Priority:** P2 (Medium)  
**Linked Assumption:** assumptions-gaps.md #4 (Technical Stack - Automation)  
**Question:** "Are you using Zapier, n8n, or other automation platforms? How do they fit into your architecture?"  
**Context:** Only ask if automation is relevant to product.

---

### Q-TECH-004: Current Progress & Codebase
**Priority:** P0 (Critical)  
**Linked Assumption:** assumptions-gaps.md #3 (Missing Data - Current Progress)  
**Question:** "What's already built? Can you walk me through your current codebase, or share access to a repo? What's working well, and what needs attention?"  
**Follow-up:** "This helps me understand where you're starting from and what guidance would be most valuable."

---

## Integrations

### Q-INT-001: Third-Party Integrations
**Priority:** P1 (High)  
**Question:** "What third-party services or APIs does your SaaS need to integrate with? Payment processors, email services, analytics, etc.?"  
**Context:** Critical for architectural decisions.

---

### Q-INT-002: Data Sources & Ownership
**Priority:** P1 (High)  
**Question:** "What data sources are you working with? Who owns the data, and what are the access requirements?"  
**Context:** Important for integration inventory.

---

## Compliance

### Q-COMP-001: Compliance Requirements
**Priority:** P2 (Medium)  
**Question:** "Are there any compliance requirements? GDPR, HIPAA, SOC2, PCI-DSS, etc.?"  
**Context:** Only ask if product involves sensitive data or regulated industries.

---

## Delivery Logistics

### Q-TIME-001: Timeline & Milestones
**Priority:** P0 (Critical)  
**Linked Assumption:** assumptions-gaps.md #6 (Timeline & Milestones)  
**Question:** "What's your target timeline for MVP launch? And when do you need to be production-ready?"  
**Follow-up:** "Understanding your timeline helps me prioritize guidance and identify potential bottlenecks."

---

### Q-TIME-002: Getting Started Timeline
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #6 (Timeline - Getting started)  
**Question:** "When are you looking to get started? Is there urgency, or can we take time to set up the engagement properly?"  
**Follow-up:** "I want to make sure we start on the right foot."

---

### Q-TIME-003: MVP Scope & Timeline
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #6 (Timeline - MVP scope)  
**Question:** "What's included in your MVP scope? And what's the target launch date?"  
**Follow-up:** "This helps me focus guidance on what matters most for MVP."

---

## Communication

### Q-COMM-001: Communication Format Preference
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #2 (Communication Format)  
**Question:** "How do you prefer to communicate? Weekly scheduled calls, async messages, or a mix? I'm flexible—available weekdays 9am-6pm EST for calls, or we can do async."  
**Follow-up:** "What response time works for you on async questions?"

---

### Q-COMM-002: Timezone & Availability
**Priority:** P1 (High)  
**Linked Assumption:** assumptions-gaps.md #2 (Communication Format - Timezone)  
**Question:** "You're based in the U.S. What timezone? And what times work best for scheduled calls?"  
**Follow-up:** "I'm available 9am-6pm EST—does that overlap well with your schedule?"

---

### Q-COMM-003: Documentation & Knowledge Sharing
**Priority:** P2 (Medium)  
**Question:** "How do you want to document our discussions and decisions? Written summaries, shared notes, or something else?"  
**Context:** Important for async communication and knowledge retention.

---

## Question Execution Plan

### First 15 Minutes (Critical Questions)
1. Q-BUS-005: Product Definition ⚠️
2. Q-BUS-006: End Users
3. Q-TECH-004: Current Progress
4. Q-BUS-001: Weekly Time Commitment
5. Q-TIME-001: Timeline & Milestones

### Main Discovery (30-45 minutes)
- All P1 questions across themes
- Follow-ups from critical questions
- Explore technical stack and integrations

### Wrap-up (Final 10-15 minutes)
- P2 questions if time permits
- Summarize key decisions
- Confirm next steps

---

## Validation Checklist

- [x] All `ASK CLIENT` items from assumptions-gaps.md mapped to questions
- [x] Critical questions prioritized for first 15 minutes
- [x] Question IDs match assumptions tracker references
- [x] Follow-up prompts prepared for common responses
- [x] Questions grouped by theme for logical flow

