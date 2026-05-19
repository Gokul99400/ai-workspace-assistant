# 🤖 AI Workspace Assistant

A beginner-friendly AI chatbot that helps you retrieve and understand task-related information using natural language queries.

Built with **React + FastAPI + Pandas + Ollama (Gemma 2B)**.

---

## 📋 Project Overview

This project demonstrates a full-stack AI application where:
- A **React frontend** provides a clean chat UI
- A **FastAPI backend** handles API requests
- **Pandas** filters task data based on user intent
- **Ollama (Gemma 2B)** formats the response conversationally

The system uses **keyword-based intent detection** (not LLMs) for task filtering — making it fast, reliable, and easy to understand.

---

## ✨ Features

- 💬 Chat-based interface for natural language queries
- 📊 Filters 100+ task records using Pandas
- 🧠 LLM-powered conversational response formatting
- 🔄 Graceful fallback if Ollama is not running
- ⚡ Quick suggestion chips for common queries
- 📱 Responsive design with Tailwind CSS

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|------------------------|
| Frontend  | React 18 + Vite + Tailwind CSS |
| HTTP      | Axios                  |
| Backend   | FastAPI + Uvicorn      |
| Data      | Pandas + CSV           |
| LLM       | Ollama (Gemma 2B)      |
| Language  | Python 3.10+, JavaScript |

---

## 📁 Folder Structure

```
ai-workspace-assistant/
│
├── backend/
│   ├── app.py              # FastAPI app + /chat endpoint
│   ├── chatbot.py          # Ollama LLM integration
│   ├── query_engine.py     # Intent detection + Pandas filtering
│   ├── requirements.txt    # Python dependencies
│   └── dataset/
│       ├── tasks.csv           # Generated task dataset
│       └── generate_dataset.py # Script to regenerate dataset
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBox.jsx      # Scrollable message list
│   │   │   ├── MessageBubble.jsx # Individual message bubble
│   │   │   └── InputBox.jsx     # Text input + send button
│   │   ├── App.jsx              # Root component
│   │   ├── main.jsx             # Entry point
│   │   └── index.css            # Global styles + Tailwind
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── README.md
├── .gitignore
└── github_link.txt
```

---

## 🚀 Installation & Setup

### Prerequisites

- Node.js 18+
- Python 3.10+
- [Ollama](https://ollama.com/) installed locally

---

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-workspace-assistant
```

---

### 2. Backend Setup

```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# (Optional) Regenerate the dataset
python dataset/generate_dataset.py

# Start the backend server
uvicorn app:app --reload
```

Backend will run at: `http://127.0.0.1:8000`

---

### 3. Frontend Setup

```bash
cd frontend

# Install Node dependencies
npm install

# Start the development server
npm run dev
```

Frontend will run at: `http://localhost:5173`

---

### 4. Install & Run Ollama

1. Download Ollama from [https://ollama.com/download](https://ollama.com/download)
2. Install and start Ollama
3. Pull the Gemma 2B model:

```bash
ollama pull gemma:2b
```

4. Ollama will run automatically at `http://localhost:11434`

> **Note:** The app works without Ollama — it will display raw task data instead of a formatted LLM response.

---

## 💬 Example Queries

| Query | What it does |
|-------|-------------|
| `Show high priority tasks` | Lists all High priority tasks |
| `What tasks are overdue?` | Shows tasks past their due date |
| `Show tasks assigned to Gokul` | Filters by owner name |
| `Show CRM project tasks` | Filters by project name |
| `What tasks are due today?` | Tasks with today's end date |
| `Show pending tasks` | To Do + In Progress tasks |
| `Show completed tasks` | Only Completed tasks |
| `Show in progress tasks` | Only In Progress tasks |

---

## 🏗️ Architecture

```
User Query
    │
    ▼
React Frontend (Axios POST)
    │
    ▼
FastAPI /chat endpoint
    │
    ├─► Intent Detection (keyword matching)
    │
    ├─► Pandas Filter (CSV data)
    │
    └─► Ollama LLM (response formatting)
         │
         ▼
    Formatted Response → Frontend
```

---

## 📸 Screenshots

> Add screenshots here after running the project.

1. **Chat Interface** — Clean, minimal chat UI
2. **Query Results** — Task list formatted by AI
3. **Quick Suggestions** — One-click query chips

---

## 🔮 Future Improvements

- [ ] Add date range filtering ("tasks due this week")
- [ ] Export filtered results as CSV
- [ ] Dark mode toggle
- [ ] Persistent chat history
- [ ] Multi-project support with upload
- [ ] Charts and analytics dashboard
- [ ] Voice input support

---

## 👨‍💻 Author

Built as part of a Software Engineer Internship assignment.

---


