# Data Model: Docusaurus ChatKit Integration

## Entity: BookContent
- **Fields**:
  - id: string (unique identifier for content section)
  - title: string (title of the section/chapter)
  - content: string (text content of the book section)
  - path: string (URL path in Docusaurus structure)
  - metadata: object (additional information like author, date, tags)
- **Relationships**: None
- **Validation**: Content must be non-empty, path must follow Docusaurus conventions
- **State transitions**: None (content is static once published)

## Entity: ChatMessage
- **Fields**:
  - id: string (unique message identifier)
  - sender_type: enum (USER | ASSISTANT)
  - content: string (message text)
  - timestamp: datetime (when message was sent/received)
  - status: string (message status: 'sent', 'delivered', 'error')
- **Relationships**: None (messages stored in component state)
- **Validation**: Content must be non-empty
- **State transitions**: None (messages are displayed as-is)

## Entity: ChatUIState
- **Fields**:
  - isChatOpen: boolean (whether the chat interface is currently open)
  - isLoading: boolean (whether the chat component is loading)
  - userInput: string (current user input in the chat)
  - messages: array (list of ChatMessage objects)
  - chatHistory: array (history of conversation sessions stored in localStorage)
- **Relationships**: None
- **Validation**: None
- **State transitions**: open ↔ closed (when user toggles chat interface)

## Entity: UserInterfaceState
- **Fields**:
  - currentPage: string (the current Docusaurus page being viewed)
  - bookNavigation: object (current state of book navigation)
  - chatWindowState: object (position, size and visibility of chat window)
  - theme: string (current theme: 'light' or 'dark')
- **Relationships**: None
- **Validation**: None
- **State transitions**: None (UI state changes based on user interactions)

## Entity: NavigationState
- **Fields**:
  - currentPath: string (current URL path)
  - breadcrumbs: array (navigation breadcrumbs)
  - sidebarOpen: boolean (whether sidebar navigation is open)
  - toc: array (table of contents for current page)
- **Relationships**: None
- **Validation**: Path must be valid Docusaurus route
- **State transitions**: None (navigation state changes with page navigation)

## Relationships Summary
- BookContent (1) → (0..n) NavigationState (via path relationships)
- ChatMessage (0..n) ↔ (1) ChatUIState (messages are contained in UI state)
- ChatUIState (1) ↔ (1) UserInterfaceState (chat state is part of overall UI state)