# Day 11 - Python Practice

import math
import random
import datetime
import os
import time
from functools import wraps

print("===== Day 11 Practice =====")

# 1. Modules & Packages
print("\n--- Modules ---")
print("Square root of 25:", math.sqrt(25))
print("Random number (1-100):", random.randint(1, 100))
print("Today:", datetime.date.today())
print("Current directory:", os.getcwd())

# 2. Iterators
print("\n--- Iterators ---")
class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current

for val in CountDown(5):
    print(val, end=" ")
print()

# 3. Generators
print("\n--- Generators ---")
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("First 10 Fibonacci:", list(fibonacci_gen(10)))

# Infinite generator (stop manually)
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter), end=" ")
print()

# 4. Decorators
print("\n--- Decorators ---")
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.6f} sec")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Finished!"

print(slow_function())

# 5. Practice Problems
print("\n--- Practice Problems ---")

# Random password generator
def generate_password(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))

print("Random Password:", generate_password(12))

# Most frequent word in a sentence
def most_frequent_word(sentence):
    words = sentence.split()
    counter = Counter(words)
    return counter.most_common(1)[0]

text = "python code practice python learning python code"
print("Most frequent word:", most_frequent_word(text))
