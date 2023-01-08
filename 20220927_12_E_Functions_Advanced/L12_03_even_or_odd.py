# 20220927 - Python - Python Advanced - Functions Advanced
# 03 - Even or Odd - judge: https://judge.softuni.org/Contests/Compete/Index/1839#2


# _______________ version 1 _________________ judge 100%


def even_odd(*args):
    args, command = args[:-1],args[-1]

    if command == 'even':
        result = [x for x in args if x % 2 == 0]
    else:
        result = [x for x in args if x % 2 == 1]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

