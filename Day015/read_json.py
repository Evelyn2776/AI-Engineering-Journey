import json
from pathlib import Path

file_path = Path(__file__).parent / "profile.json"

with open(file_path, "r") as file:
    profile = json.load(file)

print("Name:", profile["name"])
print("Country:", profile["country"])
print("Career:", profile["career"])
print("Goal:", profile["goal"])