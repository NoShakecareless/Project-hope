# Ask user for their name
# name = input("What's your name? ").strip().title()

# Say hello to user
# print(f"hello, {name}")

x = int(input("What's X? "))

y = int(input("What's Y? "))

if x > y:
    print("x is larger than y")

if x < y:
    print("x is smaller than y")

if x == y:
    print("x is equal to y")

print(x + y)


# name = input("What's your name? ").strip().title()
# hello(name)


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello ", to)
