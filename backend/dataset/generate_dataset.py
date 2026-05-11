import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

owners = ["Gokul", "Priya", "Arjun", "Sneha", "Rahul", "Divya", "Karthik", "Meena"]
projects = ["CRM System", "Mobile App", "Data Pipeline", "Web Portal", "AI Module", "ERP Upgrade", "Cloud Migration"]
priorities = ["High", "Medium", "Low"]
statuses = ["To Do", "In Progress", "Completed"]

task_templates = [
    "Design {} module", "Implement {} feature", "Test {} component",
    "Review {} code", "Deploy {} service", "Fix {} bug", "Update {} documentation",
    "Optimize {} performance", "Integrate {} API", "Refactor {} logic",
    "Create {} dashboard", "Configure {} settings", "Analyze {} data",
    "Setup {} environment", "Migrate {} database",
]

nouns = ["login", "dashboard", "report", "notification", "search", "export",
         "authentication", "payment", "profile", "settings", "analytics",
         "backup", "scheduler", "API", "cache"]

today = datetime.today()

records = []
for i in range(100):
    task_name = random.choice(task_templates).format(random.choice(nouns))
    owner = random.choice(owners)
    project = random.choice(projects)
    priority = random.choice(priorities)

    # Mix of past, present, future dates
    start_offset = random.randint(-60, 10)
    duration = random.randint(3, 30)
    start_date = today + timedelta(days=start_offset)
    end_date = start_date + timedelta(days=duration)

    # Determine status based on dates
    if end_date.date() < today.date():
        status = random.choice(["Completed", "In Progress"])  # some overdue
    elif start_date.date() > today.date():
        status = "To Do"
    else:
        status = random.choice(statuses)

    records.append({
        "Task Name": task_name.title(),
        "Owner": owner,
        "Start Date": start_date.strftime("%Y-%m-%d"),
        "End Date": end_date.strftime("%Y-%m-%d"),
        "Project Name": project,
        "Priority": priority,
        "Status": status,
    })

df = pd.DataFrame(records)
df.to_csv("tasks.csv", index=False)
print(f"Generated {len(df)} task records -> tasks.csv")
