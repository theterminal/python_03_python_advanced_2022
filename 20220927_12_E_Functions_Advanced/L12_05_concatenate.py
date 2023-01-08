# 20220927 - Python - Python Advanced - Functions Advanced
# 05 - Concatenate - judge: https://judge.softuni.org/Contests/Compete/Index/1839#4


# _______________ version 1 _________________ judge 100%


def concatenate(*args, **kwargs):
    string = ''.join(args)

    for k, v in kwargs.items():
        if k in string:                                   # could do it without this line
            string = string.replace(k, v)

    return string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
