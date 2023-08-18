# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print(f"Your name is {name}, and your are also {age} years old.")

if name == "John" and name == "Rick":
    print(f"Your name is {name}")

# The "in" operator The "in" operator could be used to check if a specified object exists within an iterable object
# container, such as a list:
if name in ["John", "Rick"]:
    print(f"Your name is {name}")

statement = False
another_statement = True
if statement is True:
    # fo something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do another thing
    pass

# The "is" operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False
"""Unlike the double equals operator "==", the "is" operator does not match the values of the variables, 
but the instances themselves"""

# The "not" operator
print(not False)  # Prints out True
print((not False) == False)  # Prints out False

# Exercise
# TODO: change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
