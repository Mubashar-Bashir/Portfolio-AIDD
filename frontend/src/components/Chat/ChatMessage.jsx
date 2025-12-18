import React from 'react';

const ChatMessage = ({ message }) => {
  const isUser = message.sender === 'user';

  return (
    <div className={`flex mb-4 ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className={`${isUser ? 'bg-primary text-primary-content rounded-br-none' : 'bg-base-200 text-base-content rounded-bl-none'} max-w-[80%] rounded-lg px-4 py-2`}>
        <div className="text-xs font-semibold mb-1">
          {isUser ? 'You' : 'Assistant'}
        </div>
        <div className="text-sm">
          {message.content}
        </div>
        {message.timestamp && (
          <div className="text-xs opacity-70 mt-1 text-right">
            {new Date(message.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </div>
        )}
      </div>
    </div>
  );
};

export default ChatMessage;