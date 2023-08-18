# Numbers
my_int = 7
print(my_int)
"""To define a floating point number"""
my_float = 7.0
print(my_float)
my_float = float(7)
print(my_float)

# Strings
my_string = 'hello'
print(my_string)
my_string = "Hello"
print(my_string)
my_string = "Don't worry about apostrophes"
print(my_string)

one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + world
print(helloworld)
# print(one + two + hello) # Mixing operators between numbers and strings is not supported

a, b = 3, 5
print(a, b)

# Exercise
my_string = "hello"
my_float = 10.0
my_int = 20

# testing
if my_string == "hello":
    print(f"String is {my_string}")
if my_float == 10.0:
    print(f"float is {my_float}")
if my_int == 20:
    print("my_int is %d" % my_int)
