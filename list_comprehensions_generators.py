"""
File: list_comprehensions_generators.py
Description:
    This file covers:
    - List Comprehensions
    - Set Comprehensions
    - Dictionary Comprehensions
    - Nested Comprehensions
    - Generator Expressions
    - Generator Functions (yield)
    - Difference between List vs Generator (Memory)
"""

# -----------------------------------------------
# 1. LIST COMPREHENSIONS
# -----------------------------------------------

# Normal method
squares_normal = []
for i in range(1, 6):
    squares_normal.append(i * i)

# List comprehension method
squares_comp = [i * i for i in range(1, 6)]
print("Squares:", squares_comp)


# -----------------------------------------------
# 2. LIST COMPREHENSION WITH CONDITIONS
# -----------------------------------------------

# Even numbers from 1 to 10
evens = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers:", evens)

# Numbers divisible by 3
div3 = [i for i in range(1, 21) if i % 3 == 0]
print("Divisible by 3:", div3)


# -----------------------------------------------
# 3. NESTED LIST COMPREHENSION
# -----------------------------------------------

matrix = [[j for j in range(1, 4)] for i in range(3)]
print("Matrix:", matrix)

pairs = [(x, y) for x in range(3) for y in range(3)]
print("Pairs:", pairs)


# -----------------------------------------------
# 4. SET COMPREHENSIONS
# -----------------------------------------------

nums = {i * 2 for i in range(5)}
print("Set comprehension:", nums)


# -----------------------------------------------
# 5. DICTIONARY COMPREHENSIONS
# -----------------------------------------------

# Mapping numbers to their squares
square_dict = {i: i * i for i in range(1, 6)}
print("Dict comprehension:", square_dict)

# Convert keys to uppercase
name_age = {"rama": 20, "sita": 22}
upper_dict = {name.upper(): age for name, age in name_age.items()}
print("Upper-case dict:", upper_dict)


# -----------------------------------------------
# 6. GENERATOR EXPRESSIONS
# -----------------------------------------------

# List comprehension → creates full list in memory
list_comp = [i * i for i in range(1, 10001)]

# Generator expression → doesn't create full list
gen_exp = (i * i for i in range(1, 10001))

print("List comprehension size:", len(list_comp))
print("Generator expression object:", gen_exp)  # not expanded


# -----------------------------------------------
# 7. GENERATOR FUNCTION (yield)
# -----------------------------------------------

def counter_gen(n):
    """A simple generator that yields numbers from 1 to n"""
    i = 1
    while i <= n:
        yield i
        i += 1

print("Generator function output:")
for num in counter_gen(5):
    print(num)


# -----------------------------------------------
# 8. PRACTICAL EXAMPLES
# -----------------------------------------------

# Extract first letters
words = ["apple", "banana", "cat", "dog"]
first_letters = [w[0] for w in words]
print("First letters:", first_letters)

# Square only even numbers
even_squares = [i*i for i in range(1, 11) if i % 2 == 0]
print("Even squares:", even_squares)

# Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sub in nested for num in sub]
print("Flattened list:", flat)


# -----------------------------------------------
# 9. LIST VS GENERATOR MEMORY DIFFERENCE
# -----------------------------------------------

import sys

big_list = [i for i in range(100000)]
big_gen = (i for i in range(100000))

print("Memory used by list:", sys.getsizeof(big_list), "bytes")
print("Memory used by generator:", sys.getsizeof(big_gen), "bytes")

# Generators save a LOT of memory!
