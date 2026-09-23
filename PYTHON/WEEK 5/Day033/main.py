# Function as an Object
def say_hello ():
    print("Hello, everyone")

hi = say_hello
hi()

# Function as an Argument
def execute(function):
    function()

execute(say_hello)

# Nested Function
def outer(name):

    def inner():
        print(name)
    inner()

outer("Evelyn")

#  Basic Decorator
def basic_decorator(function):

    def wrapper():

        print("Before")
        function()
        print("After")

    return wrapper

@basic_decorator
def hello():
    print("Hello")

hello()

# Decorator With Arguments
def moment(function):

    def wrapper(*args, **kwargs):

        print("Before")
        result = function(*args, **kwargs)
        print("After")

        return result

    return wrapper

@moment
def greet(name):
    print(f"Hello, {name}")

greet("Ayodele")

# AI Logger
def log_call (function):

    def explain (*args, **kwargs):

        print("Calling generate_response")
        output = function(*args, **kwargs)
        print("Function finished")

        return output

    return explain

@log_call
def generate_response(prompt):
    return f"AI response to: {prompt}"

response = generate_response("Explain Python")
print(response)