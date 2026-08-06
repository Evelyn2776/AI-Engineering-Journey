print("--- TO DO LIST ---")
task1 = input("Task 1: ")
task2 = input("Task 2: ")
task3 = input("Task 3: ")

with open("todo.txt", "a") as file:
    file.write(f"Task1: {task1}\n")
    file.write(f"Task2: {task2}\n")
    file.write(f"Task3: {task3}\n")

with open("todo.txt", "r") as file:
    print(file.read())