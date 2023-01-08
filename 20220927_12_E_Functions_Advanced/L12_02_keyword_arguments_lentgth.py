# 20220927 - Python - Python Advanced - Functions Advanced
# 02 - Keyword Arguments Lent=gth - judge: https://judge.softuni.org/Contests/Compete/Index/1839#1


# _______________ version 1 _________________ judge 100%


def kwargs_length(**dict):
    return len(dict.keys())


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
