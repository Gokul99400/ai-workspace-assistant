from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from query_engine import detect_intent, filter_tasks, format_tasks_for_llm
from chatbot import generate_response


app = FastAPI(
    title="AI Workspace Assistant",
    description="A chatbot that answers queries about your workspace tasks.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def root():
    return {"status": "AI Workspace Assistant is running!"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_message = request.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    intent = detect_intent(user_message)
    filtered_df = filter_tasks(intent)
    task_text = format_tasks_for_llm(filtered_df)
    reply = generate_response(user_message, task_text)

    return ChatResponse(reply=reply)
