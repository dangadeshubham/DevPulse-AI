import random
from datetime import datetime
import pytz
import subprocess

# Timezone
tz = pytz.timezone("Asia/Kolkata")
now = datetime.now(tz)

# Files
files = ["daily_log.txt", "progress.md", "inspiration.txt"]

# Messages
messages = [
    "Improving consistency 🚀",
    "Learning something new 📚",
    "Working on skills 💻",
    "Small progress today 🌱",
    "Consistency is key 🔥",
    "Debugging and refining 🛠️",
    "Exploring new ideas 💡",
    "Building habits step by step 📈"
]

# 🔥 Random number of commits per run
num_commits = random.randint(2, 8)

for _ in range(num_commits):
    file_to_update = random.choice(files)

    content = f"[{now.strftime('%Y-%m-%d %I:%M:%S %p')}] - {random.choice(messages)}\n"

    # Write to file
    with open(file_to_update, "a") as f:
        f.write(content)

    # Commit each change separately
    subprocess.run(["git", "add", file_to_update])
    subprocess.run(["git", "commit", "-m", random.choice(messages)])

# Log
with open("commit_log.txt", "a") as log:
    log.write(f"{now} -> {num_commits} commits made\n")

print(f"{num_commits} commits created successfully")
