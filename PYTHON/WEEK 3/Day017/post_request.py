import requests

data = {
    "name": "Evelyn",
    "career": "AI Engineer"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print("Status:", response.status_code)
print("Response:", response.text)