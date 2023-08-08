def main():
    student = get_student_dict1()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


"""
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
# [name, house]表示返回一个列表，列表是可以改变的，元组不行！
"""


def get_student_dict1():
    # student = {"name": input("Name: "), "house": input("House: ")}
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


def get_student_dict2():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()


"""
tuple, 元组,有序且不可更改的集合
字典的强大之处在于语义关联
"""