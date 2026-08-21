students = []
with open("students.csv") as file:
    for line in file:
        name, grade = line.rstrip().split(",")
        student = {"name" : name, "grade": grade}
        students.append(student)


for student in sorted(students,key=lambda student: student["name"], reverse = False):
    print(f"{student['name']} is in Grade {student['grade']}")



