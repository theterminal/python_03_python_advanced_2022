from math import pow


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return pow(n1, n2)          # could use 'n1 ** n2'


def calculate(data):
    num_1, operator, num_2 = data.split()

    if operator == '+':
        return f'{add(float(num_1), float(num_2)):.2f}'
    elif operator == '-':
        return f'{subtract(float(num_1), float(num_2)):.2f}'
    elif operator == '*':
        return f'{multiply(float(num_1), float(num_2)):.2f}'
    elif operator == '/':
        return f'{divide(float(num_1), float(num_2)):.2f}'
    elif operator == '^':
        return f'{power(float(num_1), float(num_2)):.2f}'
    raise ValueError('Not supported operator')
