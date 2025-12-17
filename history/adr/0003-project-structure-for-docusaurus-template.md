# ADR-0003: Project Structure for Docusaurus Template

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-18
- **Feature:** 003-docusaurus-tailwind-daisyui
- **Context:** Need to establish a standardized project structure for the Docusaurus v3 template with TailwindCSS and DaisyUI integration. The structure must follow Docusaurus conventions while accommodating custom components, CSS files, and static assets. It should support both documentation and blog content, be deployable to standard hosting platforms, and maintain modularity for easy customization by template users.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- Directory: frontend/ (root directory for the Docusaurus project)
- Components: src/components/ (modular React components like Navbar, Footer)
- CSS: src/css/ (custom CSS with Tailwind imports and additional styles)
- Pages: src/pages/ (React pages including index.js homepage)
- Documentation: docs/ (MDX documentation files)
- Blog: blog/ (MDX blog posts)
- Static Assets: static/img/ (logo, placeholder images)
- Configuration: docusaurus.config.js, tailwind.config.js, postcss.config.js, sidebars.js
- Package Management: package.json with all dependencies and scripts
- Documentation: README.md with setup and customization instructions

## Consequences

### Positive

- Follows standard Docusaurus project organization, making it familiar to developers
- Clear separation of concerns with dedicated directories for components, pages, and assets
- Easy to maintain and extend with modular component architecture
- Compatible with Docusaurus conventions and plugin ecosystem
- Supports both documentation and blog content in standard locations
- Deployable to common hosting platforms like GitHub Pages, Vercel, Netlify
- Maintains modularity allowing for easy customization of the template

### Negative

- Additional directory nesting may be more complex than minimal setups
- Requires understanding of Docusaurus conventions for customization
- May need to adjust existing Docusaurus projects to match this structure
- Some developers may prefer different organization patterns
- Additional configuration files to maintain

## Alternatives Considered

Alternative Structure A: Flat directory structure with all files in root
- Directory: All files in project root without frontend/ subdirectory
- Components: components/ at root level
- Why rejected: Would conflict with Docusaurus conventions and make integration harder

Alternative Structure B: Monorepo with separate packages for frontend/backend
- Directory: packages/frontend/ for Docusaurus project
- Components: packages/frontend/src/components/
- Why rejected: Overly complex for a documentation template that doesn't need backend services

Alternative Structure C: Next.js app directory structure
- Directory: app/ instead of src/pages/
- Components: app/components/
- Why rejected: Doesn't align with Docusaurus framework requirements, which uses pages/ directory

## References

- Feature Spec: specs/003-docusaurus-tailwind-daisyui/spec.md
- Implementation Plan: specs/003-docusaurus-tailwind-daisyui/plan.md
- Related ADRs: ADR-0001 (Docusaurus Framework Selection), ADR-0002 (Frontend Technology Stack)
- Evaluator Evidence: specs/003-docusaurus-tailwind-daisyui/research.md
