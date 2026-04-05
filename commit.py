import random
from datetime import datetime
import pytz

# Timezone
tz = pytz.timezone("Asia/Kolkata")
now = datetime.now(tz)

# Files
files = ["daily_log.txt", "progress.md", "inspiration.txt"]
file_to_update = random.choice(files)

# Messages
messages = [
    "Improving consistency 🚀",
    "Learning something new 📚",
    "Working on skills 💻",
    "Small progress today 🌱",
    "Consistency is key 🔥"
]

content = f"[{now.strftime('%Y-%m-%d %I:%M:%S %p')}] - {random.choice(messages)}\n"

# Write to file
with open(file_to_update, "a") as f:
    f.write(content)

# Log
with open("commit_log.txt", "a") as log:
    log.write(content)

print("Commit content generated successfully")
