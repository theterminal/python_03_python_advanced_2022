# 20220927 - Python - Python Advanced - Functions Advanced
# 06 - Function Executor - judge url: https://judge.softuni.org/Contests/Compete/Index/1839#5


# _______________ version 1 _________________ judge 100%


def func_executor(*args):
    result = ''

    for function in args:
        # result += function[0].__name__ + ' - ' + str(function[0](*function[1])) + '\n'
        result += f'{function[0].__name__} - {function[0](*function[1])}\n'

    return result


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
