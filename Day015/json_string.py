import json

profile = {
    "name": "Evelyn",
    "career": "AI Engineer"
}

json_text = json.dumps(profile)

print(json_text)
print(type(json_text))