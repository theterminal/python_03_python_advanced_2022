# 20221010 - Python - Python Advanced - Modules
# 05 - Fibonacci Sequence


# ----------------- version 1 -------------------

from utils_L19_05.line_parser import parse_line
from utils_L19_05.fibonacci import create, locate


nums = []

while True:
    line = input()
    if line == 'Stop':
        break

    command, arg = parse_line(line)

    if command == 'Create':
        nums = create(arg)
        print(*nums)
    elif command == 'Locate':
        idx = locate(arg, nums)
        print(f'The number - {arg} is at index {idx}') if idx != -1 else print(f'The number {arg} is not in the sequence')

