# Day 14 - Python Practice: Regular Expressions
import re

print("===== Day 14: Regular Expressions =====")

# 1. Basic search
text = "My phone number is 9876543210 and my office number is 1234567890."
pattern = r"\d{10}"   # match exactly 10 digits
matches = re.findall(pattern, text)
print("Phone numbers found:", matches)

# 2. Match email addresses
emails = "Contact us at support@example.com or sales@myshop.org"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"
print("Emails found:", re.findall(email_pattern, emails))

# 3. Using search
sentence = "I love Python programming."
if re.search(r"Python", sentence):
    print("Found the word 'Python'")

# 4. Using match (checks only at beginning)
print("Match result:", re.match(r"I love", sentence))

# 5. Replace words with sub()
text2 = "Python is great. Python is fun."
print("After replacement:", re.sub(r"Python", "Java", text2))

# 6. Character classes
sample = "Order IDs: A123, B456, C789"
print("All IDs:", re.findall(r"[A-Z]\d{3}", sample))

# 7. Anchors
line = "start middle end"
print("Starts with 'start'?", bool(re.match(r"^start", line)))
print("Ends with 'end'?", bool(re.search(r"end$", line)))

# 8. Groups & Capturing
date = "Today's date is 18-09-2025"
date_pattern = r"(\d{2})-(\d{2})-(\d{4})"
match = re.search(date_pattern, date)
if match:
    print("Day:", match.group(1))
    print("Month:", match.group(2))
    print("Year:", match.group(3))

# 9. Practice Problems
print("\n--- Practice Problems ---")

# Validate password (at least 8 chars, one digit, one uppercase)
def validate_password(pwd):
    return bool(re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", pwd))

print("Password 'Python123' valid?", validate_password("Python123"))
print("Password 'python' valid?", validate_password("python"))

# Extract hashtags from text
tweet = "Learning #Python is fun! #Coding #100DaysOfCode"
hashtags = re.findall(r"#\w+", tweet)
print("Hashtags found:", hashtags)

# Find all words starting with 's'
text3 = "sun sand sea sky start stone strong"
words_s = re.findall(r"\bs\w+", text3)
print("Words starting with 's':", words_s)
