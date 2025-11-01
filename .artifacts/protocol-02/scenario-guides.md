---
status: draft
last_updated: 2025-01-27
prepared_by: Protocol 02 AI Assistant
---

# Scenario Response Guides

**Purpose:** Pivot playbooks for common discovery call scenarios with trigger phrases, recommended responses, and fallback plans

---

## Scenario 1: Budget Adjustment Request

### Trigger Phrases
- "The budget is a bit tight"
- "Can we do this for less?"
- "Is there a way to reduce costs?"
- "What if we start smaller?"

### Context
Client may want to adjust the proposed $100/hr rate or $1,500/week cap.

### Recommended Response Framework

**Step 1: Understand the Constraint**
- "I understand budget is a consideration. What's a range that would work better for you?"
- "Is it the hourly rate or the weekly cap that's the challenge?"

**Step 2: Offer Flexibility**
- "I'm flexible on structure. We could:
  - Reduce weekly cap to 10 hours ($1,000/week)
  - Do monthly retainer at lower rate
  - Start with a smaller scope and scale up"

**Step 3: Value Focus**
- "What's most important to you—having more time available, or keeping costs lower?"
- "We can prioritize the highest-impact guidance areas to maximize value within your budget"

**Step 4: Fallback Plan**
- "Alternatively, we could start with a 2-week trial engagement to prove value, then adjust based on what works"

### Proposal Commitment Alignment
- **From Proposal:** $100/hr with $1,500/week cap (15 hours)
- **Flexibility:** Can adjust cap, not rate (maintain rate integrity)
- **Boundary:** Don't go below $80/hr (market minimum for senior guidance)

### Question References
- Q-BUS-002: Budget & Pricing Acceptance
- Q-BUS-003: Pricing Structure Preference
- Q-BUS-001: Weekly Time Commitment

---

## Scenario 2: Scope Expansion Request

### Trigger Phrases
- "Can you also help with [implementation task]?"
- "Would you be able to write code?"
- "I need someone to actually build this"
- "Can we expand beyond just guidance?"

### Context
Client may want to expand from "guidance-only" to include implementation work.

### Recommended Response Framework

**Step 1: Clarify Expectations**
- "I want to make sure I understand what you're looking for. Are you thinking:
  - Code reviews and architectural guidance (original scope)
  - Actual code implementation
  - A mix of both?"

**Step 2: Set Boundaries**
- "My proposal focused on guidance and mentorship because that's where I provide the most value—helping you avoid costly mistakes early."
- "If you need implementation work, we'd need to adjust the scope and potentially the pricing structure."

**Step 3: Offer Options**
- "Option A: Stay guidance-focused, and I help you build faster by catching issues early"
- "Option B: Hybrid approach—guidance for architecture, code reviews, and some implementation for critical pieces"
- "Option C: Full implementation—but that would be a different engagement structure"

**Step 4: Fallback Plan**
- "Let's start with guidance and see how it goes. If you need implementation help later, we can adjust."
- "I can also recommend other developers for implementation work if needed."

### Proposal Commitment Alignment
- **From Proposal:** "Guidance sessions" and "architectural reviews" (not implementation)
- **Flexibility:** Can expand scope if client needs it, but requires re-scoping
- **Boundary:** Maintain mentorship focus; don't become full-time developer

### Question References
- Q-FUNC-001: Role Boundaries (Guidance vs Implementation)
- Q-FUNC-002: Architectural Review Process
- Q-BUS-001: Weekly Time Commitment

---

## Scenario 3: Compliance Gap Discovery

### Trigger Phrases
- "We handle [sensitive data type]"
- "Do we need [compliance requirement]?"
- "Our users are in [regulated industry]"
- "We're not sure about [legal requirement]"

### Context
Product may involve sensitive data or regulated industries requiring compliance.

### Recommended Response Framework

**Step 1: Assess the Gap**
- "Let me understand the compliance requirements. Are you handling:
  - Personal health information (HIPAA)?
  - Payment card data (PCI-DSS)?
  - European user data (GDPR)?
  - Financial data (SOC2, etc.)?"

**Step 2: Evaluate Impact**
- "Compliance requirements affect architecture decisions significantly. For example:
  - Data encryption requirements
  - Access control and audit logging
  - Data residency requirements
  - Third-party vendor assessments"

**Step 3: Provide Guidance**
- "I can help you understand compliance requirements and architect accordingly, but I'm not a compliance lawyer. You may need legal counsel for specific requirements."
- "Let's identify the compliance needs early so we can architect correctly from the start."

**Step 4: Fallback Plan**
- "If compliance is complex, we may need to bring in a compliance consultant or lawyer. I can help architect to meet requirements, but legal interpretation is outside my scope."

### Proposal Commitment Alignment
- **From Proposal:** Focus on architectural guidance (includes compliance considerations)
- **Flexibility:** Can provide architectural guidance for compliance
- **Boundary:** Not legal counsel; recommend legal review for complex requirements

### Question References
- Q-COMP-001: Compliance Requirements
- Q-INT-002: Data Sources & Ownership
- Q-TECH-001: Current Tech Stack Validation

---

## Scenario 4: Timeline Unrealistic Expectations

### Trigger Phrases
- "We need to launch in [very short timeframe]"
- "Can we move faster?"
- "Is [aggressive timeline] realistic?"
- "What's the minimum viable timeline?"

### Context
Client may have unrealistic expectations about MVP timeline or production readiness.

### Recommended Response Framework

**Step 1: Understand the Constraint**
- "I hear you want to move fast. What's driving the timeline? Is it:
  - Market opportunity?
  - Investor/partner commitments?
  - Competitive pressure?
  - Personal goals?"

**Step 2: Reality Check**
- "Let me be honest about realistic timelines. For MVP → production:
  - MVP can be 2-6 months depending on scope
  - Production-ready adds 1-3 months for testing, security, scaling
  - Rushing can create technical debt that costs 3x more to fix later"

**Step 3: Focus on MVP Scope**
- "The key is defining MVP scope clearly. What's absolutely essential for launch vs what can wait?"
- "We can prioritize to hit your timeline, but some features may need to wait until post-MVP."

**Step 4: Fallback Plan**
- "If timeline is critical, we can:
  - Reduce MVP scope to essentials only
  - Parallelize work (you build, I review)
  - Accept some technical debt with plan to refactor"

### Proposal Commitment Alignment
- **From Proposal:** "Ongoing support through MVP → production" (implies realistic timeline)
- **Flexibility:** Can accelerate with scope reduction
- **Boundary:** Won't recommend shortcuts that create critical technical debt

### Question References
- Q-TIME-001: Timeline & Milestones
- Q-TIME-003: MVP Scope & Timeline
- Q-BUS-005: Product Definition

---

## Scenario 5: Tech Stack Mismatch

### Trigger Phrases
- "We're actually using [different tech]"
- "We're thinking of switching to [new tech]"
- "Are you familiar with [tech not mentioned]?"
- "We're not sure about [tech choice]"

### Context
Actual tech stack may differ from job post, or client may want to change stack.

### Recommended Response Framework

**Step 1: Understand Current State**
- "Let me understand your current stack. What are you actually using now?"
- "Are you planning to migrate, or are you starting fresh?"

**Step 2: Assess Expertise Match**
- "I'm most experienced with Next.js, Node, Supabase, Postgres. If you're using [different tech], I can still provide general architectural guidance, but some stack-specific advice may be limited."
- "I'm happy to learn your stack, but you'd get more value if I'm already expert in it."

**Step 3: Evaluate Tech Decisions**
- "If you're considering switching, let's discuss the pros/cons. Sometimes switching mid-project creates more problems than it solves."
- "If you're committed to [different tech], let's make sure it's the right choice for your use case."

**Step 4: Fallback Plan**
- "If there's a significant stack mismatch, we could:
  - Focus on general architecture principles (still valuable)
  - I can learn your stack (adds time/cost)
  - You might want someone with specific expertise in [their stack]"

### Proposal Commitment Alignment
- **From Proposal:** "Full-stack experience across Next.js, Node, Supabase, Postgres"
- **Flexibility:** Can provide general guidance even with different stack
- **Boundary:** Be honest about expertise limits; don't pretend expertise you don't have

### Question References
- Q-TECH-001: Current Tech Stack Validation
- Q-TECH-004: Current Progress & Codebase
- Q-FUNC-001: Role Boundaries

---

## Scenario 6: Communication Format Mismatch

### Trigger Phrases
- "I prefer [different format]"
- "I'm not available [at proposed times]"
- "Can we do [different approach]?"
- "I don't like [scheduled calls/async]"

### Context
Client may prefer different communication format than proposed.

### Recommended Response Framework

**Step 1: Understand Preference**
- "I want to make sure our communication works for you. What format works best?"
- "I'm flexible—what's your preference?"

**Step 2: Offer Flexibility**
- "I proposed [X], but I'm happy to adjust to [Y] if that works better for you."
- "We can do a hybrid approach—scheduled calls for deep dives, async for quick questions."

**Step 3: Establish Expectations**
- "If we go async, what's your expected response time? And what's mine?"
- "If we do scheduled calls, what times work best for you?"

**Step 4: Fallback Plan**
- "Let's start with [their preference] and adjust if needed. The important thing is we have effective communication."

### Proposal Commitment Alignment
- **From Proposal:** "Weekly guidance sessions (or async, your call)" and "Available weekdays 9am-6pm EST or async"
- **Flexibility:** Already flexible in proposal
- **Boundary:** Need to establish clear expectations regardless of format

### Question References
- Q-COMM-001: Communication Format Preference
- Q-COMM-002: Timezone & Availability
- Q-COMM-003: Documentation & Knowledge Sharing

---

## Scenario Response Execution Checklist

- [ ] All scenarios mapped to proposal commitments
- [ ] Trigger phrases identified
- [ ] Recommended responses framed
- [ ] Fallback plans documented
- [ ] Question references linked
- [ ] Proposal alignment validated

---

## Usage Notes

- Use scenario guides during discovery call when trigger phrases are detected
- Adapt responses to specific client context
- Maintain proposal commitment integrity while being flexible
- Document which scenarios occurred during call for future reference

