
# --------------------------------------------------
# 1. Basic if statement
# --------------------------------------------------

age = 18

if age >= 18:
    print("You are eligible to vote.")

# --------------------------------------------------
# 2. if-else statement
# --------------------------------------------------

marks = 45

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

# --------------------------------------------------
# 3. if-elif-else ladder
# --------------------------------------------------

score = 82

if score >= 90:
    print("Grade: A+")
elif score >= 75:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

# --------------------------------------------------
# 4. Nested if statement
# --------------------------------------------------

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")

# --------------------------------------------------
# 5. Using logical operators (and, or, not)
# --------------------------------------------------

age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# --------------------------------------------------
# 6. Checking even or odd number
# --------------------------------------------------

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
