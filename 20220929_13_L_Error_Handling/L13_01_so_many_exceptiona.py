# 20220929 - Python - Python Advanced - Error Handling
# 01 - So Many Exceptions - judge: No judge for this problem


# _______________ version 1 _________________


for i in range(4):
    numbers_list = [int(x) for x in input().split(", ")]
    result = 1

    for number in numbers_list:

        if number <= 5:
            result *= number

        elif number <= 10:
            result /= number

    if result >= 1:
        print(f'{result:.0f}')
    else:
        print(result)
