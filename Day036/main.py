# Basic Context Manager
class Demo:

    def __enter__(self):
        print("Entering context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving context")


with Demo():
    print("Inside context")


# Context Manager With return
class AIModel:

    def __enter__(self):
        print("Model loaded")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Model unloaded")


with AIModel() as model:
    print("Running AI model")


# Build Your Own Resource Manager
class Resource:

    def __enter__(self):
        print("Resource opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")

    def use(self):
        print("Using resource")


with Resource() as resource:
    resource.use()


# AI Model Resource Manager
class AIModelResource:

    def __enter__(self):
        print("Model loading...")
        print("Model ready")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Model shutting down...")

    def generate(self, prompt):
        print(f"Generating response for: {prompt}")


with AIModelResource() as model:
    model.generate("Explain Python iterators")


# Exception Handling
class SafeOperation:

    def __enter__(self):
        print("Operation started")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Operation cleaned up")


try:
    with SafeOperation():
        print("Doing work")
        raise ValueError("Test error")

except ValueError as error:
    print(f"Error: {error}")