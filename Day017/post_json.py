import requests

data = {
    "name": "Evelyn",
    "career": "AI Engineer"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

result = response.json()

print("Status:", response.status_code)
print("ID:", result["id"])
print("Name:", result["name"])
print("Career:", result["career"])