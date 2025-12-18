# Quickstart: Global Floating Chat UI with Local Context Awareness

## Development Setup

1. **Prerequisites**
   - Node.js 18+
   - npm or yarn
   - Docusaurus project already set up

2. **Installation**
   ```bash
   # Navigate to frontend directory
   cd frontend/

   # Install dependencies (if not already installed)
   npm install
   ```

3. **Running the Development Server**
   ```bash
   # Start Docusaurus development server
   npm start
   ```

## Component Structure

The floating chat UI consists of several key components:

- `FloatingChat.jsx` - Main component that provides the floating icon and manages open/close state
- `ChatWindow.jsx` - The main chat window UI when expanded
- `ChatMessage.jsx` - Individual message display component
- `ChatContext.jsx` - Component that displays local context information
- `usePageContext.js` - Hook to get current page title/route
- `useSelectedText.js` - Hook to detect and retrieve selected text

## Key Features

1. **Floating Icon**: Always visible chat icon that can be clicked to open the chat
2. **Context Awareness**: Automatically detects and displays current page title/route
3. **Text Selection**: Detects when user selects text and displays it in the context area
4. **Mock Messages**: Predefined messages to simulate conversation experience
5. **Responsive Design**: Works on all device sizes with TailwindCSS/DaisyUI

## Integration Points

The chat component is integrated at the global layout level by wrapping the main Docusaurus layout, ensuring it's available on all pages without requiring individual page modifications.