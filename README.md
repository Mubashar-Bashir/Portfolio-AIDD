# Docusaurus ChatKit Integration

This project combines a Docusaurus documentation site with a ChatKit interface for interactive book content assistance.

## Project Structure

- `frontend/` - Docusaurus-based documentation site with integrated chat interface
- `backend/` - FastAPI backend that provides chat, search, and content APIs

## Features

- Docusaurus-based documentation site with book content
- Integrated ChatKit interface for interactive assistance
- API endpoints for chat functionality, content search, and book content access
- Context-aware chat that references current page content

## Prerequisites

- Node.js (v16 or higher)
- Python 3.11+
- npm or yarn package manager

## Setup and Running

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   pip install pydantic-settings
   ```

4. Start the backend server:
   ```bash
   python -m uvicorn main:app --reload --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The frontend will be available at http://localhost:3000 and will connect to the backend at http://localhost:8000.

## API Endpoints

The backend provides the following API endpoints under `http://localhost:8000/api/v1/`:

- `POST /chat/start` - Start a new chat session
- `POST /chat/{session_id}/message` - Send a message in a chat session
- `GET /chat/{session_id}` - Get chat session details
- `POST /search` - Search book content
- `GET /content/{content_id}` - Get specific book content
- `GET /content/list` - List available book content

## Environment Variables

Create a `.env` file in the backend directory with the following variables:

```env
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
BACKEND_CORS_ORIGINS=http://localhost,http://localhost:3000
```

## Development

- The frontend uses React components in the `src/components/` directory
- ChatKit components are in `src/components/ChatKit/`
- Book content components are in `src/components/BookContent/`
- The chat interface is integrated into the Docusaurus theme via `src/theme/Layout.jsx`

## Building for Production

To build the frontend for production:

```bash
npm run build
```

Note: There may be webpack polyfill issues during the build process. If you encounter issues, the development server (`npm start`) works correctly for testing and development.

## Troubleshooting

- Ensure the backend server is running before starting the frontend
- Check that the API endpoints are accessible from the frontend
- Verify that CORS settings allow communication between frontend and backend