# Tailwind CSS Usage Guidelines and Prevention Rules

## Issue Report: Tailwind @apply Directive Compilation Error

### Problem Description
A Tailwind CSS compilation error occurred due to the use of `@apply` directives in a plain CSS file (`chat-styles.css`). The error "Cannot apply unknown utility class w-14" was generated because Tailwind's `@apply` directive only works within files that are processed by Tailwind's build pipeline, but plain CSS files are not processed by Tailwind.

### Root Cause Analysis
1. **Misplaced @apply directives**: Tailwind utility classes were being applied in a plain CSS file that wasn't processed by Tailwind
2. **Build pipeline mismatch**: The CSS file was imported normally but contained Tailwind-specific syntax that required preprocessing
3. **Lack of clear styling guidelines**: No documented rule prevented the use of `@apply` in regular CSS files

### Impact
- Build failures during development and production
- Developer confusion about proper Tailwind usage
- Potential delays in project delivery

## Prevention Rules

### 1. Inline Tailwind Classes in JSX/TSX Components
**Rule**: Always use Tailwind utility classes directly in the `className` prop of JSX/TSX components
```jsx
// ✅ CORRECT
<button className="w-14 h-14 rounded-full bg-primary text-primary-content">
  Chat
</button>

// ❌ AVOID
<button className="chat-button">
  Chat
</button>
// Then defining .chat-button { @apply w-14 h-14 rounded-full bg-primary text-primary-content; }
```

### 2. Reserved Use of @apply Directives
**Rule**: Use `@apply` directives only in files that are guaranteed to be processed by Tailwind:
- CSS files processed through a build system that runs Tailwind
- Files with specific Tailwind configuration in the build pipeline
- Never in plain CSS files imported directly

### 3. Component-First Styling Approach
**Rule**: Prioritize component-level styling over global CSS when using Tailwind:
- Keep Tailwind utility classes in the components that use them
- Create reusable component functions/fragments for repeated styles
- Use CSS modules or styled-components for complex styling that can't be expressed with Tailwind

### 4. Animation and Complex CSS Handling
**Rule**: For animations, keyframes, and complex CSS that can't be expressed with Tailwind:
- Create minimal CSS files for animations only
- Use specific file naming (e.g., `*-animations.css`, `*-keyframes.css`)
- Document that these files contain only non-Tailwind CSS features
- Import these files only where needed

### 5. Code Review Checklist
Add these items to the code review checklist:
- [ ] No `@apply` directives in plain CSS files
- [ ] Tailwind utility classes are used directly in JSX/TSX components
- [ ] CSS files containing `@apply` are processed by Tailwind build pipeline
- [ ] Component styling follows the inline Tailwind approach

### 6. Team Training Points
- Educate team members about the difference between Tailwind utility classes and regular CSS
- Explain when and where `@apply` can be used safely
- Demonstrate the component-first styling approach with Tailwind
- Provide examples of proper and improper Tailwind usage

## Implementation Guidelines

### For New Components:
1. Use Tailwind classes directly in the component's `className` props
2. Create reusable component functions for common styling patterns
3. Use CSS-in-JS or styled-components for complex, non-Tailwind styles
4. Keep animations in separate CSS files that are properly configured

### For Existing CSS Files:
1. Migrate `@apply` directives to inline Tailwind classes in components
2. Remove `@apply` from plain CSS files
3. Create minimal CSS files for animations and complex CSS only
4. Update imports to reference the new component-based styling

### For Build Process:
1. Ensure Tailwind is properly configured to process only intended files
2. Verify that plain CSS files are not expected to contain Tailwind directives
3. Add build-time checks to catch improper `@apply` usage
4. Set up proper error reporting for Tailwind compilation issues

## Enforcement Strategy

### 1. Linting Rules
Configure ESLint and Stylelint to catch improper Tailwind usage:
- Rule to warn on CSS files containing `@apply`
- Rule to encourage direct Tailwind usage in components

### 2. Pre-commit Hooks
Add pre-commit checks to prevent `@apply` in plain CSS files:
- Validate CSS files for Tailwind-specific syntax
- Run Tailwind build to catch compilation errors early

### 3. Documentation Updates
Update project documentation to include these guidelines:
- Add to the project constitution
- Include in the development workflow documentation
- Create examples in the component library

## Version Information
- **Document Version**: 1.0.0
- **Created**: 2025-12-18
- **Last Updated**: 2025-12-18
- **Status**: Active