"""
error_handling_advanced.py
Author: Sanika
Description:
    This module demonstrates advanced Python exception handling,
    including custom exceptions, multiple exception blocks,
    raising errors, finally block, and logging.
"""

import logging

# ----------------------------
# Configure Logging
# ----------------------------
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --------------------------------
# Custom Exception Class
# --------------------------------
class InvalidAgeError(Exception):
    """Custom exception raised when age is invalid."""
    pass


# --------------------------------
# Function using custom exceptions
# --------------------------------
def validate_age(age):
    """Validate age and raise custom exception if invalid."""
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
    elif age > 120:
        raise InvalidAgeError("Age cannot be more than 120!")
    else:
        return "Valid age."


# --------------------------------
# Demonstrating try-except-else-finally
# --------------------------------
def divide_numbers(a, b):
    try:
        logging.info(f"Trying to divide {a} by {b}")
        result = a / b
    except ZeroDivisionError:
        logging.error("Attempted division by zero!")
        return "Error: Cannot divide by zero."
    except TypeError:
        logging.error("Invalid input type encountered!")
        return "Error: Please enter numbers only."
    else:
        logging.info("Division successful.")
        return f"Result: {result}"
    finally:
        print("Operation complete (finally block executed).")


# --------------------------------
# Testing the functions
# --------------------------------
if __name__ == "__main__":

    # Test divide_numbers()
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))
    print(divide_numbers("10", 2))

    # Test custom exception
    try:
        print(validate_age(-5))
    except InvalidAgeError as e:
        print("Caught custom exception:", e)

    try:
        print(validate_age(150))
    except InvalidAgeError as e:
        print("Caught custom exception:", e)

    print(validate_age(25))
