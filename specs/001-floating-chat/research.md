# Research: Global Floating Chat UI with Local Context Awareness

## Decision: Component Architecture
**Rationale**: Using a React-based floating chat component with Docusaurus integration allows for global availability across all pages while maintaining compatibility with the existing tech stack.
**Alternatives considered**:
- Standalone JavaScript widget (would require more DOM manipulation)
- iframe-based solution (would complicate context detection)
- Native Docusaurus plugin (would be overkill for UI-only component)

## Decision: Global Layout Integration
**Rationale**: Implementing the chat at the global layout level using a layout wrapper ensures consistent availability across all pages without requiring modifications to individual page components.
**Alternatives considered**:
- Adding to each page individually (high maintenance, inconsistent)
- Using Docusaurus swizzling (unnecessary complexity for this feature)
- Injecting via script (would complicate context detection)

## Decision: Context Detection Approach
**Rationale**: Using React hooks for page context and selected text detection provides a clean, reactive approach that integrates well with the React lifecycle.
**Alternatives considered**:
- Global event listeners (could cause memory leaks)
- Direct DOM manipulation (less maintainable)
- External libraries for text selection (additional dependencies)

## Decision: Mock Data Strategy
**Rationale**: Using a mock service for chat messages provides a realistic UI experience without requiring backend integration, meeting the "UI-only" requirement from the specification.
**Alternatives considered**:
- Hardcoded messages (less flexible)
- JSON files (unnecessary complexity)
- External mock API (overkill for UI-only requirement)

## Decision: Styling Approach
**Rationale**: Using TailwindCSS with DaisyUI components ensures consistency with the existing design system while providing pre-styled components for rapid development.
**Alternatives considered**:
- Custom CSS (inconsistent with project standards)
- CSS modules (unnecessary for this scope)
- Styled-components (additional dependency not needed)