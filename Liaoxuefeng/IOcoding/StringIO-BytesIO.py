# StringIO 内存中读写str
from io import StringIO
from io import BytesIO
# str写入StringIO

f = StringIO()
f.write("hello")
f.write(" ")
f.write("World!")
print(f.getvalue())

# 读取StringIO

f = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())

# BytesIO 二进制数据
f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())
