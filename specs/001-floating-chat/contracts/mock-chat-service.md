# Mock Chat Service Interface

## Purpose
Defines the interface for the mock chat service that provides UI-only chat functionality without backend integration.

## Service Definition

### ChatService Interface

```javascript
interface ChatService {
  // Get initial mocked messages
  getInitialMessages(): Promise<ChatMessage[]>

  // Simulate sending a message
  sendMessage(content: string): Promise<ChatMessage>

  // Get current context
  getCurrentContext(): Promise<LocalContextData>

  // Update context when page changes
  updateContext(context: LocalContextData): void
}
```

### Data Types

```javascript
type ChatMessage = {
  id: string
  content: string
  sender: 'user' | 'assistant'
  timestamp: Date
  status: 'sent' | 'delivered' | 'read'
}

type LocalContextData = {
  pageTitle: string
  pageRoute: string
  selectedText: string
  lastUpdated: Date
}
```

## Implementation Notes
- All methods return Promise to simulate async behavior
- No actual network requests are made
- Messages are stored in-memory for the session
- Context is updated reactively based on page state