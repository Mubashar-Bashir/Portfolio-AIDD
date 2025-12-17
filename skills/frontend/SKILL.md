---
name: frontend
description: Modern frontend development with React, TypeScript, and framework integration. Use when Claude needs to work with frontend applications for: (1) Creating React components, (2) Implementing TypeScript patterns, (3) Integrating with frameworks like Docusaurus, (4) Managing state and side effects, (5) Optimizing performance and accessibility
---

# Frontend Development Skill

## Purpose
This skill provides comprehensive support for modern frontend development using React, TypeScript, and related technologies. It focuses on creating maintainable, performant, and accessible user interfaces.

## When to Use This Skill
- Creating new React components with proper TypeScript typing
- Implementing state management solutions
- Integrating with documentation frameworks like Docusaurus
- Optimizing frontend performance
- Ensuring accessibility compliance
- Implementing responsive design patterns

## Core Capabilities

### Component Development
- Create functional components with TypeScript interfaces
- Implement proper prop validation and default values
- Use React hooks appropriately (useState, useEffect, etc.)
- Follow component composition patterns

### State Management
- Implement local state with useState/useReducer
- Integrate global state management (Context API, Redux, etc.)
- Manage side effects properly with useEffect
- Handle async operations with proper error handling

### Performance Optimization
- Implement code splitting with React.lazy
- Use React.memo for component optimization
- Apply proper key props for lists
- Optimize bundle size and loading times

### Integration Patterns
- Connect with external APIs and services
- Integrate with documentation frameworks (Docusaurus)
- Implement proper error boundaries
- Handle form submissions and validation

## Key Patterns and Conventions

### TypeScript Interfaces
```typescript
interface ComponentProps {
  requiredProp: string;
  optionalProp?: number;
  callback?: (value: string) => void;
}
```

### React Hooks Best Practices
- Follow the Rules of Hooks
- Extract custom hooks for complex logic
- Use useCallback/useMemo appropriately

### File Structure
- Organize components by feature or type
- Use index files for clean imports
- Separate components, hooks, and utilities

## Best Practices
- Use PascalCase for component names
- Implement proper TypeScript typing
- Follow accessibility guidelines (ARIA, semantic HTML)
- Write comprehensive component tests
- Use CSS-in-JS or CSS modules for styling
- Implement responsive design patterns

## Common Use Cases

### Creating Reusable Components
- Design components with clear, focused responsibilities
- Implement proper prop interfaces
- Add comprehensive documentation and examples

### API Integration
- Create custom hooks for data fetching
- Implement proper loading and error states
- Handle authentication and authorization

### Docusaurus Integration
- Create custom theme components
- Implement plugin functionality
- Customize the documentation experience

## References
- See [COMPONENT_LIBRARY.md](COMPONENT_LIBRARY.md) for reusable component patterns
- See [TYPESCRIPT_PATTERNS.md](TYPESCRIPT_PATTERNS.md) for advanced TypeScript techniques
- See [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md) for optimization strategies