# Docusaurus + ChatKit Development Rule Book
## Stability-First SDD Approach for Error-Free Development

### 🧠 THE FOUNDATION PRINCIPLE
**If the foundation is shaky, SDD becomes noise. If the foundation is solid, SDD becomes power.**

---

## 🏗️ LEVEL 0 — Environment Lock (Non-Negotiable)

### Goal: Ensure tooling is deterministic.

### Actions Required:
- Lock versions:
  - Node.js (exact version)
  - npm / pnpm
  - Docusaurus version
  - React version
  - Python version (for backend)
  - FastAPI version

- Create version lock files:
  - `.nvmrc` for Node.js
  - `package-lock.json` with exact versions
  - `requirements.txt` with pinned versions
  - `engines` block in package.json

### Verification Gates:
- `npx create-docusaurus@latest` works without errors
- `npm start` renders default site
- `npm run build` succeeds
- Python virtual environment activates properly
- Backend server starts with `uvicorn main:app --reload`

### ❌ STOP RULES:
- Do NOT write SDD specs until environment is locked
- Do NOT integrate ChatKit until baseline works
- Do NOT use AI until environment is stable
- Do NOT proceed if any verification fails

---

## 🧱 LEVEL 1 — Baseline Contract (Hello World Gate)

### Goal: Prove the framework works without customization.

### Required Gates (All Must Pass):
1. Default Docusaurus site loads without errors
2. One custom page renders text only (no complex components)
3. One React component renders static JSX
4. Hot reload works in development
5. Build command succeeds (`npm run build`)
6. Backend server responds to health check (`/health` endpoint)
7. Basic API endpoint returns expected response

### Validation Rule:
- If any gate fails → fix manually, no AI tools
- This becomes your golden baseline for all future development

---

## 📜 LEVEL 2 — SDD Starts Here (Primitive Specs Only)

### Goal: Build specifications for primitives, not features.

### Valid Early Specs (Examples):
- "Render a static Chat panel container"
- "Render a message bubble with mock text"
- "Render a send button"
- "Render a message input field"
- "Render a loading spinner"
- "Render an error message container"

### ❌ Invalid Early Specs:
- Real chat functionality
- RAG integration
- API calls
- Authentication
- Complex state machines
- Vector database integration

### SDD Rules:
- Each primitive spec must touch only one file
- Each spec must produce visible output
- Each spec must be reversible
- Each spec must have a clear acceptance criterion

---

## 🧩 LEVEL 3 — Module Isolation (No Integration Yet)

### Goal: Build modules in isolation with zero dependencies.

### Module Structure:
- **Chat UI Module**: Chat interface, message display, input handling
- **API Client Module**: API communication, error handling, retry logic
- **State Management Module**: Message history, loading states, errors
- **UI Components Module**: Buttons, inputs, styling, animations

### Isolation Requirements:
- Each module has separate SDD spec
- Each module has separate route/page for testing
- Each module uses mock data only
- Zero cross-module dependencies allowed
- Each module must work independently

### Integration Rule:
- No module may import another module until all modules pass isolation tests
- Each module must be testable in isolation

---

## 🔌 LEVEL 4 — Mock Integration Gate

### Goal: Prove components work together with mock data before real APIs.

### Mock Integration Requirements:
- Chat UI works with mock messages (hardcoded)
- API client returns mock responses
- Error handling works with mock errors
- Loading states work with mock delays
- Components render independently with mock data

### ❌ No Real Dependencies Allowed:
- No real backend server
- No real API calls to external services
- No real authentication
- No real vector database
- No real Cohere API calls

### Success Criteria:
- This eliminates 70% of integration bugs
- All UI components render correctly with mock data
- Error states are properly handled
- Loading states work as expected

---

## 🔗 LEVEL 5 — Single Integration at a Time

### Goal: Integrate systems one at a time with proper validation.

### Integration Order (Recommended):
1. Chat UI → fake API (mock endpoints)
2. Chat UI → real backend API
3. RAG service → vector store
4. Authentication → login system
5. Real-time features → WebSocket connections

### Integration Rules:
- Never integrate two systems simultaneously
- Every integration has its own SDD spec
- Every integration has its own test
- Every integration has its own rollback plan
- Each integration must pass all previous tests

### Validation Gates:
- Before integrating next system, ensure current integration works perfectly
- Document integration points and dependencies
- Create integration tests for each connection

---

## 🧪 LEVEL 6 — Failure-Driven Testing (Before Features)

### Testing Requirements (Mandatory):
- **Render Test**: One per component (ensures component renders without errors)
- **Interaction Test**: One per module (ensures user interactions work)
- **Contract Test**: One per integration (ensures API contracts are met)
- **Error Test**: One per error scenario (ensures error handling works)
- **Performance Test**: One per critical path (ensures acceptable performance)

### Testing Rules:
- Testing is not after development — it's during development
- If any test fails → stop and fix immediately
- No integration without passing tests
- All tests must be automated and repeatable

---

## 🔁 LEVEL 7 — AI Usage Discipline (Critical)

### When to Use AI (✅ Allowed):
- When baseline environment is stable
- When scope is one file or one function
- When output is a specific patch
- When you know the expected result
- When fixing isolated, well-defined problems

### When NOT to Use AI (❌ Forbidden):
- Ask AI to "fix everything" at once
- Ask AI to "make it work" without clear specs
- Allow AI to refactor entire folders
- Allow AI to integrate multiple systems automatically
- Use AI when baseline is unstable

### AI Discipline Rules:
- Always verify AI output manually
- Test AI-generated code immediately
- Keep AI changes small and focused
- Document AI-assisted changes for review

---

## 🚦 THE GOLDEN RULES (Print & Follow)

### Rule 1: Expected Output Clarity
**If you cannot explain the expected output in one sentence, you are not ready to code.**

### Rule 2: Gate Progression
**Never skip a level. If Level N fails, you cannot proceed to Level N+1.**

### Rule 3: Isolation First
**Prove it works in isolation before proving it works integrated.**

### Rule 4: One Change at a Time
**Only change one variable at a time during debugging.**

### Rule 5: Immediate Fix
**If something breaks, fix it immediately before continuing.**

---

## 🧰 Daily Workflow (Follow Exactly)

1. **Run baseline build** (`npm run build` && backend health check)
2. **Pick one isolated spec** from your SDD plan
3. **Implement one primitive** component or function
4. **Test manually** and run automated tests
5. **Commit** with clear, descriptive message
6. **Only then proceed** to next task

---

## 🚨 Common Failure Patterns to Avoid

### Pattern 1: Environment Uncertainty
- **Problem**: Different Node.js versions across team
- **Solution**: Use `.nvmrc` and enforce in CI

### Pattern 2: Premature Integration
- **Problem**: Trying to connect everything at once
- **Solution**: Follow single integration rule

### Pattern 3: Skipping Baseline
- **Problem**: Starting with customizations
- **Solution**: Always start with working baseline

### Pattern 4: AI Before Stability
- **Problem**: Using AI when environment is unstable
- **Solution**: Lock environment first, then use AI

### Pattern 5: No Mock Data Strategy
- **Problem**: Trying to connect to real services immediately
- **Solution**: Prove with mocks before real connections

---

## 🎯 Success Metrics

### Development Speed Indicators:
- Baseline environment setup: < 30 minutes
- New component creation: < 1 hour (with tests)
- Integration: < 2 hours per system
- Bug fixes: < 30 minutes
- Full build and test: < 5 minutes

### Quality Indicators:
- Zero "Hello World" failures
- < 5% integration bugs
- < 1% regression bugs
- < 10 minutes to identify and fix issues
- 95%+ test coverage on critical paths

---

## 🔄 Troubleshooting Quick Reference

### When "Hello World" Fails:
1. Check environment versions (Node, npm, Python)
2. Verify baseline Docusaurus works
3. Check dependency installation
4. Review configuration files

### When Integration Fails:
1. Verify single system works in isolation
2. Check API endpoint availability
3. Validate data format contracts
4. Review error logs

### When AI Suggestions Don't Work:
1. Verify baseline environment
2. Check if scope is too broad
3. Validate expected output is clear
4. Test with smaller, focused changes

This rule book provides the systematic approach needed to minimize troubleshooting overhead and build solid, synchronized modules that work error-free.