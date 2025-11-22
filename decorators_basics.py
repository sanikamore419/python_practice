
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

# ---------------------------
# 3. Decorator With Arguments
# ---------------------------
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Iteration {i+1}/{times}")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# ---------------------------
# 4. Multiple Decorators Example
# ---------------------------
@timer
@my_decorator
def combined():
    print("Running combined decorators example...")

# ---------------------------
# Run Tests
# ---------------------------
if __name__ == "__main__":
    say_hello()
    print()

    print(slow_function())
    print()

    greet("Alice")
    print()

    combined()
