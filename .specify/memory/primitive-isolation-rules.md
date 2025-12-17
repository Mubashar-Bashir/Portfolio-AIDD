# Primitive & Module Isolation Rules

This document defines the isolation rules that ensure system stability and prevent cross-contamination between development phases.

## Core Principles

### Modules vs Primitives
- **Primitives are sacred**: Never modified after acceptance, isolated, testable alone
- **Modules are disposable**: Group primitives, may be rewritten, may fail safely

### Isolation Rules

#### Primitive Isolation Rules
Each primitive must:
1. Have no external dependency (except core libraries defined in constitution)
2. Be testable in isolation (unit tests pass without integration)
3. Never be modified after acceptance (replace, don't patch)
4. Have clear, documented interfaces
5. Be versioned independently
6. Have comprehensive test coverage (minimum 90%)

#### Module Isolation Rules
Modules may:
1. Group multiple primitives together
2. Be rewritten when needed
3. Be replaced entirely
4. Fail without affecting other modules
5. Have looser coupling between primitives

#### Forbidden Cross-Dependencies
- Primitives cannot depend on other primitives directly (use interfaces/adapters)
- Frontend primitives cannot access backend resources
- Authentication primitives cannot access business logic
- RAG primitives cannot access UI components

## Implementation Guidelines

### Creating New Primitives
1. Define interface first
2. Implement with no external dependencies
3. Write comprehensive unit tests
4. Get approval before integration
5. Never modify after acceptance - create new version instead

### Creating New Modules
1. Compose from existing primitives
2. Define clear boundaries
3. Implement error handling
4. Ensure failure isolation
5. Document dependencies

## Validation Checks

### Pre-Commit Validation
Before any code change, validate:
- [ ] No primitive modification (except during primitive creation)
- [ ] Proper isolation boundaries maintained
- [ ] No forbidden dependencies
- [ ] Tests pass in isolation
- [ ] Current epoch permissions respected

### Continuous Integration Validation
- [ ] Primitive immutability check
- [ ] Dependency isolation validation
- [ ] Cross-boundary violation detection
- [ ] Test coverage verification

## Violation Handling

When isolation rules are violated:
1. Identify the specific rule broken
2. Roll back to last valid state
3. Document the violation
4. Update rules if necessary
5. Re-run validation

## Examples

### Good Primitive Structure
```
primitives/
├── auth/
│   ├── login_primitive.py
│   ├── token_handler.py
│   └── tests/
├── rag/
│   ├── embedding_primitive.py
│   ├── retrieval_primitive.py
│   └── tests/
└── ui/
    ├── button_primitive.js
    ├── form_primitive.js
    └── tests/
```

### Good Module Structure
```
modules/
├── user_management/
│   ├── primitives_used: [auth_primitives, ui_primitives]
│   └── integration_logic.py
├── document_search/
│   ├── primitives_used: [rag_primitives, auth_primitives]
│   └── integration_logic.py
└── frontend_shell/
    ├── primitives_used: [ui_primitives, auth_primitives]
    └── layout_logic.js
```

This structure ensures complete isolation while allowing controlled composition.