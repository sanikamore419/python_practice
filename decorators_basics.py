"""
decorators_basics.py
--------------------
Author: [Your Name]
Date: Today

Purpose:
    Introduce Python decorators, including:
    - Simple function decorators
    - Decorators with arguments
    - Preserving metadata with functools.wraps
    - Multiple decorators on one function
"""

from functools import wraps
import time

# ---------------------------
# 1. Basic Decorator
# ---------------------------
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs...")
        result = func()
        print("After function runs...")
        return result
    return wrapper

@my_decorator
def say_hello():
    """Prints hello message."""
    print("Hello!")

# ---------------------------
# 2. Decorator for Timing
# ---------------------------
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱ {func.__name__} executed in {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Finished slow task!"
