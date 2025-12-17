<!--
SYNC IMPACT REPORT
Version change: N/A (initial creation) → 1.0.0 (new constitution)
List of modified principles: N/A (initial creation) → Added 6 core principles
Added sections: Core Principles (Security First, Source of Truth, Modularity, RAG Protocol Compliance, Testing Excellence, Naming Conventions), Technical Standards, Development Workflow, Governance
Removed sections: N/A (initial creation)
Templates requiring updates: ✅ plan-template.md (Constitution Check section will now reference new principles), ✅ spec-template.md (requirements alignment), ✅ tasks-template.md (task categorization)
Follow-up TODOs: None
-->

# AIBOOK Constitution

## Core Principles

### Security First
No hardcoded credentials; all secrets must be managed via environment variables (e.g., .env files). Security is the top priority in all implementations and deployments.

### Source of Truth
Deployed Docusaurus content serves as the single source of truth for RAG (Retrieval Augmented Generation) knowledge. All AI responses must be grounded in this verified content.

### Modularity
Separate Python files must be maintained for FastAPI, Cohere, Qdrant, and Agent logic. Each component should be modular, well-defined, and independently testable.

### RAG Protocol Compliance
LLM responses must be strictly grounded in retrieved book context. No hallucinations or responses outside the provided document corpus are acceptable.

### Testing Excellence
Minimum 80% test coverage is required for all RAG and API modules. Comprehensive testing ensures reliability and correctness of the system.

### Naming Conventions
React components use PascalCase. Python functions use snake_case and must include type hints for improved maintainability and clarity.

## Technical Standards

### Stack Requirements
Technology stack: Docusaurus (Frontend), FastAPI (Backend), OpenAI Agent SDK, ChatKit SDK. All implementations must align with these core technologies.

### Deployment Constraints
Frontend must deploy to GitHub Pages/Vercel. Backend must be designed for Vercel/Railway deployment using FastAPI. All deployment configurations must follow these platforms' requirements.

### Vector Database and Embeddings
Embedding generation must use Cohere for all vector generation. Vector storage must use Qdrant Cloud for the vector database. These technologies are non-negotiable for consistency and performance.

## Development Workflow

### Code Quality Standards
All Python functions must include type hints. React components must follow PascalCase naming. Code reviews must verify compliance with all constitutional principles. Complexity must be justified with clear documentation.

### Review and Approval Process
All pull requests and code reviews must verify constitutional compliance. Changes to core components require explicit approval from designated maintainers. Breaking changes must include migration plans and justification.

## Governance

All development practices must comply with this constitution. Amendments require formal documentation, team approval, and migration planning. This constitution supersedes all other development practices. All PRs and reviews must verify compliance with these principles. Use project documentation for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-12-15 | **Last Amended**: 2025-12-15