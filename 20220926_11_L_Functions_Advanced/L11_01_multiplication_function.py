# 20220926 - Python - Python Advanced - Functions Advanced
# 01 - Multiplication Function - judge: https://judge.softuni.org/Contests/Practice/Index/1838#0


# _______________ version 1 _________________ judge 100%


def multiply(*args):
    result = 1
    for element in args:
        result *= element

    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
