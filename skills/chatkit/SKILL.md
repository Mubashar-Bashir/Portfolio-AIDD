---
name: chatkit
description: Comprehensive ChatKit implementation, customization, and integration with backend services. Use when Claude needs to work with chat functionality for: (1) Implementing chat interfaces, (2) Customizing chat components, (3) Integrating with backend AI services, (4) Managing chat sessions and messages, (5) Implementing RAG-based chat responses
---

# ChatKit Integration Skill

## Purpose
This skill provides comprehensive guidance for implementing, customizing, and integrating chat functionality into web applications. It focuses on creating seamless chat experiences with proper backend integration and AI-powered responses.

## When to Use This Skill
- Implementing chat interfaces in web applications
- Customizing chat component appearance and behavior
- Integrating chat with backend services and APIs
- Implementing RAG (Retrieval Augmented Generation) for chat responses
- Managing chat sessions and message history
- Optimizing chat performance and user experience

## Core Capabilities

### Chat Interface Implementation
- Create responsive and accessible chat UI components
- Implement message display with proper formatting
- Add typing indicators and status updates
- Design message input and submission controls

### Backend Integration
- Connect chat frontend to backend APIs
- Implement real-time message synchronization
- Handle authentication and authorization
- Manage connection states and error handling

### RAG Integration
- Implement semantic search for context retrieval
- Connect to vector databases (Qdrant, etc.)
- Inject retrieved context into AI responses
- Ensure responses are grounded in source content

### Session Management
- Create and manage chat sessions
- Store and retrieve conversation history
- Handle session timeouts and cleanup
- Implement anonymous vs. authenticated sessions

## Key Implementation Patterns

### Message Structure
```typescript
interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  sources?: string[]; // For RAG-based responses
}
```

### API Integration
- Use REST or WebSocket patterns as appropriate
- Implement proper error handling and retry logic
- Handle rate limiting and connection management

### Context Injection
- Retrieve relevant content before AI processing
- Format context for optimal AI response quality
- Track source citations in responses

## Best Practices
- Ensure all responses are grounded in source content (RAG compliance)
- Implement proper security measures for API keys
- Design for accessibility (keyboard navigation, screen readers)
- Optimize for performance with message virtualization
- Handle edge cases (network failures, large message volumes)
- Maintain consistent user experience across devices

## Common Implementation Scenarios

### Basic Chat Interface
- Message history display
- Text input with send functionality
- Real-time message updates
- Typing indicators

### RAG-Enhanced Chat
- Context retrieval from document database
- Source citation in responses
- Relevance scoring for retrieved content
- Fallback responses when no context found

### Session Management
- Create new sessions for conversations
- Resume existing sessions
- Clear or archive old sessions
- Handle concurrent sessions

## References
- See [CHAT_INTEGRATION.md](CHAT_INTEGRATION.md) for frontend-backend integration patterns
- See [RAG_IMPLEMENTATION.md](RAG_IMPLEMENTATION.md) for Retrieval Augmented Generation techniques
- See [UI_PATTERNS.md](UI_PATTERNS.md) for chat interface design patterns