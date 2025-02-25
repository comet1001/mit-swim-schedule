import json

# Load extracted data
with open("schedule.json", "r") as json_file:
    schedule_data = json.load(json_file)

# Create HTML content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Open Rec Swim - Teaching Pool</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        h1 { color: #0073e6; }
        table { margin: auto; border-collapse: collapse; width: 60%; }
        th, td { padding: 10px; border: 1px solid #ddd; }
        th { background-color: #0073e6; color: white; }
    </style>
</head>
<body>
    <h1>Available Open Rec Swim Time Slots - Teaching Pool</h1>
    <table>
        <tr>
            <th>Day</th>
            <th>Time</th>
        </tr>"""

for entry in schedule_data:
    html_content += f"""
        <tr>
            <td>{entry['day']}</td>
            <td>{entry['time']}</td>
        </tr>"""

html_content += """
    </table>
</body>
</html>
"""

# Save the HTML file
with open("index.html", "w") as file:
    file.write(html_content)

print("Generated index.html for GitHub Pages")
