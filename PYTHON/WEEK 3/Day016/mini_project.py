import requests

try:
    response = requests.get("https://randomuser.me/api/")
    response.raise_for_status()

    data = response.json()

    user = data["results"][0]

    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    country = user["location"]["country"]
    email = user["email"]

    print("------------------------------\n")
    print("RANDOM USER INFORMATION\n")
    print("------------------------------\n\n")
    print(f"Name: {first_name} {last_name}\n")
    print(f"Country: {country}\n")
    print(f"Email: {email}\n")

except requests.exceptions.RequestException as erorr:
    print(f"Request Failed: {erorr}")