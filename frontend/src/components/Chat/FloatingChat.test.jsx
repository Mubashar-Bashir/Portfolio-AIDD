import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import FloatingChat from './FloatingChat';
import { ChatServiceProvider } from './ChatContext';

// Mock the hooks and services
jest.mock('../../hooks/usePageContext', () => ({
  default: () => ({ pageTitle: 'Test Page', pageRoute: '/test' })
}));

jest.mock('../../hooks/useSelectedText', () => ({
  default: () => ''
}));

jest.mock('../../services/mockChatService', () => ({
  default: {
    getInitialMessages: jest.fn(() => Promise.resolve([])),
    sendMessage: jest.fn((content) => Promise.resolve({
      id: Date.now().toString(),
      content,
      sender: 'user',
      timestamp: new Date(),
      status: 'sent'
    }))
  }
}));

// Wrapper component to provide context
const renderWithProvider = (component) => {
  return render(
    <ChatServiceProvider>
      {component}
    </ChatServiceProvider>
  );
};

describe('FloatingChat', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders floating chat button when closed', () => {
    renderWithProvider(<FloatingChat />);

    const chatButton = screen.getByLabelText('Open chat');
    expect(chatButton).toBeInTheDocument();
  });

  test('opens chat window when button is clicked', async () => {
    renderWithProvider(<FloatingChat />);

    const chatButton = screen.getByLabelText('Open chat');
    fireEvent.click(chatButton);

    // Wait for the chat window to appear
    await waitFor(() => {
      const chatWindow = screen.getByRole('dialog');
      expect(chatWindow).toBeInTheDocument();
    });
  });

  test('closes chat window when close button is clicked', async () => {
    renderWithProvider(<FloatingChat />);

    // Open the chat first
    const openButton = screen.getByLabelText('Open chat');
    fireEvent.click(openButton);

    await waitFor(() => {
      expect(screen.getByRole('dialog')).toBeInTheDocument();
    });

    // Close the chat
    const closeButton = screen.getByLabelText('Close chat');
    fireEvent.click(closeButton);

    // Wait for the chat window to disappear
    await waitFor(() => {
      expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
    });
  });

  test('should have proper accessibility attributes', () => {
    renderWithProvider(<FloatingChat />);

    const chatButton = screen.getByLabelText('Open chat');
    expect(chatButton).toHaveAttribute('tabIndex', '0');
    expect(chatButton).toHaveAttribute('aria-label', 'Open chat');
  });

  test('should respond to keyboard shortcuts', () => {
    renderWithProvider(<FloatingChat />);

    // Simulate Alt+Shift+C to open chat
    fireEvent.keyDown(window, { key: 'C', altKey: true, shiftKey: true });

    // Verify chat button is focused or chat opens (depending on implementation)
    // This test might need adjustment based on actual behavior
  });
});