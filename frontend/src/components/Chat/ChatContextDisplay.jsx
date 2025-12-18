import React from 'react';
import { useChatContext } from './ChatContext';

const ChatContextDisplay = () => {
  const { context } = useChatContext();

  // Only show context if there's relevant information
  const hasContext = context.pageTitle || context.pageRoute || (context.selectedText && context.selectedText.trim() !== '');

  if (!hasContext) {
    return null;
  }

  return (
    <div className="bg-base-200 p-3 border-b border-base-300 text-sm">
      <div className="font-semibold text-base-content">Context</div>
      {context.pageTitle && (
        <div className="text-base-content text-sm mt-1">
          <strong>Page:</strong> {context.pageTitle}
        </div>
      )}
      {context.pageRoute && (
        <div className="text-base-content text-sm mt-1">
          <strong>Route:</strong> {context.pageRoute}
        </div>
      )}
      {context.selectedText && context.selectedText.trim() !== '' && (
        <div className="text-base-content text-sm mt-1">
          <strong>Selected Text:</strong> "{context.selectedText}"
        </div>
      )}
      {context.lastUpdated && (
        <div className="text-base-content text-sm mt-1 text-xs opacity-70">
          Updated: {context.lastUpdated.toLocaleTimeString()}
        </div>
      )}
    </div>
  );
};

export default ChatContextDisplay;