def main():
    hello("")
    goodbye("world")


def hello(name):
    assert name != ""
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


print(__name__)


if __name__ == "__name__":
    main()
