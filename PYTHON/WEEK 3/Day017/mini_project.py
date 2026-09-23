import requests

name = input("Name: ")
country = input("Country: ")
career = input("Career: ")

student_profile = {
    "Name": name,
    "Country": country,
    "Career": career
}

try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=student_profile
    )

    response.raise_for_status()
    result = response.json()

    print("----------------------------")
    print("STUDENT PROFILE")
    print("----------------------------\n")
    print("Name: ", result["Name"])
    print("Country: ",result["Country"])
    print("Career: ", result["Career"])
    print("\n")
    print("Profile sent successfully!")
    print("Server ID: ", result["id"])

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
