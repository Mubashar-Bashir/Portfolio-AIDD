# Data Model: Global Floating Chat UI with Local Context Awareness

## Entities

### FloatingChatComponent
- **Properties**:
  - isOpen (boolean): Current visibility state of the chat window
  - minimized (boolean): Whether chat is minimized or expanded
  - position (object): x, y coordinates for floating position
- **State transitions**:
  - closed → open (on click of floating icon)
  - open → closed (on click of close button)
  - open → minimized (on click of minimize button)
- **Validation**: Must maintain proper positioning within viewport bounds

### ChatMessage
- **Properties**:
  - id (string): Unique identifier for the message
  - content (string): Text content of the message
  - sender (string): 'user' or 'assistant'
  - timestamp (date): When the message was created
  - status (string): 'sent', 'delivered', 'read' (for mock purposes)
- **Validation**: Content must not be empty, sender must be valid type

### LocalContextData
- **Properties**:
  - pageTitle (string): Current page title from Docusaurus
  - pageRoute (string): Current URL/route information
  - selectedText (string): Text currently selected by user (if any)
  - lastUpdated (date): When context was last refreshed
- **Validation**: Page title and route should be non-empty when available

### ChatWindowState
- **Properties**:
  - isVisible (boolean): Whether chat window is currently displayed
  - messages (array): List of ChatMessage objects
  - context (LocalContextData): Current context information
  - unreadCount (number): Number of unread messages (mock)
- **State transitions**:
  - idle → active (when user interacts with chat)
  - active → idle (when user closes chat)

## Relationships
- FloatingChatComponent contains ChatWindowState
- ChatWindowState contains multiple ChatMessage objects
- ChatWindowState contains LocalContextData