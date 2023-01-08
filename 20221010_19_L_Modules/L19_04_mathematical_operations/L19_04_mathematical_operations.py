# 20221010 - Python - Python Advanced - Modules
# 03 - Triangle


# ----------------- version 1 -------------------


from utils.math_operations import calculate


first, operator, second = input().split()

print(calculate(float(first), float(second), operator))
