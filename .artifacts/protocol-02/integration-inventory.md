---
status: draft
last_updated: 2025-01-27
prepared_by: Protocol 02 AI Assistant
---

# Integration & Dependency Inventory

**Purpose:** System and dependency overview with access requirements and risk flags

---

## Status Legend
- `@ASK_CLIENT` - Must ask client during discovery call
- `confirmed` - Validated with client
- `research` - Can research independently
- `pending` - Awaiting follow-up

---

## System Inventory

| System | Purpose | Owner | Data Availability | Access Status | Risk Level | Next Action | Question ID |
|--------|---------|-------|-------------------|---------------|------------|-------------|-------------|
| **Product Codebase** | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | Q-TECH-004 | Q-BUS-005 |
| **Git Repository** | Version control | @ASK_CLIENT | N/A | @ASK_CLIENT | LOW | Q-TECH-004 | Q-COMM-003 |
| **Supabase** | Backend/database | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | MEDIUM | Q-TECH-001 | Q-INT-002 |
| **Postgres Database** | Data storage | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | HIGH | Q-TECH-001 | Q-INT-002 |
| **Next.js Frontend** | User interface | @ASK_CLIENT | N/A | @ASK_CLIENT | LOW | Q-TECH-001 | Q-TECH-004 |
| **Node.js Backend** | API/server logic | @ASK_CLIENT | N/A | @ASK_CLIENT | MEDIUM | Q-TECH-001 | Q-TECH-004 |
| **Payment Processor** | Payment handling | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | HIGH | Q-INT-001 | Q-COMP-001 |
| **Email Service** | Email delivery | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | MEDIUM | Q-INT-001 | Q-INT-002 |
| **Analytics Platform** | User analytics | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | LOW | Q-INT-001 | Q-INT-002 |
| **AI/LLM APIs** | AI features | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | MEDIUM | Q-TECH-002 | Q-INT-002 |
| **Zapier/n8n** | Automation workflows | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | MEDIUM | Q-TECH-003 | Q-INT-002 |
| **CI/CD Pipeline** | Deployment automation | @ASK_CLIENT | N/A | @ASK_CLIENT | MEDIUM | Q-TECH-001 | Q-TECH-004 |
| **Hosting/Infrastructure** | Production hosting | @ASK_CLIENT | N/A | @ASK_CLIENT | HIGH | Q-TECH-001 | Q-TIME-003 |

---

## Dependency Mapping

### Critical Dependencies (Must Know)

1. **Database → Application**
   - **Dependency:** Application depends on database schema and data structure
   - **Risk:** HIGH - Schema changes can break application
   - **Action:** @ASK_CLIENT about current schema and migration strategy
   - **Question:** Q-TECH-001, Q-TECH-004

2. **Frontend → Backend API**
   - **Dependency:** Frontend depends on backend API endpoints
   - **Risk:** MEDIUM - API changes break frontend
   - **Action:** @ASK_CLIENT about API structure and versioning strategy
   - **Question:** Q-TECH-001, Q-TECH-004

3. **Payment Processing → Compliance**
   - **Dependency:** Payment processing requires compliance (PCI-DSS)
   - **Risk:** HIGH - Non-compliance has legal/financial consequences
   - **Action:** @ASK_CLIENT about compliance requirements
   - **Question:** Q-INT-001, Q-COMP-001

4. **AI Integrations → Data Privacy**
   - **Dependency:** AI/LLM integrations may process user data
   - **Risk:** MEDIUM - Data privacy concerns
   - **Action:** @ASK_CLIENT about data handling and privacy policies
   - **Question:** Q-TECH-002, Q-COMP-001

### Integration Requirements

| Integration Type | Required | Owner | Access Needed | Risk | Question ID |
|------------------|----------|-------|---------------|------|-------------|
| Payment Gateway | @ASK_CLIENT | @ASK_CLIENT | API keys | HIGH | Q-INT-001 |
| Email Service | @ASK_CLIENT | @ASK_CLIENT | API keys | MEDIUM | Q-INT-001 |
| Authentication Provider | @ASK_CLIENT | @ASK_CLIENT | OAuth config | HIGH | Q-INT-001 |
| Third-Party APIs | @ASK_CLIENT | @ASK_CLIENT | API keys | MEDIUM | Q-INT-001 |
| Analytics Services | @ASK_CLIENT | @ASK_CLIENT | API keys | LOW | Q-INT-001 |

---

## Data Ownership & Access

### Data Sources

| Data Source | Owner | Availability | Access Method | Compliance | Question ID |
|------------|-------|--------------|---------------|------------|-------------|
| User Data | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | Q-INT-002 |
| Business Data | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | Q-INT-002 |
| Third-Party Data | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | @ASK_CLIENT | Q-INT-002 |

---

## Risk Assessment

### High Risk Items (Address First)

1. **Database Access & Schema**
   - **Risk:** Database schema changes can break application
   - **Mitigation:** Establish schema review process before changes
   - **Question:** Q-TECH-001, Q-TECH-004

2. **Payment Processing**
   - **Risk:** Security and compliance requirements
   - **Mitigation:** Validate compliance strategy and security practices
   - **Question:** Q-INT-001, Q-COMP-001

3. **Production Infrastructure**
   - **Risk:** Deployment and hosting decisions affect scalability
   - **Mitigation:** Review hosting strategy and scaling plans
   - **Question:** Q-TECH-001, Q-TIME-003

### Medium Risk Items

4. **API Integrations**
   - **Risk:** API changes can break integrations
   - **Mitigation:** Establish integration testing and monitoring
   - **Question:** Q-INT-001

5. **Authentication & Authorization**
   - **Risk:** Security vulnerabilities
   - **Mitigation:** Review authentication architecture
   - **Question:** Q-TECH-001, Q-COMP-001

---

## Access Requirements

### Repository Access
- **Required:** @ASK_CLIENT
- **Level:** Read-only, Read-write, or Admin
- **Question:** Q-TECH-004, Q-COMM-003

### Environment Access
- **Development:** @ASK_CLIENT
- **Staging:** @ASK_CLIENT
- **Production:** @ASK_CLIENT
- **Question:** Q-TECH-001, Q-TECH-004

### Service Account Access
- **Supabase:** @ASK_CLIENT
- **Hosting Platform:** @ASK_CLIENT
- **CI/CD:** @ASK_CLIENT
- **Question:** Q-TECH-001, Q-TECH-004

---

## Pre-Call Research Items

### Can Research Independently
- [ ] Supabase best practices and common patterns
- [ ] Next.js architecture patterns
- [ ] Postgres schema design patterns
- [ ] Node.js backend architecture patterns
- [ ] Payment processing compliance (general guidance)

---

## Post-Call Update Checklist

- [ ] All `@ASK_CLIENT` tags resolved
- [ ] System owners identified
- [ ] Access requirements documented
- [ ] Risk levels validated
- [ ] Integration dependencies mapped
- [ ] Data ownership clarified
- [ ] Compliance requirements identified

---

## Validation

- [x] Table covers System, Purpose, Owner, Data Availability, Risk, Next Action
- [x] All `@ASK_CLIENT` tags linked to question IDs
- [x] Risk levels assigned (HIGH/MEDIUM/LOW)
- [x] Integration requirements documented
- [x] Data ownership section included

