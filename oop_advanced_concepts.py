# oop_advanced_concepts.py
# -----------------------------------------------
# Advanced OOP Concepts in Python
# Polymorphism, Abstraction, Encapsulation,
# Inheritance, Method Overriding, MRO, and ABC.
# -----------------------------------------------

from abc import ABC, abstractmethod

# -----------------------------
# 1. ENCAPSULATION
# -----------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance        # protected variable
        self.__pin = "1234"            # private variable

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount


# -----------------------------
# 2. ABSTRACTION (Using ABC)
# -----------------------------
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started"


# -----------------------------
# 3. POLYMORPHISM
# -----------------------------
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

# Function using polymorphism
def animal_sound(animal):
    return animal.speak()


# -----------------------------
# 4. METHOD OVERRIDING
# -----------------------------
class Parent:
    def show(self):
        return "Parent class method"

class Child(Parent):
    def show(self):
        return "Child class method (overridden)"
