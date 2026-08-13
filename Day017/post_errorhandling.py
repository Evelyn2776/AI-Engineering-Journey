import requests

data = {
    "name": "Evelyn",
    "career": "AI Engineer"
}

try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data,
        timeout=5
    )

    response.raise_for_status()

    result = response.json()

    print("Created successfully!")
    print("ID:", result["id"])
    print("Name:", result["name"])
    print("Career:", result["career"])

except requests.RequestException as error:
    print("Request failed:", error)