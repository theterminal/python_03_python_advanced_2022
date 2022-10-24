# 20221010 - Python - Python Advanced - Modules
# 01 - Calculate Logarithm


# ----------------- version 1 -------------------


from math import log, e


number = int(input())
base_entered = input()

base = e if base_entered == 'natural' else int(base_entered)

print(f'{log(number, base):.2f}')


# ----------------- version 2 -------------------


from math import log


number = int(input())
base = input()

if base == "natural":
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, int(base)):.2f}")
