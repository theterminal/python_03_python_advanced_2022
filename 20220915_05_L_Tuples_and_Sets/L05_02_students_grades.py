# 20220915 - Python - Python Advanced - Tuples and Sets
# 02 - Students Grades - judge url: https://judge.softuni.org/Contests/Practice/Index/1832#1


# _______________ version 1 _________________ judge 100%


num_students = int(input())
students = {}

for i in range(num_students):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)

    grades = ' '.join(str(f'{grade:.2f}') for grade in grades)
    print(f'{student} -> {grades} (avg: {average_grade:.2f})')


# _______________ version 2 _________________ judge 100%


num_students = int(input())
students = {}

for i in range(num_students):
    data = tuple(input().split())
    student, grade = data
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)

    grades = ' '.join(str(f'{grade:.2f}') for grade in grades)
    print(f'{student} -> {grades} (avg: {average_grade:.2f})')
