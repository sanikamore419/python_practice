# Day 3: Operators in Python

# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)   # float division
print("a // b =", a // b) # floor division
print("a % b =", a % b)
print("a ** b =", a ** b) # exponent

print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)

print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\nAssignment Operators:")
c = 5
c += 3
print("c after += 3:", c)
c *= 2
print("c after *= 2:", c)

print("\nBitwise Operators:")
print("a & b:", a & b)   # AND
print("a | b:", a | b)   # OR
print("a ^ b:", a ^ b)   # XOR
print("~a:", ~a)         # NOT
print("a << 1:", a << 1) # left shift
print("a >> 1:", a >> 1) # right shift

print("\nMembership Operators:")
nums = [1, 2, 3, 4, 5]
print("3 in nums:", 3 in nums)
print("10 not in nums:", 10 not in nums)

print("\nIdentity Operators:")
p = [1, 2, 3]
q = [1, 2, 3]
r = p
print("p is q:", p is q)     # False, different objects
print("p is r:", p is r)     # True, same reference
print("p == q:", p == q)     # True, values are equal
