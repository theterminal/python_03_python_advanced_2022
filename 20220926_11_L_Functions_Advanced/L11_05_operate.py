# 20220926 - Python - Python Advanced - Functions Advanced
# 05 - Operate - judge: https://judge.softuni.org/Contests/Practice/Index/1838#4


# _______________ version 2 _________________ judge 100%


from functools import reduce


def operate(operator, *numbers):
    result = 0

    if operator == '+':
        result = reduce(lambda x, y: x + y, numbers)
    elif operator == '-':
        result = reduce(lambda x, y: x - y, numbers)
    elif operator == '*':
        result = reduce(lambda x, y: x * y, numbers)
    elif operator == '/':
        if 0 not in numbers or numbers[0] == 0:
            result = reduce(lambda x, y: x / y, numbers)
        else:
            result = f'There is a 0 in the list and division on 0 is not possible!'

    return result


print(operate("/", 1, 0, 5))


# _______________ version 1 _________________ judge 100%


def operate(operator, *args):
    def add():
        result = 0
        for element in args:
            result += element
        return result

    def subtract():
        result = 0
        for el_i in range(len(args)):
            if el_i == 0:
                result = args[0]
            else:
                result -= args[el_i]
        return result

    def multiply():
        result = 1
        for element in args:
            result *= element
        return result

    def divide():
        result = 0
        for el_i in range(len(args)):
            if el_i == 0:
                result = float(args[0])
            else:
                if args[el_i] != 0:
                    result /= float(args[el_i])
                else:
                    result = f'There is a 0 in the list and division on 0 is not possible!'
                    break
        return result

    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(operate("/", 10, 2, 5))
