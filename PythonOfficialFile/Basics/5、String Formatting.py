# String Formatting

# This prints out "Hello, John!"
name = "John"
print("Hello, %s" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
my_list = [1, 2, 3]
print("A list: %s" % my_list)


# Exercise

data = ("John", "Doe", 53.44)
format_string = "Hello"
f_string = "Hello %s %s. Your current balance is $%s."
print(format_string + " %s %s. Your current balance is $%s" % data)
print(f_string % data)
