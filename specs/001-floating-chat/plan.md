# Implementation Plan: Global Floating Chat UI with Local Context Awareness

**Branch**: `001-floating-chat` | **Date**: 2025-12-18 | **Spec**: [link]
**Input**: Feature specification from `/specs/001-floating-chat/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a global floating Chat UI component with local context awareness for the Docusaurus site. The component is UI-only (no backend integration) with mocked messages, able to open/close, and display local context including current page title/route and any selected text. The chat UI is integrated at the global layout level using Docusaurus theme customization. Based on research, the implementation will use React components with Context API for state management, following Docusaurus conventions and project constitution requirements.

## Technical Context

**Language/Version**: JavaScript/TypeScript (React 18.x) - Required by Docusaurus framework and project constitution
**Primary Dependencies**: React, Docusaurus, ChatKit SDK, TailwindCSS, DaisyUI - Aligned with project constitution stack
**Storage**: N/A - UI-only implementation with no persistent storage requirements
**Testing**: Jest, React Testing Library - Standard for React component testing
**Target Platform**: Web browsers (Chrome, Firefox, Safari, Edge) - Docusaurus site compatibility
**Project Type**: Web/frontend - Single UI component for Docusaurus site
**Performance Goals**: <100ms for UI interactions, <500ms for text selection detection, minimal impact on page load time
**Constraints**: Must not interfere with existing page functionality, must follow Docusaurus styling guidelines
**Scale/Scope**: Single floating chat component, global site availability, no backend integration required

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Compliance Verification

**Security First**: ✅ N/A - UI-only component with no secrets or credentials required

**Source of Truth**: ✅ N/A - No backend functionality, no data storage

**Modularity**: ✅ Component will be modular React component with clear interfaces

**RAG Protocol Compliance**: ✅ N/A - No LLM integration in this UI-only component

**Testing Excellence**: ✅ Component will include unit and integration tests to ensure reliability

**Naming Conventions**: ✅ React component will follow PascalCase naming as required by constitution

**Technical Standards**: ✅ Implementation will use React (as part of Docusaurus) and follow project stack requirements

### Gates Status
All constitutional principles are satisfied or not applicable for this UI-only component. No violations detected.

## Project Structure

### Documentation (this feature)

```text
specs/001-floating-chat/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

frontend/
├── src/
│   ├── components/
│   │   └── FloatingChat/
│   │       ├── FloatingChat.tsx
│   │       ├── FloatingChatContext.tsx
│   │       ├── FloatingChatButton.tsx
│   │       ├── ChatWindow.tsx
│   │       ├── MessageList.tsx
│   │       └── MessageInput.tsx
│   ├── hooks/
│   │   └── useTextSelection.ts
│   └── styles/
│       └── floating-chat.css
└── tests/
    └── components/
        └── FloatingChat/
            ├── FloatingChat.test.tsx
            └── FloatingChatContext.test.tsx

### Source Code (Docusaurus structure)

src/
├── components/
│   └── FloatingChat/
│       └── index.js              # Main entry point for Docusaurus integration
├── css/
│   └── custom.css               # Custom styles for floating chat
└── theme/
    └── Root.js                  # Global wrapper to integrate floating chat
```

**Structure Decision**: The floating chat component will be implemented as a React component following Docusaurus conventions. The component will be integrated at the global layout level through the Root theme component. The structure follows the web application pattern with components organized in a modular fashion.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
