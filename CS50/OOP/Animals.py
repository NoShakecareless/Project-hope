class Animal(object):
    def run(self):
        print("Animal is running.....")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Dog is running.....")

    def eat(self):
        print("Eating meat......")


class Cat(Animal):
    def run(self):
        print("Cat is running.....")


def run_twice(animal):
    print("run twice!")
    animal.run()
    animal.run()

#  Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了


if __name__ == "__main__":
    cat = Cat()
    dog = Dog("bob", 1)
    cat.run()
    dog.run()
    dog.eat()
    run_twice(Cat())

