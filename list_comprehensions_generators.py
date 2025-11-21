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
