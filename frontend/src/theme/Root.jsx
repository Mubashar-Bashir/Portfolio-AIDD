import React, { useState, useEffect } from 'react';
import LessonAssistant from '../components/Chat/LessonAssistant';
import { ChatServiceProvider } from '../components/Chat/ChatContext';

// Global wrapper to integrate floating lesson assistant across all pages
const Root = ({ children }) => {
  const [isChatLoaded, setIsChatLoaded] = useState(false);

  // Load the floating chat component after initial render to avoid SSR issues
  useEffect(() => {
    setIsChatLoaded(true);
  }, []);

  return (
    <ChatServiceProvider>
      {children}
      {isChatLoaded && <LessonAssistant />}
    </ChatServiceProvider>
  );
};

export default Root;