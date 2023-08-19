# python解释器可以启动时用 -O（大写字母o）来关闭assert，之后assert可以当作pass来看
# print 也可以用logging来替代用于调试
import logging
logging.basicConfig(level=logging.INFO)
# level 有debug、info、warning、error等几个级别

def foo(s):
    n = int(s)
    assert n != 0, "n is zero!"
    return 10 / 0


def main():
    foo('0')


main()
