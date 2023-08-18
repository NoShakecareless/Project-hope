my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list[0])   # print 1
print(my_list[1])   # print 2
print(my_list[2])   # print 3

# print out 1, 2, 3
for x in my_list:
    print(x)
# Exercise
"""
In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets 
operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will 
be 1."""
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")


# This code should write out the filled arrays and the seccond name in the names list(Eric).
print(numbers)
print(strings)
print(f"The second name on the name list is {second_name}")
