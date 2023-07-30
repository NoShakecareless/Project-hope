def main():
    x = int(input("What's X ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


if __name__ == '__main__':
    main()
