import logging

# Basic Logging

logging.basicConfig(level=logging.DEBUG)

logging.info("Application started")  # noqa: LOG015
logging.info("User logged in")  # noqa: LOG015
logging.info("Study session started")  # noqa: LOG015
logging.info("Study session completed")  # noqa: LOG015
logging.info("Application stopped")  # noqa: LOG015

# Different Levels

logging.debug("This program is logging")  # noqa: LOG015
logging.info("Loading AI model")  # noqa: LOG015
logging.warning("30% Percent remaining")  # noqa: LOG015
logging.error("Processing failed")  # noqa: LOG015
logging.critical("Heavy damages has been done to this system.")  # noqa: LOG015

# Exception Logging

try:
    result = 10 / 0
    logging.debug(result)  # noqa: LOG015
except ZeroDivisionError:
    logging.exception("A zero error occurred")  # noqa: LOG015

# AI Logger 

def generate_response(prompt):
    logging.info(f"Received prompt: {prompt}")  # noqa: LOG015
    logging.info("Generating AI response")  # noqa: LOG015

    response = f"AI response to: {prompt}"

    logging.info("Response generated")  # noqa: LOG015

    return response

response = generate_response("Explain Python logging")
print(response)

# StudyBot Logger

def study_bot (name):

    try:
        result = 15 / 0
        logging.info(result)  # noqa: LOG015
    except ZeroDivisionError:
        logging.exception(f"{name}: Something went wrong")  # noqa: LOG015

    return f"{name} finished processing"

print(study_bot("Evelyn AI"))
