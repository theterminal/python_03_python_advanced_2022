# 20221010 - Python - Python Advanced - Modules
# 04 - Mathematical Operations


# ----------------- version 1 -------------------


from utils_L19_04.calculations import calculate
from termcolor import colored

data = input('\nEnter a single string in the following format: \n\n'
             + colored('{number1} {sign} {number2}', 'blue', attrs=['bold']) + '\n\n'
             'The sign can be one of the following:\n\n'
             '" / "  divide the first number with the second\n'
             '" * "  multiply the 2 numbers\n'
             '" - "  subtract the first number with the second\n'
             '" + "  add the 2 numbers\n'
             '" ^ "  raise the first number to the second\n\n'
             'and press "Enter": ')

print(calculate(data))
