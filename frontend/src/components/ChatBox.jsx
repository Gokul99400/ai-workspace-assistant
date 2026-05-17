import React, { useEffect, useRef } from 'react'
import MessageBubble from './MessageBubble'

/**
 * ChatBox Component
 * Renders the scrollable list of chat messages.
 * Props:
 *   - messages: Array of { role, text }
 *   - isLoading: boolean
 */
function ChatBox({ messages, isLoading }) {
  // Reference to the bottom of the message list for auto-scroll
  const bottomRef = useRef(null)

  // Auto-scroll to the latest message whenever messages change
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading])

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-1 chat-scroll bg-gray-50">
      {/* Show placeholder when no messages */}
      {messages.length === 0 && (
        <div className="flex flex-col items-center justify-center h-full text-center text-gray-400 py-16">
          <div className="w-16 h-16 bg-white rounded-2xl shadow-sm border border-gray-100 flex items-center justify-center mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" className="w-8 h-8 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
            </svg>
          </div>
          <p className="font-medium text-gray-500 mb-1">Start a conversation</p>
          <p className="text-sm">Try: "Show high priority tasks" or "What tasks are overdue?"</p>
        </div>
      )}

      {/* Render all messages */}
      {messages.map((msg, index) => (
        <MessageBubble key={index} message={msg} />
      ))}

      {/* Loading indicator — "AI is typing..." */}
      {isLoading && (
        <div className="flex items-end gap-2 mb-4">
          <div className="w-8 h-8 rounded-full bg-emerald-500 flex items-center justify-center text-xs font-bold text-white flex-shrink-0">
            AI
          </div>
          <div className="bg-white border border-gray-100 rounded-2xl rounded-bl-md px-4 py-3 shadow-sm">
            <div className="flex items-center gap-1 text-gray-400 text-sm">
              <span>AI is typing</span>
              <span className="dot-1 text-blue-500 font-bold">.</span>
              <span className="dot-2 text-blue-500 font-bold">.</span>
              <span className="dot-3 text-blue-500 font-bold">.</span>
            </div>
          </div>
        </div>
      )}

      {/* Invisible div at the bottom for auto-scroll */}
      <div ref={bottomRef} />
    </div>
  )
}

export default ChatBox
