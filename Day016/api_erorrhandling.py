import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    print("Title:", data["title"])

except requests.RequestException as error:
    print("Request failed:", error)