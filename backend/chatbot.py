import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma:2b"


def generate_response(user_message: str, task_data: str) -> str:
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
                "stream": False,
            },
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Sorry, I could not generate a response.")
        else:
            return fallback_response(task_data)

    except requests.exceptions.ConnectionError:
        return fallback_response(task_data)

    except Exception as e:
        return f"An error occurred: {str(e)}\n\n{fallback_response(task_data)}"


def fallback_response(task_data: str) -> str:
    if "No tasks found" in task_data:
        return "No tasks found matching your query. Try asking about high priority tasks, overdue tasks, or tasks by owner."

    return (
        "Here are the matching tasks from your workspace:\n\n"
        + task_data
        + "\n\n_(Note: AI formatting unavailable. Ollama may not be running.)_"
    )
