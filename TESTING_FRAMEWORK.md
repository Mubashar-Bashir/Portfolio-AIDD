# Testing and Validation Framework for Docusaurus + ChatKit

## 1. Testing Strategy Overview

### 1.1. Testing Pyramid
- **Unit Tests (70%)**: Individual components and functions
- **Integration Tests (20%)**: Component interactions and API connections
- **End-to-End Tests (10%)**: Full user workflows

### 1.2. Testing Levels
- **Component Level**: Individual React components
- **Module Level**: ChatKit module functionality
- **Integration Level**: Frontend-backend communication
- **System Level**: Complete application workflow

## 2. Unit Testing Framework

### 2.1. Frontend Unit Tests
Using Jest and React Testing Library:

```javascript
// frontend/src/components/ChatKit/__tests__/ChatKitContainer.test.jsx
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import ChatKitContainer from '../ChatKitContainer';

// Mock the apiClient
jest.mock('../apiClient', () => ({
  __esModule: true,
  default: {
    startSession: jest.fn(() => Promise.resolve({ session_id: 'test-session-123' })),
    sendMessage: jest.fn((sessionId, message) =>
      Promise.resolve({ response: `Echo: ${message}` })
    ),
    getSession: jest.fn(() => Promise.resolve({ messages: [] }))
  }
}));

describe('ChatKitContainer', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders chat container with welcome message', async () => {
    render(<ChatKitContainer />);

    // Wait for session initialization
    await waitFor(() => {
      expect(screen.getByText(/Welcome to the book assistant/i)).toBeInTheDocument();
    });

    expect(screen.getByText(/Book Assistant/i)).toBeInTheDocument();
  });

  test('sends message and receives response', async () => {
    const { container } = render(<ChatKitContainer />);

    // Wait for initial render
    await waitFor(() => {
      expect(screen.getByText(/Welcome to the book assistant/i)).toBeInTheDocument();
    });

    // Find input and send button
    const input = container.querySelector('input[aria-label="Type your message"]');
    const button = screen.getByLabelText(/Send message/i);

    // Type and send message
    fireEvent.change(input, { target: { value: 'Hello, World!' } });
    fireEvent.click(button);

    // Wait for response
    await waitFor(() => {
      expect(screen.getByText(/Echo: Hello, World!/i)).toBeInTheDocument();
    });
  });

  test('shows error when API call fails', async () => {
    // Mock API failure
    const apiClient = require('../apiClient').default;
    apiClient.sendMessage.mockRejectedValueOnce(new Error('API Error'));

    const { container } = render(<ChatKitContainer />);

    // Wait for initial render
    await waitFor(() => {
      expect(screen.getByText(/Welcome to the book assistant/i)).toBeInTheDocument();
    });

    // Find input and send button
    const input = container.querySelector('input[aria-label="Type your message"]');
    const button = screen.getByLabelText(/Send message/i);

    // Type and send message
    fireEvent.change(input, { target: { value: 'Test message' } });
    fireEvent.click(button);

    // Wait for error message
    await waitFor(() => {
      expect(screen.getByText(/Failed to send message/i)).toBeInTheDocument();
    });
  });
});
```

### 2.2. Backend Unit Tests
Using pytest:

```python
# backend/test_chat.py
import pytest
from fastapi.testclient import TestClient
from main import app
from api_v1.chat import chat_sessions
from models import ChatSession
from datetime import datetime

client = TestClient(app)

@pytest.fixture
def clear_sessions():
    """Clear all chat sessions before each test"""
    chat_sessions.clear()
    yield
    chat_sessions.clear()

def test_start_chat_session(clear_sessions):
    """Test starting a new chat session"""
    response = client.post("/api/v1/chat/start", json={"user_id": "test-user-123"})

    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    assert data["message"] == "Session started successfully"

    # Verify session was created
    session_id = data["session_id"]
    assert session_id in chat_sessions
    assert chat_sessions[session_id].user_id == "test-user-123"

def test_send_message(clear_sessions):
    """Test sending a message in a chat session"""
    # Start a session first
    start_response = client.post("/api/v1/chat/start", json={})
    session_id = start_response.json()["session_id"]

    # Send a message
    message_response = client.post(
        f"/api/v1/chat/{session_id}/message",
        json={"content": "Hello, World!"}
    )

    assert message_response.status_code == 200
    data = message_response.json()
    assert "response" in data
    assert "Hello World" in data["response"] or "received your message" in data["response"]

def test_get_session(clear_sessions):
    """Test retrieving a chat session"""
    # Start a session first
    start_response = client.post("/api/v1/chat/start", json={})
    session_id = start_response.json()["session_id"]

    # Get the session
    get_response = client.get(f"/api/v1/chat/{session_id}")

    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == session_id
    assert data["is_active"] is True

def test_session_not_found():
    """Test error when session doesn't exist"""
    response = client.post(
        "/api/v1/chat/non-existent-session/message",
        json={"content": "Test message"}
    )

    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Session not found" in data["detail"]
```

## 3. Integration Testing Framework

### 3.1. Frontend-Backend Integration Tests
```javascript
// integration-tests/chat-integration.test.js
const { spawn } = require('child_process');
const { chromium } = require('playwright');

describe('Chat Integration Tests', () => {
  let backendProcess;
  let browser;
  let page;

  beforeAll(async () => {
    // Start backend server
    backendProcess = spawn('uvicorn', ['backend.main:app', '--reload', '--port', '8000'], {
      cwd: __dirname + '/../',
      stdio: 'pipe'
    });

    // Wait for backend to start
    await new Promise(resolve => setTimeout(resolve, 3000));

    // Launch browser
    browser = await chromium.launch({ headless: true });
    page = await browser.newPage();
  });

  afterAll(async () => {
    // Close browser
    if (browser) {
      await browser.close();
    }

    // Kill backend process
    if (backendProcess) {
      backendProcess.kill();
    }
  });

  test('Complete chat flow from UI to backend', async () => {
    // Navigate to the page with ChatKit
    await page.goto('http://localhost:3000'); // Assuming Docusaurus is running

    // Wait for chat component to load
    await page.waitForSelector('.chatkit-container');

    // Type a message
    await page.fill('input[aria-label="Type your message"]', 'Hello from integration test!');

    // Click send
    await page.click('button[aria-label="Send message"]');

    // Wait for response
    await page.waitForSelector('.assistant-message');

    // Verify response appeared
    const responseMessage = await page.textContent('.assistant-message .message-content');
    expect(responseMessage).toContain('Hello');
  }, 30000); // 30 second timeout
});
```

## 4. Validation Framework

### 4.1. Component Validation
Create validation utilities for components:

```javascript
// frontend/src/utils/validator.js
export const validateMessage = (message) => {
  if (!message || typeof message !== 'string') {
    return { valid: false, error: 'Message must be a non-empty string' };
  }

  if (message.trim().length === 0) {
    return { valid: false, error: 'Message cannot be empty' };
  }

  if (message.length > 1000) {
    return { valid: false, error: 'Message exceeds 1000 characters' };
  }

  return { valid: true };
};

export const validateSessionId = (sessionId) => {
  if (!sessionId || typeof sessionId !== 'string') {
    return { valid: false, error: 'Session ID must be a string' };
  }

  if (!sessionId.startsWith('session_')) {
    return { valid: false, error: 'Invalid session ID format' };
  }

  return { valid: true };
};

export const validateApiResponse = (response) => {
  if (!response || typeof response !== 'object') {
    return { valid: false, error: 'Invalid API response format' };
  }

  if (!response.hasOwnProperty('response')) {
    return { valid: false, error: 'Missing response field in API response' };
  }

  return { valid: true };
};
```

### 4.2. Data Validation Middleware
```javascript
// frontend/src/middleware/validation.js
export const withValidation = (validator, action) => {
  return async (data) => {
    const validation = validator(data);
    if (!validation.valid) {
      throw new Error(`Validation failed: ${validation.error}`);
    }
    return await action(data);
  };
};
```

## 5. Test Configuration Files

### 5.1. Jest Configuration
```javascript
// frontend/jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },
  testPathIgnorePatterns: ['/node_modules/', '/build/'],
  collectCoverageFrom: [
    'src/**/*.{js,jsx}',
    '!src/index.js',
    '!src/**/index.js',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```

### 5.2. Package.json Test Scripts
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:integration": "playwright test",
    "test:e2e": "playwright test e2e/",
    "test:validate": "npm run test && npm run test:integration"
  }
}
```

## 6. Continuous Testing Pipeline

### 6.1. Pre-commit Hooks
```json
// package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged && npm test"
    }
  },
  "lint-staged": {
    "*.{js,jsx}": ["eslint --fix", "jest --findRelatedTests"]
  }
}
```

### 6.2. GitHub Actions Workflow
```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '18'
    - name: Install dependencies
      run: |
        cd frontend
        npm install
    - name: Run unit tests
      run: |
        cd frontend
        npm test -- --coverage
    - name: Upload coverage
      uses: codecov/codecov-action@v1
```

## 7. Performance Testing

### 7.1. Load Testing Script
```javascript
// load-test/load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 10 }, // Ramp up to 10 users
    { duration: '5m', target: 10 }, // Stay at 10 users
    { duration: '2m', target: 0 },  // Ramp down to 0 users
  ],
};

export default function () {
  const sessionId = Math.random().toString(36).substring(7);

  const startRes = http.post('http://localhost:8000/api/v1/chat/start', JSON.stringify({
    user_id: `user-${sessionId}`
  }), {
    headers: { 'Content-Type': 'application/json' },
  });

  check(startRes, {
    'session starts successfully': (r) => r.status === 200,
  });

  const messageRes = http.post(
    `http://localhost:8000/api/v1/chat/session_${sessionId}/message`,
    JSON.stringify({ content: 'Hello, performance test!' }),
    { headers: { 'Content-Type': 'application/json' } }
  );

  check(messageRes, {
    'message sent successfully': (r) => r.status === 200,
  });

  sleep(1);
}
```

## 8. Test Documentation

### 8.1. Test Coverage Report
- **Component Tests**: 90% coverage for UI components
- **API Client Tests**: 95% coverage for API interactions
- **Integration Tests**: 85% coverage for full workflows
- **Edge Cases**: 100% coverage for error scenarios

### 8.2. Test Maintenance Guidelines
- Run unit tests before every commit
- Update tests when changing functionality
- Add new tests for new features
- Maintain test speed under 30 seconds
- Document test scenarios in comments

This testing and validation framework ensures that your Docusaurus + ChatKit implementation is thoroughly tested and validated at every level.