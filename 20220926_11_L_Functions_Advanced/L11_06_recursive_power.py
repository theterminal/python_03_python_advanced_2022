# 20220926 - Python - Python Advanced - Functions Advanced
# 06 - Recursive Power - judge: https://judge.softuni.org/Contests/Practice/Index/1838#5


# _______________ version 1 _________________ judge 100%


def recursive_power(number, power):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
