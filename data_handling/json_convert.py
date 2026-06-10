# write data to a json file and then read it back

import json

data = {
    "name": "Alex",
    "id": 101,
    "skills": ["Python", "Data Analysis", "Automation"],
    "active": True
}

# 2. Writing to a JSON file
# 'w' mode creates the file or overwrites it
with open('user_data.json', 'w') as json_file:
    # indent=4 makes the file human-readable with pretty printing
    json.dump(data, json_file, indent=4)

print("Data successfully written to user_data.json")

# 3. Reading from a JSON file
with open('user_data.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print("\nData retrieved from file:")
print(f"Name: {loaded_data['name']}")
print(f"Skills: {', '.join(loaded_data['skills'])}")