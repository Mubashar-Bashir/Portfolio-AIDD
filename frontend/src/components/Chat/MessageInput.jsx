import React, { useState } from 'react';
import { useChatContext } from './ChatContext';
import ChatService from '../../services/mockChatService';

const MessageInput = () => {
  const [inputValue, setInputValue] = useState('');
  const { addMessage, context } = useChatContext();
  const [isSending, setIsSending] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isSending) return;

    setIsSending(true);

    try {
      // Add user message to UI immediately
      const userMessage = {
        id: Date.now().toString(),
        content: inputValue,
        sender: 'user',
        timestamp: new Date(),
        status: 'sent',
        contextInfo: { ...context }
      };

      addMessage(userMessage);

      // Clear input
      setInputValue('');

      // Send to service with context information (this will also trigger the assistant response)
      await ChatService.sendMessage(inputValue, { ...context });
    } catch (error) {
      console.error('Error sending message:', error);
      // Optionally show user-friendly error message
      alert(`Failed to send message: ${error.message || 'Unknown error occurred'}`);
    } finally {
      setIsSending(false);
    }
  };

  return (
    <div className="p-3 border-t border-base-300 flex items-center gap-2">
      <form onSubmit={handleSubmit} className="flex w-full gap-2">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Type your message..."
          className="flex-1 input input-bordered input-sm"
          aria-label="Type your message"
          disabled={isSending}
        />
        <button
          type="submit"
          className="btn btn-primary btn-sm disabled:opacity-50 disabled:cursor-not-allowed"
          disabled={!inputValue.trim() || isSending}
          aria-label="Send message"
        >
          {isSending ? (
            <span className="loading loading-spinner loading-xs"></span>
          ) : (
            'Send'
          )}
        </button>
      </form>
    </div>
  );
};

export default MessageInput;