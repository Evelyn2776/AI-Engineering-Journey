import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("USER_NAME")
career = os.getenv("CAREER")
country = os.getenv("COUNTRY")

print("----------------------------")
print("AI ENGINEERING PROFILE")
print("----------------------------\n")
print("Name:", name)
print("Career:", career)
print("Country:", country)