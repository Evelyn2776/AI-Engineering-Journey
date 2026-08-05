class Cup:
    def __init__(self, color):
        self.color = color

blue_cup = Cup("blue")
print(blue_cup.color)

class Cup:
    def __init__(self):
        self.contents = "empty"

my_cup = Cup()
my_cup.contents = "Mocha"
print(my_cup.contents)

class Cup:
    def greet(self):
        print("Ready for coffee!")

my_cup = Cup()
my_cup.greet()

class Cup:
    def __init__(self):
        self.ounces = 5
    def drink(self, amt):
        if amt > self.ounces:
            print("Not enough liquid!")
        else:
            self.ounces -= amt

my_cup = Cup()
my_cup.drink(10)
print(my_cup.ounces)

class TestCup:
    def __init__(self):
        print("Stamped!")

cup_instance = TestCup()

class Cup:
    def __init__(self):
        self.material = "paper"

my_cup = Cup()
print(my_cup.material)