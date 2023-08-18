def generator_function():
    value1 = yield 1
    value1 = yield 0
    print("value1 is ", value1)
    value2 = yield 1
    print("value2 is ", value2)
    value3 = yield 2
    print("value3 is ", value3)


g = generator_function()
print(g.__next__())
print(g.send(1))
g.send(1)
print(g.send(2))
