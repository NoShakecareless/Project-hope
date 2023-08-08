students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        student = {"name": name, "house": house}
        students.append(student)
#        row = line.rstrip().split(",")
#        print(f"{row[0]} is in {row[1]}")


def get_name(stu):
    return stu["name"]
#    return stu["house"]


# 此时不能给这么写sorted(students)，因为students是字典不是单纯的句子, 除非添加sorted参数key
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is from {student['house']}")
