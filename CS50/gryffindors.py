"""
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
gryffindors1 = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

"""
students = ["Hermione", "Harry", "Ron"]


# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
gryffindors = {student: "Gryffindor" for student in students}    # from right to left

print(gryffindors)

for i, student in enumerate(students):
    print(i + 1, student)
    