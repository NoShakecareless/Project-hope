import logging
# 记录错误信息, 程序打印完出错信息后继续执行, 并正常退出
# logging.exception(e)


try:
    print("try...")
    # r = 10 / 0
    r = 10 / 2
    print("result:", r)
except ZeroDivisionError as e:
    print("except:", e)
finally:
    print("finally")
print("End")
"""
try 运行代码，出错会跳转至except错误处理代码，后续代码不执行。执行完except之后如果有finally，则执行finally语句块
finally如果有，不管有没有错误一定会执行
"""

# Multiple Error
try:
    print("try...")
    r = 10 / int('a')
    print("result:", r)
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
else:
    print("No error!")  # 没有错误的时候执行else语句块
finally:
    print("finally...")
print("End")


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print("Finally...")


main()
