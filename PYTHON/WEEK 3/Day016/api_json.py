import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

data = response.json()

print("User ID:", data["userId"])
print("Todo ID:", data["id"])
print("Title:", data["title"])
print("Completed:", data["completed"])