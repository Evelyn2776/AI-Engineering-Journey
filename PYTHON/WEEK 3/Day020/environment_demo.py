import os

name = os.getenv("USER_NAME", "Guest")

print("Hello,", name)