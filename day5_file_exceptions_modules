# ==============================
# Day 5 Python Practice
# Topics: File Handling, Exceptions, Modules
# ==============================

import math
import random
import datetime
import os


# ------------------------------
# 1. FILE HANDLING
# ------------------------------

def file_handling_demo():
    print("\n--- File Handling Demo ---")

    # Write to a file
    with open("day5_demo.txt", "w") as f:
        f.write("Hello, this is Day 5!\n")
        f.write("Learning file handling in Python.\n")

    # Read from file
    with open("day5_demo.txt", "r") as f:
        content = f.read()
        print("\nFile content:\n", content)

    # Append to file
    with open("day5_demo.txt", "a") as f:
        f.write("Appending this new line.\n")

    print("File operations completed.\n")


# ------------------------------
# 2. EXCEPTION HANDLING
# ------------------------------

def exception_handling_demo():
    print("\n--- Exception Handling Demo ---")

    try:
        num = int(input("Enter a number: "))
        print("10 divided by", num, "=", 10 / num)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter a valid number!")
    finally:
        print("Execution completed.")


# ------------------------------
# 3. MODULES DEMO
# ------------------------------

def modules_demo():
    print("\n--- Modules Demo ---")

    print("Square root of 16:", math.sqrt(16))
    print("Random dice roll:", random.randint(1, 6))
    print("Today's date:", datetime.datetime.now().strftime("%d-%m-%Y"))
    print("Current working directory:", os.getcwd())


# ------------------------------
# 4. MINI PROJECT: Student Record System
# ------------------------------

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    marks = input("Enter student marks: ")

    with open("students.txt", "a") as f:
        f.write(f"{name},{age},{marks}\n")
    print("Student record added!\n")


def view_students():
    print("\n--- Student Records ---")
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No records found.")
            for line in lines:
                name, age, marks = line.strip().split(",")
                print(f"Name: {name}, Age: {age}, Marks: {marks}")
    except FileNotFoundError:
        print("No student file found yet.\n")


def search_student():
    search_name = input("Enter name to search: ")
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, age, marks = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"Found -> Name: {name}, Age: {age}, Marks: {marks}")
                    found = True
                    break
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No student file found yet.\n")


def student_system():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting Student Record System.")
            break
        else:
            print("Invalid choice, try again.")


# ------------------------------
# MAIN DRIVER
# ------------------------------
if __name__ == "__main__":
    print("===== Day 5 Python Practice =====")

    file_handling_demo()
    exception_handling_demo()
    modules_demo()

    print("\n--- Now try the Mini Project ---")
    student_system()
