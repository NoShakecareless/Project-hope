"""
names = []

for i in range(3):
    names.append(input("What's your name ?"))

for name in sorted(names):
    print(f"hello, {name}")


name = input("What's your name ?")

with open("name.txt", "a") as file:
    file.write(f"{name}\n")

file.close()
"""

"""""
with open("name.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""

names = []

with open("name.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
