import random
import datetime

name = input("Enter your name: ")

messages = ["Very good. Keep it up", "Perfect. very wonderful!", "Good. How magnificent"]
comments = ["Have a good study session!", "Keep up the great work!!", "You are doing pretty great!!!"]
message = random.choice(messages)
comment = random.choice(comments)

date = datetime.date.today()

print("------------------------------")
print("AI ENGINEERING STUDY ASSISTANT")
print("------------------------------\n")
print(f"Name: {name}\n")
print(f"Date: {date}\n")
print(f"Today's message: {message}\n")
print(comment)