"""
query_engine.py
Handles keyword detection and Pandas-based filtering of task data.
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

# Load dataset once when the module is imported.
# Use an absolute path relative to this file so it works regardless of cwd.
DATASET_PATH = Path(__file__).resolve().parent / "dataset" / "tasks.csv"

df = pd.read_csv(DATASET_PATH)
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["End Date"] = pd.to_datetime(df["End Date"])



def detect_intent(message: str) -> dict:
    """
    Detect the user's intent based on keyword matching.
    Returns a dict with intent type and optional parameters.
    """
    msg = message.lower()

    # Check for owner name mentions
    owners = df["Owner"].str.lower().unique()
    for owner in owners:
        if owner in msg:
            return {"intent": "by_owner", "owner": owner}

    # Check for project name mentions
    projects = df["Project Name"].str.lower().unique()
    for project in projects:
        # Match partial project names (e.g., "crm" matches "crm system")
        project_short = project.split()[0]
        if project_short in msg or project in msg:
            return {"intent": "by_project", "project": project}

    # Keyword-based intent detection
    if any(word in msg for word in ["today", "due today", "today's"]):
        return {"intent": "due_today"}

    if any(word in msg for word in ["overdue", "past due", "missed", "late"]):
        return {"intent": "overdue"}

    if any(word in msg for word in ["pending", "incomplete", "not done", "remaining"]):
        return {"intent": "pending"}

    if any(word in msg for word in ["high priority", "urgent", "critical", "high"]):
        return {"intent": "high_priority"}

    if any(word in msg for word in ["completed", "done", "finished", "closed"]):
        return {"intent": "completed"}

    if any(word in msg for word in ["in progress", "ongoing", "active", "working"]):
        return {"intent": "in_progress"}

    if any(word in msg for word in ["all tasks", "list all", "show all", "everything"]):
        return {"intent": "all_tasks"}

    return {"intent": "unknown"}


def filter_tasks(intent: dict) -> pd.DataFrame:
    """
    Apply Pandas filters based on the detected intent.
    Returns a filtered DataFrame.
    """
    today = pd.Timestamp(datetime.today().date())

    intent_type = intent.get("intent")

    if intent_type == "due_today":
        return df[df["End Date"].dt.date == today.date()]

    elif intent_type == "overdue":
        return df[
            (df["End Date"] < today) &
            (df["Status"] != "Completed")
        ]

    elif intent_type == "pending":
        return df[df["Status"].isin(["To Do", "In Progress"])]

    elif intent_type == "high_priority":
        return df[df["Priority"] == "High"]

    elif intent_type == "completed":
        return df[df["Status"] == "Completed"]

    elif intent_type == "in_progress":
        return df[df["Status"] == "In Progress"]

    elif intent_type == "by_owner":
        owner = intent.get("owner", "").title()
        return df[df["Owner"].str.lower() == owner.lower()]

    elif intent_type == "by_project":
        project = intent.get("project", "")
        return df[df["Project Name"].str.lower() == project.lower()]

    elif intent_type == "all_tasks":
        return df.head(20)

    else:
        # Default: return a sample of tasks
        return df.head(10)


def format_tasks_for_llm(filtered_df: pd.DataFrame) -> str:
    """
    Convert filtered DataFrame to a clean text format for the LLM.
    """
    if filtered_df.empty:
        return "No tasks found matching your query."

    # Limit to top 10 results to keep LLM input concise
    sample = filtered_df.head(10)

    lines = []
    for _, row in sample.iterrows():
        lines.append(
            f"- Task: {row['Task Name']} | Owner: {row['Owner']} | "
            f"Project: {row['Project Name']} | Priority: {row['Priority']} | "
            f"Status: {row['Status']} | Due: {row['End Date'].strftime('%Y-%m-%d')}"
        )

    total = len(filtered_df)
    summary = f"Found {total} task(s). Showing top {len(sample)}:\n"
    return summary + "\n".join(lines)
