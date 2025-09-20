# Day 13 - Python Practice: NumPy Basics
import numpy as np

print("===== Day 13 Practice =====")

# 1. Creating Arrays
print("\n--- Creating Arrays ---")
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
arange_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("Array:", arr)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Arange:", arange_arr)
print("Linspace:", linspace_arr)

# 2. Array Properties
print("\n--- Array Properties ---")
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# 3. Indexing and Slicing
print("\n--- Indexing & Slicing ---")
print("First element:", arr[0])
print("Slice 2 to 4:", arr[1:4])

# 4. Vectorized Operations
print("\n--- Vectorized Operations ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Dot Product:", np.dot(a, b))

# 5. Matrix Operations
print("\n--- Matrix Operations ---")
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)
print("Transpose:\n", matrix.T)

# 6. Useful Functions
print("\n--- NumPy Functions ---")
data = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Sum:", np.sum(data))

# 7. Reshaping
print("\n--- Reshaping ---")
reshaped = np.arange(1, 10).reshape(3, 3)
print("Reshaped 3x3:\n", reshaped)

# 8. Practice Problem: Student Marks
print("\n--- Student Marks Analysis ---")
marks = np.array([88, 76, 92, 85, 69, 95])
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# 9. Practice Problem: Random Data
print("\n--- Random Data ---")
random_data = np.random.randint(1, 101, size=(5, 5))
print("Random 5x5 Array:\n", random_data)
print("Row sums:", np.sum(random_data, axis=1))
print("Column sums:", np.sum(random_data, axis=0))
