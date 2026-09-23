import json

profile = {
    "name": "Evelyn",
    "age": 23,
    "country": "Nigeria",
    "career": "AI Engineer",
    "goal": "Become a great AI Engineer"
}

with open("new_profile.json", "w") as file:
    json.dump(profile, file, indent=4)

print("Profile saved successfully.")