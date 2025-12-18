import React, { useEffect, useRef } from 'react';
import { useChatContext } from './ChatContext';
import ChatMessage from './ChatMessage';

const MessageList = () => {
  const { messages } = useChatContext();
  const messagesEndRef = useRef(null);

  // Scroll to bottom when messages change
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-3">
      {messages && messages.length > 0 ? (
        messages.map((message) => (
          <ChatMessage key={message.id} message={message} />
        ))
      ) : (
        <div className="text-center text-base-content opacity-70 py-4">
          No messages yet. Start the conversation!
        </div>
      )}
      <div ref={messagesEndRef} />
    </div>
  );
};

export default MessageList;