---
name: animated-components
description: Create attractive, performant animated components for enhanced user experience. Use when Claude needs to work with animations for: (1) Creating micro-interactions, (2) Implementing loading animations, (3) Designing page transitions, (4) Optimizing animation performance, (5) Creating engaging UI effects
---

# Animated Components Expert Skill

## Purpose
This skill provides guidance for creating attractive, performant animated components that enhance user experience without compromising performance. It focuses on implementing animations that are both engaging and technically sound.

## When to Use This Skill
- Creating micro-interactions for user feedback
- Implementing loading and transition animations
- Designing page and component transitions
- Optimizing animation performance and smoothness
- Creating engaging UI effects that enhance usability
- Implementing accessibility-aware animations

## Core Capabilities

### Micro-interactions
- Design subtle feedback animations for user actions
- Create hover and focus state animations
- Implement loading and progress indicators
- Add personality through motion design

### Performance Optimization
- Use CSS transforms and opacity for smooth animations
- Implement animation frame optimization
- Apply proper animation triggering techniques
- Minimize layout thrashing and repaints

### Animation Libraries
- Leverage Framer Motion, React Spring, or similar
- Create custom animation hooks
- Implement staggered and sequenced animations
- Handle animation state management

### Accessibility Considerations
- Respect user preference for reduced motion
- Provide animation cancellation options
- Maintain accessibility during animations
- Ensure animations don't cause seizures

## Key Animation Principles

### Performance
- Use hardware-accelerated properties (transform, opacity)
- Avoid animating layout properties (width, height, left, top)
- Implement proper animation timing and easing
- Optimize for 60fps performance

### Purpose
- Use animation to enhance, not distract
- Provide clear feedback for user actions
- Guide attention to important elements
- Create visual continuity between states

### Smoothness
- Use appropriate easing functions
- Maintain consistent timing across animations
- Implement proper animation chaining
- Consider animation duration for different contexts

## Best Practices
- Keep animations short (100-500ms for micro-interactions)
- Use consistent easing functions throughout the interface
- Respect user's reduced motion preferences
- Test animations on various devices and performance levels
- Avoid animating too many elements simultaneously
- Provide meaningful animations that support user tasks

## Common Animation Patterns

### Component Animations
- Fade in/out transitions
- Slide and scale effects
- Staggered list animations
- Collapse and expand transitions

### Feedback Animations
- Button press states
- Form validation feedback
- Loading spinners and progress bars
- Success and error state animations

### Navigation Animations
- Page transition effects
- Modal entrance/exit animations
- Tab switching animations
- Menu open/close effects

## References
- See [ANIMATION_PATTERNS.md](ANIMATION_PATTERNS.md) for common animation implementation techniques
- See [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md) for animation optimization strategies
- See [ACCESSIBILITY.md](ACCESSIBILITY.md) for accessible animation practices