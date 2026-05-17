import React, { useState } from 'react'
import axios from 'axios'
import ChatBox from './components/ChatBox'
import InputBox from './components/InputBox'

const API_URL = 'http://127.0.0.1:8000/chat'

const SUGGESTIONS = [
  'Show high priority tasks',
  'What tasks are overdue?',
  'Show tasks assigned to Gokul',
  'Show completed tasks',
  'CRM project tasks',
  'Show pending tasks',
]

function App() {
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  const sendMessage = async (userMessage) => {
    const userEntry = { role: 'user', text: userMessage }
    setMessages((prev) => [...prev, userEntry])
    setIsLoading(true)

    try {
      const response = await axios.post(API_URL, { message: userMessage })
      const botReply = response.data.reply
      setMessages((prev) => [...prev, { role: 'bot', text: botReply }])
    } catch (error) {
      const errorMsg =
        error.response?.data?.detail ||
        'Could not connect to the backend. Please make sure the server is running on port 8000.'
      setMessages((prev) => [...prev, { role: 'bot', text: `⚠️ Error: ${errorMsg}` }])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 to-blue-50 flex items-center justify-center p-4">
      <div className="w-full max-w-2xl flex flex-col bg-white rounded-2xl shadow-xl overflow-hidden" style={{ height: '85vh' }}>
        <div className="bg-gradient-to-r from-blue-600 to-blue-700 px-6 py-4 flex items-center gap-3">
          <div className="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <div>
            <h1 className="text-white font-semibold text-lg leading-none">AI Workspace Assistant</h1>
            <p className="text-blue-200 text-xs mt-0.5">Powered by Ollama · Gemma 2B</p>
          </div>
          <div className="ml-auto flex items-center gap-1.5">
            <div className="w-2 h-2 bg-emerald-400 rounded-full"></div>
            <span className="text-blue-200 text-xs">Online</span>
          </div>
        </div>
        {messages.length === 0 && (
          <div className="px-4 py-3 bg-white border-b border-gray-100">
            <p className="text-xs text-gray-400 mb-2 font-medium uppercase tracking-wide">Quick Queries</p>
            <div className="flex flex-wrap gap-2">
              {SUGGESTIONS.map((s, i) => (
                <button
                  key={i}
                  onClick={() => sendMessage(s)}
                  className="text-xs bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 rounded-full px-3 py-1.5 transition-colors"
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}
        <ChatBox messages={messages} isLoading={isLoading} />
        <InputBox onSend={sendMessage} isLoading={isLoading} />
      </div>
    </div>
  )
}

export default App
