# Live Discovery Call Test Scenarios

Generated from Protocol 02 artifacts. Natural Taglish voice, client-safe responses.

---

## TIMELINE Bucket

### T01: MVP Launch Timeline
**Client:** "We're aiming to launch MVP in 4 weeks. Realistic ba yan?"

**Assistant (expected):** "Four weeks is tight pero doable depende sa scope. What's included sa MVP? Kasi if it's auth, core features, and basic UI, we can work with that. But we'd need to be super clear on what's in vs out para hindi tayo mag-overcommit."

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-001, Q-TIME-003), `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 6)

**Side-effects:**
- Append to `risk-opportunity-list.md`: "Timeline: 4-week MVP target - requires scope validation"
- Upsert `discovery-approval-log.json`: `{"timeline_mvp": "4_weeks", "status": "needs_scope_validation"}`

---

### T02: Production Readiness Timeline
**Client:** "When can we go production-ready after MVP?"

**Assistant (expected):** "Typically 4-8 weeks after MVP launch, pero it depends on what 'production-ready' means for you. Are we talking polished UI, full testing, monitoring setup? Or just stable enough for early users? Let's define that para we can plan properly."

**Grounding:** `.artifacts/protocol-01/PROPOSAL.md` (line 7), `.artifacts/protocol-02/discovery-brief.md` (lines 23-25)

**Side-effects:**
- Append to `timeline-discussion.md`: "Production readiness: 4-8 weeks post-MVP, pending definition"

---

### T03: Getting Started Timeline
**Client:** "Can we start next week?"

**Assistant (expected):** "Next week works! Before we start, I'd like to do this discovery call para we're aligned. Then we can kick off right after. Does Monday or Tuesday work better for you?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-002), `.artifacts/protocol-01/PROPOSAL.md` (line 20)

**Side-effects:**
- Upsert `discovery-approval-log.json`: `{"start_date": "next_week", "discovery_call_needed": true}`

---

## SCOPE Bucket

### S01: Guidance vs Implementation Boundary
**Client:** "Can you write some code for critical parts like auth?"

**Assistant (expected):** "I can do architectural guidance and code reviews by default. For critical pieces like auth, I'm open to writing some code if needed—pero let's be clear that's outside the usual guidance scope. Would you want that as an exception, or should we adjust the engagement structure?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-FUNC-001, Q-FUNC-002), `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 1)

**Side-effects:**
- Append to `scope-clarification.md`: "Scope expansion: Client requests code implementation for auth (critical exception)"
- Append to `risk-opportunity-list.md`: "Scope creep risk: Code implementation requested for auth"

---

### S02: MVP Scope Definition
**Client:** "MVP should have user auth, dashboard, and Salesforce integration."

**Assistant (expected):** "Got it—auth, dashboard, Salesforce integration. That's doable for MVP. Is the Salesforce integration one-way (pull data) or two-way (sync)? And what's the dashboard showing—just Salesforce data or other sources too?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-003, Q-INT-001), `.artifacts/protocol-02/integration-inventory.md` (lines 22-37)

**Side-effects:**
- Upsert `client-discovery-form.md`: "MVP scope: auth + dashboard + Salesforce integration (one-way TBD)"
- Append to `integration-inventory.md`: "Salesforce integration required (direction TBD)"

---

### S03: Feature Prioritization
**Client:** "Can we add email notifications and analytics to MVP?"

**Assistant (expected):** "We can, pero that adds complexity. Email notifications are straightforward—analytics depends on what you're tracking. If we're tight on the 4-week timeline, I'd suggest pushing analytics to Phase 2 unless it's critical for MVP validation. What do you think?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-003), `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 6)

**Side-effects:**
- Append to `scope-clarification.md`: "Feature add: Email notifications (feasible), Analytics (suggest Phase 2)"
- Append to `risk-opportunity-list.md`: "Scope expansion: Email + analytics requested for MVP"

---

## PRICING Bucket

### P01: Weekly Cap Acceptance
**Client:** "The $1,500/week cap works for us."

**Assistant (expected):** "Perfect! So we're aligned on 15 hours/week at $100/hr. Should we start with weekly invoicing, or would you prefer monthly?"

**Grounding:** `.artifacts/protocol-01/proposal-summary.json` (lines 8-14), `.artifacts/protocol-02/question-bank.md` (Q-BUS-002)

**Side-effects:**
- Upsert `discovery-approval-log.json`: `{"pricing_approved": true, "weekly_cap": 1500, "invoicing": "TBD"}`

---

### P02: Budget Constraint
**Client:** "Budget is tight. Can we do 10 hours/week instead?"

**Assistant (expected):** "Totally understand. We can do 10 hours/week—that's $1,000/week. We'd just need to prioritize what gets covered within that time. What's most important to you—architectural reviews, live sessions, or async guidance?"

**Grounding:** `.artifacts/protocol-01/pricing-analysis.json` (lines 36-48), `.artifacts/protocol-02/question-bank.md` (Q-BUS-001, Q-BUS-002)

**Side-effects:**
- Upsert `discovery-approval-log.json`: `{"weekly_cap_adjusted": 1000, "hours_per_week": 10}`
- Append to `risk-opportunity-list.md`: "Budget constraint: Reduced to 10 hrs/week, prioritization needed"

---

### P03: Monthly Budget Validation
**Client:** "What's the monthly cost?"

**Assistant (expected):** "At 15 hours/week, monthly is around $6,000. Does that fit your budget?"

**Grounding:** `.artifacts/protocol-01/proposal-summary.json` (line 14), `.artifacts/protocol-02/question-bank.md` (Q-BUS-004)

**Side-effects:**
- None (informational query)

---

## INTEGRATION Bucket

### I01: Salesforce Integration Direction
**Client:** "We need to pull Salesforce data into our app."

**Assistant (expected):** "Got it—one-way pull from Salesforce. Do you have API access already, or do we need to set that up? And what data are we pulling—contacts, leads, opportunities?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-INT-001, Q-INT-002), `.artifacts/protocol-02/integration-inventory.md` (lines 22-37)

**Side-effects:**
- Append to `integration-inventory.md`: "Salesforce: one-way pull, data types TBD, API access TBD"
- Upsert `client-discovery-form.md`: "Integration: Salesforce one-way pull"

---

### I02: Payment Gateway Integration
**Client:** "We'll use Stripe for payments."

**Assistant (expected):** "Stripe is solid. Do you have a Stripe account set up already? And are we handling subscriptions, one-time payments, or both? That affects how we structure the integration."

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-INT-001), `.artifacts/protocol-02/integration-inventory.md` (line 31)

**Side-effects:**
- Append to `integration-inventory.md`: "Payment: Stripe (account status TBD, payment type TBD)"
- Append to `risk-opportunity-list.md`: "Compliance: Stripe integration requires PCI-DSS consideration"

---

### I03: Email Service Integration
**Client:** "We need transactional emails—signup, password reset, notifications."

**Assistant (expected):** "For transactional emails, I'd suggest SendGrid or Postmark. Do you have a preference, or should we evaluate based on volume and cost? And do you need email templates designed, or do you have those already?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-INT-001), `.artifacts/protocol-02/integration-inventory.md` (line 32)

**Side-effects:**
- Append to `integration-inventory.md`: "Email: Transactional (SendGrid/Postmark TBD, templates TBD)"

---

### I04: API Rate Limits
**Client:** "What if we hit Salesforce API rate limits?"

**Assistant (expected):** "Good question. Salesforce has daily API limits depending on your plan. We'd need to implement caching and batch requests to stay within limits. What's your Salesforce plan—Professional, Enterprise, or Unlimited?"

**Grounding:** `.artifacts/protocol-02/integration-inventory.md` (lines 69-78), `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 5)

**Side-effects:**
- Append to `integration-inventory.md`: "Salesforce: Rate limit mitigation needed (caching + batching)"
- Append to `risk-opportunity-list.md`: "Integration risk: Salesforce API rate limits"

---

### I05: OAuth Configuration
**Client:** "How do we handle Salesforce OAuth?"

**Assistant (expected):** "We'll set up OAuth 2.0 with Salesforce. You'll need to create a Connected App in Salesforce to get client ID and secret. I can guide you through that, or we can do it together in a session. Have you done OAuth setup before?"

**Grounding:** `.artifacts/protocol-02/integration-inventory.md` (line 75), `.artifacts/protocol-02/question-bank.md` (Q-INT-001)

**Side-effects:**
- Append to `integration-inventory.md`: "Salesforce OAuth: Connected App setup required"
- Create `integration-inventory.md` entry: "OAuth config: Client ID/secret needed"

---

### I06: Third-Party API Credentials
**Client:** "Do we need separate API keys for dev and production?"

**Assistant (expected):** "Yes, definitely. You'll want separate keys for dev, staging, and production. That way you're not testing with live data. Most services like Stripe and SendGrid provide test keys—we'll set those up first."

**Grounding:** `.artifacts/protocol-02/integration-inventory.md` (lines 126-143), `.artifacts/protocol-02/question-bank.md` (Q-INT-001)

**Side-effects:**
- Append to `integration-inventory.md`: "API keys: Separate for dev/staging/prod environments"

---

## COMPLIANCE Bucket

### C01: Data Privacy Requirements
**Client:** "We're handling user data. Any compliance concerns?"

**Assistant (expected):** "Depends on your users and data. If you're in the US only, you're mostly looking at basic privacy policies. If you have EU users, GDPR applies. Are you collecting sensitive data like health info or financial data?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-COMP-001), `.artifacts/protocol-02/integration-inventory.md` (lines 63-67)

**Side-effects:**
- Append to `risk-opportunity-list.md`: "Compliance: Data privacy requirements TBD (GDPR if EU users)"
- Append to `integration-inventory.md`: "Compliance: Privacy policy required, GDPR TBD"

---

### C02: PCI-DSS for Payments
**Client:** "Do we need PCI compliance for Stripe?"

**Assistant (expected):** "If you're using Stripe Elements or Checkout, Stripe handles PCI compliance for you. You just need to follow their integration guidelines. If you're storing card data yourself, that's a different story—but I'd strongly recommend not doing that."

**Grounding:** `.artifacts/protocol-02/integration-inventory.md` (lines 57-61), `.artifacts/protocol-02/question-bank.md` (Q-COMP-001)

**Side-effects:**
- Append to `integration-inventory.md`: "PCI-DSS: Stripe handles compliance (use Elements/Checkout)"

---

## CAPACITY Bucket

### CA01: Weekly Time Commitment
**Client:** "I'm thinking 10-15 hours/week from you."

**Assistant (expected):** "Perfect, that aligns with the proposed 15-hour weekly cap. Should we start at 10 hours and scale up if needed, or go straight to 15?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-BUS-001), `.artifacts/protocol-01/proposal-summary.json` (line 12)

**Side-effects:**
- Upsert `discovery-approval-log.json`: `{"weekly_hours": "10-15", "cap": 15}`

---

### CA02: Communication Format Preference
**Client:** "I prefer async communication over scheduled calls."

**Assistant (expected):** "Async works great. What's your expected response time? I can usually respond within a few hours during weekdays (9am-6pm EST). For deeper architectural reviews, I'd need 24 hours. Does that work?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-COMM-001), `.artifacts/protocol-01/PROPOSAL.md` (line 20)

**Side-effects:**
- Upsert `communication-plan.md`: "Format: Async preferred, response time: few hours (quick), 24hrs (deep)"

---

### CA03: Availability Timezone
**Client:** "I'm in PST. Does your EST availability work?"

**Assistant (expected):** "I'm 9am-6pm EST, which is 6am-3pm PST. If that's too early for you, we can do async or adjust my availability. What times work best for you?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-COMM-002), `.artifacts/protocol-01/PROPOSAL.md` (line 20)

**Side-effects:**
- Append to `communication-plan.md`: "Timezone: PST client, EST mentor (6am-3pm PST overlap)"

---

## AMBIGUITY Bucket

### A01: Product Definition Missing
**Client:** "I need help with architecture and guidance."

**Assistant (expected):** "I'd love to help. To give you relevant guidance, I need to understand what you're building. Can you walk me through your SaaS product? What problem does it solve, and who's it for?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-BUS-005), `.artifacts/protocol-02/assumptions-gaps.md` (lines 72-76)

**Side-effects:**
- Append to `discovery-call-notes.md`: "Product definition: Requested from client (critical gap)"

---

### A02: Vague Tech Stack
**Client:** "We're using modern web stack."

**Assistant (expected):** "Modern web stack covers a lot. Are you using React, Vue, or something else for frontend? And for backend—Node, Python, Go? Understanding your stack helps me provide relevant guidance."

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TECH-001), `.artifacts/protocol-02/assumptions-gaps.md` (lines 45-50)

**Side-effects:**
- Append to `discovery-call-notes.md`: "Tech stack: Vague response, needs clarification"

---

### A03: Unclear MVP Scope
**Client:** "MVP should have everything users need."

**Assistant (expected):** "Let's break that down. What are the must-have features for MVP vs nice-to-haves? If we had to launch in 4 weeks with only 3 features, what would they be?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-003, Q-BUS-005), `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 2)

**Side-effects:**
- Append to `scope-clarification.md`: "MVP scope: Unclear, needs feature prioritization"

---

## CHANGE Bucket

### CH01: Tech Stack Change Mid-Project
**Client:** "We're thinking of switching from Supabase to Firebase."

**Assistant (expected):** "That's a significant change. What's driving the switch? If it's early enough, we can evaluate both. But if you're already deep into Supabase, migration could be costly. Let's talk through the pros/cons."

**Grounding:** `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 5), `.artifacts/protocol-02/question-bank.md` (Q-TECH-001)

**Side-effects:**
- Append to `risk-opportunity-list.md`: "Tech stack change: Supabase → Firebase under consideration"
- Append to `scope-clarification.md`: "Migration: Supabase to Firebase (impact assessment needed)"

---

### CH02: Scope Expansion Request
**Client:** "Can we add mobile app to MVP?"

**Assistant (expected):** "Mobile app is a big add. Are we talking native (iOS/Android) or React Native? And would this push the 4-week timeline, or do we need to de-scope something else to fit it in?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-003), `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 1)

**Side-effects:**
- Append to `scope-clarification.md`: "Scope expansion: Mobile app requested (timeline impact TBD)"
- Append to `risk-opportunity-list.md`: "Scope creep: Mobile app added to MVP"

---

### CH03: Timeline Extension Request
**Client:** "Can we extend MVP timeline to 8 weeks?"

**Assistant (expected):** "Sure, 8 weeks gives us more breathing room. Does that mean we're adding features, or just want more time for the original scope? Either way, we can adjust the plan."

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-001), `.artifacts/protocol-02/risk-opportunity-list.md` (Risk 6)

**Side-effects:**
- Upsert `timeline-discussion.md`: "MVP timeline: Extended to 8 weeks (reason TBD)"

---

## APPROVALS Bucket

### AP01: Pricing Approval
**Client:** "The pricing looks good. Let's move forward."

**Assistant (expected):** "Great! I'll send over a recap with next steps. When would you like to officially start?"

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-BUS-002), `.artifacts/protocol-01/proposal-summary.json` (lines 8-14)

**Side-effects:**
- Upsert `discovery-approval-log.json`: `{"pricing_approved": true, "status": "ready_to_start"}`

---

### AP02: Scope Approval
**Client:** "The MVP scope we discussed sounds perfect."

**Assistant (expected):** "Awesome. I'll document that in the recap: auth, dashboard, Salesforce integration (one-way). If anything changes, we can adjust as we go."

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-003), `.artifacts/protocol-02/call-agenda.md` (lines 154-169)

**Side-effects:**
- Upsert `client-discovery-form.md`: "MVP scope approved: auth + dashboard + Salesforce one-way"
- Upsert `discovery-approval-log.json`: `{"scope_approved": true}`

---

### AP03: Timeline Approval
**Client:** "4-week MVP timeline works for us."

**Assistant (expected):** "Perfect. We'll target 4 weeks for MVP. I'll break that down into milestones in the recap so we can track progress."

**Grounding:** `.artifacts/protocol-02/question-bank.md` (Q-TIME-001), `.artifacts/protocol-02/call-agenda.md` (lines 131-150)

**Side-effects:**
- Upsert `timeline-discussion.md`: "MVP timeline approved: 4 weeks"
- Upsert `discovery-approval-log.json`: `{"timeline_approved": true, "mvp_weeks": 4}`

---

## Coverage Summary

**Total Tests:** 27
**Per Bucket:** Timeline (3), Scope (3), Pricing (3), Integration (6), Compliance (2), Capacity (3), Ambiguity (3), Change (3), Approvals (3)

**Artifacts Used:**
- `.artifacts/protocol-01/PROPOSAL.md`
- `.artifacts/protocol-01/proposal-summary.json`
- `.artifacts/protocol-01/pricing-analysis.json`
- `.artifacts/protocol-02/discovery-brief.md`
- `.artifacts/protocol-02/assumptions-gaps.md`
- `.artifacts/protocol-02/question-bank.md`
- `.artifacts/protocol-02/integration-inventory.md`
- `.artifacts/protocol-02/call-agenda.md`
- `.artifacts/protocol-02/risk-opportunity-list.md`
