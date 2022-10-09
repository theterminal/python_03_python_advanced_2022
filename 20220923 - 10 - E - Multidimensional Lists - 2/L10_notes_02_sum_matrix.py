# 20220923 - Python - Python Advanced - Multidimensional Lists


print('\n-------- matrix sum ----------\n')


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum(matrix, []))                  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(sum(matrix, [])))             # 45


print('\n-------- matrix sum ----------\n')


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0

for row in matrix:
    for col in row:
        total += col

print(total)                            # 45
