import React, { useState } from 'react'

function InputBox({ onSend, isLoading }) {
  const [input, setInput] = useState('')

  const handleSend = () => {
    const trimmed = input.trim()
    if (!trimmed || isLoading) return
    onSend(trimmed)
    setInput('')
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="border-t border-gray-100 bg-white p-4">
      <div className="flex items-center gap-3 bg-gray-50 rounded-xl border border-gray-200 px-4 py-2 focus-within:border-blue-400 focus-within:ring-2 focus-within:ring-blue-100 transition-all">
        <input
          type="text"
          className="flex-1 bg-transparent text-sm text-gray-800 placeholder-gray-400 outline-none"
          placeholder="Ask about tasks, priorities, owners..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={isLoading}
        />
        <button
          onClick={handleSend}
          disabled={isLoading || !input.trim()}
          className={`w-8 h-8 rounded-lg flex items-center justify-center transition-all ${
            input.trim() && !isLoading
              ? 'bg-blue-600 text-white hover:bg-blue-700 active:scale-95'
              : 'bg-gray-200 text-gray-400 cursor-not-allowed'
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="w-4 h-4"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <line x1="22" y1="2" x2="11" y2="13" />
            <polygon points="22 2 15 22 11 13 2 9 22 2" />
          </svg>
        </button>
      </div>
      <p className="text-xs text-gray-400 mt-2 text-center">
        Press Enter to send · Shift+Enter for new line
      </p>
    </div>
  )
}

export default InputBox
