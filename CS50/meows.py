"""
def meow(n: int) -> str:
    Meow n times.
    :param n : Number of times to meow
    :type n : int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    return "meow\n" * n


# number = input("Number: ")
number: int = int(input("Number: "))
meows: str = meow(number)
# meow(number)
print(meows)
------------------------------
import sys
if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")
"""
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
