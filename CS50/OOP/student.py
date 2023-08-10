import sys


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            # sys.exit("Missing name")
            #   return None
            raise ValueError("Missing name")
        self._name = name
    # Getter

    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


'''
raise: raise ValueError
'''


def main():
    student = get_student_class()
    #    if student["name"] == "Padma":
    #        student["house"] = "Ravenclaw"
    #    print(f"{student['name']} from {student['house']}")
    # print(f"{student.name} from {student.house}")
    student._house = "Number four, Privet Drive "    # setter & getter let you set value manually not pass
    print(student)  # 打印出计算机内存地址，对象存储地址 def __str__(self)


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


def get_student_class():
    #   student = Student()
    #   student.name = input("Name: ")
    #   student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


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
