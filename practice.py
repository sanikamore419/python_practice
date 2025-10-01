def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet("Sanika"))
print(greet("Sanika", msg="Hi"))

# *args example
def add_numbers(*args):
    return sum(args)

print(add_numbers(1,2,3,4))

# **kwargs example
def show_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")

show_info(name="Sanika", age=21)

# Lambda example
square = lambda x: x**2
print(square(5))
