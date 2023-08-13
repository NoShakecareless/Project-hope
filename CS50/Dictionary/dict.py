# dictionary 字典 相对于列表（一维） 是多维的  key在第一行，值在第二行，如例：名字是key，院校是值value


students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
# 只会打印出名字的key
for student in students:
    print(student)

for student in students:
    print(student, students[student], sep=", ")

"""
输出：
Hermione, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin
"""

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Other"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
