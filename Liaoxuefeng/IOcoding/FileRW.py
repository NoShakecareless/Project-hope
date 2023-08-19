# 文件读写一旦出现IOError, 一旦出错后面的f.close()就不会调用, 故为了保证正确关闭文件, 采用 try...finally...来实现
try:
    f = open("test.txt", 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 简洁写法
with open("test.txt", "r") as f:
    print(f.read())
    #   实现效果和上面try...finally...一样, 并且不需要调用f.close()

    """
    read会一次性读取文件全部内容, 可以反复调用read(size)方法, 每次最多读取size个字节的内容
    另外可以调用readline()每次读取一行内容, 调用readlines()一次读取所有内容并按行返回list
    配置文件调用readlines()最方便
    """
for line in f.readlines():
    print(line.strip())    # 把末尾的'\n'删掉

# file-like Object
# f = open("test.jpg", "rb")

# 字符编码
# f = open("gbk.txt", "r", encoding="gbk", errors="ignore)
# errors参数，文本文件中夹杂了非法编码字符



