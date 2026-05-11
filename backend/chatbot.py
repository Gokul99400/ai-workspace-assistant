"""
chatbot.py
Handles communication with the local Ollama LLM.
"""

import requests
import json

# Ollama API endpoint (runs locally)
OLLAMA_URL = "http://localhost:11434/api/generate"

# Use gemma:2b or llama3 — whichever is installed
MODEL_NAME = "gemma:2b"


def generate_response(user_message: str, task_data: str) -> str:
    """
    Send the user query and filtered task data to Ollama.
    Returns a conversational response string.
    """

    # Build a clear prompt for the LLM
    prompt = f"""You are a helpful AI Workspace Assistant. A user asked: "{user_message}"

Here is the relevant task data retrieved from the system:

{task_data}

Please provide a clear, concise, and friendly response summarizing this information.
Keep the response under 150 words. Use bullet points if listing multiple tasks.
Do not make up any information beyond what is provided above."""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,  # Get full response at once
            },
            timeout=60  # 60 second timeout
        )

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Sorry, I could not generate a response.")
        else:
            # Fallback: return the raw task data if LLM fails
            return fallback_response(task_data)

    except requests.exceptions.ConnectionError:
        # Ollama is not running — return formatted task data directly
        return fallback_response(task_data)

    except Exception as e:
        return f"An error occurred: {str(e)}\n\n{fallback_response(task_data)}"


def fallback_response(task_data: str) -> str:
    """
    Return a simple formatted response when Ollama is unavailable.
    """
    if "No tasks found" in task_data:
        return "No tasks found matching your query. Try asking about high priority tasks, overdue tasks, or tasks by owner."

    return (
        "Here are the matching tasks from your workspace:\n\n"
        + task_data
        + "\n\n_(Note: AI formatting unavailable. Ollama may not be running.)_"
    )
