activity = input("What did you do today?")

with open("daily_journal.txt", "a") as file:
    file.write("\n" + activity)
