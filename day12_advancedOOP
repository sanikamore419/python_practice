# Day 12 - Python Practice: Advanced OOP

print("===== Day 12 Practice =====")

# 1. Class vs Instance Variables
print("\n--- Class vs Instance Variables ---")
class Car:
    wheels = 4  # class variable (shared)

    def __init__(self, brand, model):
        self.brand = brand   # instance variable
        self.model = model

c1 = Car("Toyota", "Corolla")
c2 = Car("Tesla", "Model 3")
print(c1.brand, c1.wheels)
print(c2.brand, c2.wheels)

# 2. Class methods and Static methods
print("\n--- Class & Static Methods ---")
class Student:
    school_name = "Sanjivani College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def is_pass(marks):
        return marks >= 40

s1 = Student("Sanika", 85)
print(s1.school_name)
Student.change_school("Engineering College")
print(s1.school_name)
print("Pass?", Student.is_pass(39))

# 3. Inheritance and Method Overriding
print("\n--- Inheritance ---")
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

pets = [Dog(), Cat(), Animal()]
for pet in pets:
    print(pet.speak())

# 4. Encapsulation
print("\n--- Encapsulation ---")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Sanika", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())

# 5. Polymorphism Example
print("\n--- Polymorphism ---")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print("Area:", shape.area())

# 6. Practice Problem - Student Grades
print("\n--- Student Grades ---")
class GradeBook:
    def __init__(self):
        self.records = {}

    def add_student(self, name, grade):
        self.records[name] = grade

    def get_topper(self):
        return max(self.records, key=self.records.get)

gb = GradeBook()
gb.add_student("Sanika", 92)
gb.add_student("Riya", 85)
gb.add_student("Aarav", 78)
print("Topper:", gb.get_topper())
