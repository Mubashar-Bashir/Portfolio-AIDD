import React, { useState } from 'react';
import { useChatContext } from './ChatContext';
import ChatContextDisplay from './ChatContextDisplay';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const ChatWindow = ({ onClose }) => {
  const { context } = useChatContext();
  const [isMinimized, setIsMinimized] = useState(false);

  if (isMinimized) {
    return (
      <div className="bg-primary text-primary-content p-2 rounded-lg shadow-lg cursor-pointer" onClick={() => setIsMinimized(false)}>
        <div className="flex items-center justify-between">
          <span className="font-bold">Chat</span>
          <span className="text-sm">({context.pageTitle || 'Page'})</span>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-base-100 border border-base-300 rounded-lg shadow-2xl flex flex-col w-80 h-[500px] max-h-[80vh] transition-all duration-300">
      {/* Chat Header */}
      <div className="bg-primary text-primary-content p-4 rounded-t-lg flex justify-between items-center">
        <div className="flex items-center">
          <h3 className="font-bold text-lg">AI Assistant</h3>
          {context.pageTitle && (
            <span className="ml-2 text-xs opacity-80 truncate max-w-[100px]">{context.pageTitle}</span>
          )}
        </div>
        <div className="flex space-x-2">
          <button
            className="text-primary-content hover:text-white cursor-pointer text-xl"
            onClick={() => setIsMinimized(true)}
            aria-label="Minimize chat"
          >
            −
          </button>
          <button
            className="text-primary-content hover:text-white cursor-pointer text-xl"
            onClick={onClose}
            aria-label="Close chat"
          >
            ×
          </button>
        </div>
      </div>

      {/* Context Display */}
      <ChatContextDisplay />

      {/* Messages */}
      <MessageList />

      {/* Input Area */}
      <MessageInput />
    </div>
  );
};

export default ChatWindow;