# Day 10 - Python Practice

# 1. Sets & Dictionary Practice
print("---- Set & Dictionary Practice ----")
# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Dictionary operations
my_dict = {'a': 10, 'b': 20, 'c': 30}
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Get 'b':", my_dict.get('b'))
my_dict.update({'d': 40})
print("Updated Dictionary:", my_dict)

# 2. List & Dictionary Comprehensions
print("\n---- Comprehensions ----")
# List comprehension
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Squares of even numbers:", squares)

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 11)}
print("Square Dictionary:", square_dict)

# 3. Lambda, Map, Filter, Reduce
print("\n---- Lambda, Map, Filter, Reduce ----")
from functools import reduce

nums = [1, 2, 3, 4, 5]

# Lambda with map
squared_nums = list(map(lambda x: x**2, nums))
print("Squared using map:", squared_nums)

# Filter odd numbers
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print("Odd numbers:", odd_nums)

# Reduce - product of all numbers
product = reduce(lambda x, y: x * y, nums)
print("Product using reduce:", product)

# 4. Exception Handling
print("\n---- Exception Handling ----")
try:
    x = int(input("Enter a number to divide 100 by: "))
    print("Result:", 100 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution complete.")

# 5. File Handling
print("\n---- File Handling ----")
numbers = [1, 2, 3, 4, 5]
with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")

# Read file and sum numbers
with open("numbers.txt", "r") as f:
    total = sum(int(line.strip()) for line in f)
print("Sum of numbers from file:", total)

# 6. Small Practice Problems
print("\n---- Practice Problems ----")

# Palindrome Checker
def is_palindrome(s):
    return s == s[::-1]

word = "radar"
print(f"Is '{word}' a palindrome?:", is_palindrome(word))

# Fibonacci Sequence
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:n]

print("First 10 Fibonacci numbers:", fibonacci(10))

# Prime Numbers in Range
def primes_upto(n):
    result = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            result.append(num)
    return result

print("Primes up to 50:", primes_upto(50))

# Most Frequent Element
from collections import Counter
lst = [1, 2, 2, 3, 3, 3, 4]
freq = Counter(lst)
most_common = freq.most_common(1)[0][0]
print("Most frequent element:", most_common)
