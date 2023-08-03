"""
i = 1
while i <= 3:
    print("meow")
    i += 1
"""

"""
# for loop & list
for i in [0, 1, 2]:
    print("meow")

for i in range(10):
    print("Meow")

# 另类循环打印,python特性
print("MEOW\n" * 3, end="")
"""

"""
while True:
    n = int(input("What's X?"))
    if n > 0:
        break

for i in range(n):
    print("meow")
 
"""


def main():
    number = get_number()
    print_meow(number)


def get_number():
    while True:
        n = int(input("What's X ?"))
        if n > 0:
            return n
        else:
            print("x must be greater than 0")


def print_meow(n):
    for x in range(n):
        print("meow")


if __name__ == '__main__':
    main()
