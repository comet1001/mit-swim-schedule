import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the swimming pool schedule
URL = "https://www.mitrecsports.com/pool-schedule-z/?week=1"

# Send request and get page content
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract pool schedule (modify based on actual structure)
schedule_data = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    day_section = soup.find("div", {"id": f"schedule-{day.lower()}"})  # Modify if needed
    if day_section:
        slots = day_section.find_all("div", class_="schedule-slot")
        for slot in slots:
            pool_name = slot.find("div", class_="pool-name").text.strip()
            activity = slot.find("div", class_="activity-name").text.strip()
            time_range = slot.find("div", class_="time-range").text.strip()

            if pool_name == "TEACHING POOL" and activity == "Open Rec Swim":
                schedule_data.append({"day": day, "time": time_range})

# Save extracted data to JSON
with open("schedule.json", "w") as json_file:
    json.dump(schedule_data, json_file, indent=4)

print("Scraped data saved to schedule.json")
