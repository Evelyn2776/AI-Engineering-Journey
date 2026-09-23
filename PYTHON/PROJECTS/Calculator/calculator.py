# Calculator
class Calculator:

    
    def __init__(self, number1: float, number2: float):
        self.number1 = number1
        self.number2 = number2


    def add(self) -> float:
        return self.number1 + self.number2


    def subtract(self) -> float:
        return self.number1 - self.number2


    def multiply(self) -> float:
        return self.number1 * self.number2


    def power(self) -> float:
        return self.number1 ** self.number2


    def divide(self) -> float:
        if self.number2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return self.number1 / self.number2