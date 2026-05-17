import React from 'react'

function MessageBubble({ message }) {
  const isUser = message.role === 'user'

  return (
    <div className={`flex items-end gap-2 mb-4 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>
      <div
        className={`w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 ${
          isUser
            ? 'bg-blue-600 text-white'
            : 'bg-emerald-500 text-white'
        }`}
      >
        {isUser ? 'You' : 'AI'}
      </div>
      <div
        className={`max-w-[75%] px-4 py-3 rounded-2xl text-sm leading-relaxed shadow-sm ${
          isUser
            ? 'bg-blue-600 text-white rounded-br-md'
            : 'bg-white text-gray-800 border border-gray-100 rounded-bl-md'
        }`}
      >
        {message.text.split('\n').map((line, i) => (
          <p key={i} className={line === '' ? 'mt-1' : ''}>
            {line}
          </p>
        ))}
      </div>
    </div>
  )
}

export default MessageBubble
