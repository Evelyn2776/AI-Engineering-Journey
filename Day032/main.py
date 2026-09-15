# Varable Type Hint
name: str = "Evelyn"
age: int = 23
height: float = 168.7
is_student: bool = False

# Function and Ruturn Type Hints
def calculate_total(price: int, quantity: int) -> int:
    return price * quantity

# Collection Type Hints
# For a list
skills: list[str] = ["cooking","cleaning"]

# For a tuple
scores: tuple[int, ...] = (50, 70, 30)

# For a dictionary
student: dict[str, int] = {
    "Age": 20,
    "Mark": 15
}

# Union Type Hint
name: str | list[str] = "Evelyn"

def generate_response(prompt: str) -> str:
    return f"AI response to: {prompt}"

print(generate_response("Start"))