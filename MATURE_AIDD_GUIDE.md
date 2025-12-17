# Mature AIDD: Fool-Resistant SDD System

This project implements a mature, production-grade AIDD (AI-Driven Development) architecture that addresses the common problems of debugging hell, integration failures, and chaotic development in SDD projects.

## Problem Statement

Traditional SDD approaches suffer from:
- Generated code has many issues
- Debugging takes too long
- Bug fixes introduce new build failures
- Frustration and loss of confidence
- "Hello world" sometimes breaks
- Integration destabilizes working parts

These are not coding problems but systemic failures of isolation, controlled evolution, and governance automation.

## Solution: Four Governance Layers

```
┌──────────────────────────┐
│   Constitution Layer     │  (Law - Executable Governance)
├──────────────────────────┤
│   Epoch Governance       │  (Permissions - Controlled Access)
├──────────────────────────┤
│   Primitive Isolation    │  (Execution Units - Bounded Context)
├──────────────────────────┤
│   Implementation Code    │  (Disposable - Replaceable)
└──────────────────────────┘
```

### 1. Constitution Layer (Law)
- **Purpose**: Executable governance that defines what is permitted
- **Tools**: `.specify/scripts/constitution-validator.py`
- **Function**: Validates every AI action against constitutional rules

### 2. Epoch Governance (Permissions)
- **Purpose**: Permission envelopes that control what can be modified
- **Tools**: `.specify/scripts/epoch-creator.py`
- **Epochs**:
  - Epoch 1: Frontend Stability Epoch
  - Epoch 2: Backend Contract Epoch
  - Epoch 3: Auth Isolation Epoch
  - Epoch 4: RAG/Intelligence Epoch
  - Epoch 5: Integration & Hardening Epoch

### 3. Primitive Isolation (Execution Units)
- **Purpose**: Bounded contexts with enforced boundaries
- **Tools**: `.specify/scripts/primitive-validator.py`
- **Rules**: Primitives are sacred (never modified after acceptance), modules are disposable

### 4. Implementation Code (Disposable)
- **Purpose**: The actual code that can be replaced without affecting system integrity
- **Characteristics**: Replaceable, follows patterns defined by higher layers

## Key Scripts and Tools

### Constitution Validator
```bash
.specify/scripts/constitution-validator.py write backend/main.py "Adding new endpoint"
```
Validates actions against constitutional rules and current epoch permissions.

### Epoch Creator
```bash
.specify/scripts/epoch-creator.py create --name "Backend_Contract_Epoch" --goal "Define API contracts" --allowed-actions "define,create,mock" --forbidden-actions "connect,live,integrate"
```
Creates and manages development epochs with proper governance controls.

### Primitive Validator
```bash
.specify/scripts/primitive-validator.py primitives/auth/
```
Validates primitives against isolation rules to prevent cross-contamination.

### Constitution Evolver
```bash
.specify/scripts/constitution-evolver.py propose --title "Add Security Requirement" --description "New security requirement" --add-section "Security" "All APIs must use OAuth2"
```
Manages controlled evolution of the constitution with proper validation.

## How This Eliminates Debugging Hell

| Problem | Why It Disappears |
|---------|------------------|
| Endless debugging | Bugs cannot cross epoch boundaries |
| Fix breaks other parts | Isolation law prevents cross-contamination |
| Build failures | Gate law + exit conditions enforce stability |
| AI chaos | Permission envelope controls all actions |
| Integration mess | Integration epoch only |
| Rewrites | Primitive immutability prevents patching |

## Bug Handling in Mature AIDD

1. Bug detected
2. Identify violated law
3. Roll back to last valid primitive
4. Replace primitive (don't patch)
5. Re-run validation gate

## Controlled Evolution Strategy

- **Constitution**: Rarely (only fundamental law changes)
- **Epoch Amendments**: Occasionally (permission boundary changes)
- **Primitives**: Frequently (within isolation rules)
- **Code**: Disposable (replaceable at will)

## Getting Started

1. **Validate current state**:
   ```bash
   .specify/scripts/constitution-validator.py read . "Initial validation"
   ```

2. **Check current epoch**:
   ```bash
   cat .specify/current-epoch.json
   ```

3. **List available epochs**:
   ```bash
   .specify/scripts/epoch-creator.py list
   ```

4. **Validate primitives**:
   ```bash
   .specify/scripts/primitive-validator.py primitives/
   ```

## Best Practices

1. **Always validate before acting**:
   Use the constitution validator for every action

2. **Respect epoch boundaries**:
   Only perform allowed actions in current epoch

3. **Maintain primitive isolation**:
   Never modify primitives after acceptance

4. **Replace, don't patch**:
   If a primitive is broken, create a new one

5. **Evolve constitution deliberately**:
   Use the constitution evolver for changes

## Architecture Decision

📋 Architectural decision detected: Mature AIDD Governance Architecture - Document reasoning and tradeoffs? Run `/sp.adr Mature-AIDD-Governance-Architecture`.

This system transforms SDD from a chaotic process into a fool-resistant system where bugs cannot propagate and development follows predictable, isolated phases.