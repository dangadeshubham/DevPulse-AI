import os
import random
from datetime import datetime
import pytz

# Set timezone (India)
tz = pytz.timezone("Asia/Kolkata")
now = datetime.now(tz)

# Random file selection
files = ["daily_log.txt", "progress.md", "inspiration.txt"]

file_to_update = random.choice(files)

# Random content
messages = [
    "Improving consistency 🚀",
    "Learning something new 📚",
    "Working on skills 💡",
    "Small progress today ✔️",
    "Consistency is key 🔥"
]

content = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {random.choice(messages)}\n"

# Write to file
with open(file_to_update, "a") as f:
    f.write(content)

# Also log commits
with open("commit_log.txt", "a") as log:
    log.write(content)

print("Commit content generated successfully")
