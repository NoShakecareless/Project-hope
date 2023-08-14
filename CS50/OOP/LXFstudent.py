class Student(object):
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def print_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
        print("Name: %s, Age: %s" % (self.__name, self.__age))

    def get_score_level(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 80:
            return "B"
        elif self.__score >= 70:
            return "C"
        elif self.__score >= 60:
            return "D"
        else:
            return "Remake"

    def __str__(self):
        return f"{self.__name}  {self.__age}  {self.__score}"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("wrong score")

# __name 仍然可以通过 _Student__name在外部进行访问！
# stu1.__name 和 class内部的__name不是一个变量


if __name__ == "__main__":
    print("class Student has following properties include: name, age, score,plz input these values when you create "
          "objects!")
    stu1 = Student("Bob", 17, 95)
    print(stu1)
    stu1.print_info()
    grade = stu1.get_score_level()
    print(f"{stu1.get_name()}: {grade}")
    stu1.score = 59
    stu1.print_info()
    grade = stu1.get_score_level()
    print(f"{stu1.get_name()}: {grade}")
