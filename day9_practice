# Day 9 Python Practice - All in One

# 1. Find factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# 2. Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 3. Check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

# 4. Find largest number in a list
def largest_number(arr):
    return max(arr)

# 5. Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

# 6. Reverse a string
def reverse_string(s):
    return s[::-1]

# 7. Find prime numbers in a range
def primes_in_range(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# 8. Sort a list
def sort_list(arr):
    return sorted(arr)

# 9. Count frequency of elements in list
def frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq


# ------------------- TESTING -------------------
if __name__ == "__main__":
    print("Factorial(5):", factorial(5))
    print("Fibonacci(6):", fibonacci(6))
    print("Is 'madam' Palindrome?:", is_palindrome("madam"))
    print("Largest Number:", largest_number([2, 8, 4, 10, 5]))
    print("Vowel Count in 'hello world':", count_vowels("hello world"))
    print("Reverse of 'Python':", reverse_string("Python"))
    print("Primes till 20:", primes_in_range(20))
    print("Sorted List:", sort_list([5, 1, 9, 3, 7]))
    print("Frequency:", frequency([1, 2, 2, 3, 1, 4, 2]))
