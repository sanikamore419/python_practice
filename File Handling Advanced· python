"""
File: file_handling_advanced.py
Topic: Advanced File Handling in Python (CSV, JSON, Context Managers)
Author: Sanika
"""

import csv
import json
from contextlib import contextmanager

# ---------------------------
# 1. Reading and Writing CSV
# ---------------------------

def write_csv(filename, data):
    """Write a list of dictionaries to a CSV file."""
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv(filename):
    """Read and return CSV data as a list of dictionaries."""
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


# ---------------------------
# 2. Reading and Writing JSON
# ---------------------------

def write_json(filename, data):
    """Write Python objects to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def read_json(filename):
    """Read JSON file and return Python object."""
    with open(filename, 'r') as f:
        return json.load(f)


# ---------------------------
# 3. Custom Context Manager
# ---------------------------

@contextmanager
def open_file(filename, mode):
    """Custom context manager for file opening and safe closing."""
    f = None
    try:
        f = open(filename, mode)
        yield f
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if f:
            f.close()


# Example usage of custom context manager
def log_message(filename, message):
    with open_file(filename, 'a') as f:
        f.write(message + '\n')


# ---------------------------
# 4. Main Execution Example
# ---------------------------
if __name__ == "__main__":
    # CSV Example
    employees = [
        {"name": "Sanika", "role": "Developer", "salary": 70000},
        {"name": "Aarav", "role": "Analyst", "salary": 50000}
    ]
    write_csv("employees.csv", employees)
    print("CSV Read:", read_csv("employees.csv"))

    # JSON Example
    write_json("employee_data.json", employees)
    print("JSON Read:", read_json("employee_data.json"))

    # Logging using custom context manager
    log_message("logs.txt", "Program executed successfully.")
    print("Log written.")
