import os
import random
from datetime import datetime

# IRON BOT - Bodybuilding Video Planner

IDEAS = [
    {
        "title": "3 BEST ABS EXERCISES",
        "exercises": ["CRUNCHES", "LEG RAISES", "PLANK"]
    },
    {
        "title": "BUILD STRONGER ARMS",
        "exercises": ["BICEP CURLS", "HAMMER CURLS", "PUSH UPS"]
    },
    {
        "title": "CHEST WORKOUT",
        "exercises": ["PUSH UPS", "DUMBBELL PRESS", "CHEST FLY"]
    },
    {
        "title": "BUILD BIGGER SHOULDERS",
        "exercises": ["SHOULDER PRESS", "LATERAL RAISES", "FRONT RAISES"]
    }
]

def create_daily_idea():
    today = datetime.now().strftime("%Y-%m-%d")
    random.seed(today)
    idea = random.choice(IDEAS)

    os.makedirs("videos", exist_ok=True)

    with open("videos/daily_idea.txt", "w") as file:
        file.write(f"IRON BOT - {today}\n")
        file.write(f"TITLE: {idea['title']}\n\n")
        for exercise in idea["exercises"]:
            file.write(f"- {exercise}\n")

    print("Daily bodybuilding idea created!")
    print(idea["title"])

if __name__ == "__main__":
    create_daily_idea()
