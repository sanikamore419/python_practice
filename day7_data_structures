# Day 7 Practice: Python Data Structures in One Program

def main():
    # ---- LIST ----
    print("\n🔹 LIST Example")
    nums = [1, 2, 3, 4, 5]
    nums.append(6)
    nums.remove(3)
    print("List after operations:", nums)

    squares = [x**2 for x in range(6)]
    print("Squares using list comprehension:", squares)

    # ---- TUPLE ----
    print("\n🔹 TUPLE Example")
    point = (3, 4)
    x, y = point
    print(f"Point unpacked: x={x}, y={y}")

    colors = ("red", "blue", "green")
    print("Second color:", colors[1])

    # ---- SET ----
    print("\n🔹 SET Example")
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    print("Union:", A | B)
    print("Intersection:", A & B)
    print("Difference (A-B):", A - B)

    # ---- DICTIONARY ----
    print("\n🔹 DICTIONARY Example")
    student = {"name": "Sanika", "age": 20, "marks": 95}
    student["age"] = 21
    student["city"] = "Pune"
    for key, value in student.items():
        print(f"{key}: {value}")

    # ---- CHALLENGE: Word Frequency Counter ----
    print("\n🔹 WORD FREQUENCY Example")
    text = "the cat sat on the mat with the cat"
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print("Word frequencies:", freq)


# Run the program
if __name__ == "__main__":
    main()
