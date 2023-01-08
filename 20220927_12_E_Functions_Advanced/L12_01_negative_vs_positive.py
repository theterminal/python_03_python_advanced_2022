# 20220927 - Python - Python Advanced - Functions Advanced
# 01 - Negative vs Positive - judge: https://judge.softuni.org/Contests/Compete/Index/1839#0


# _______________ version 1 _________________ judge 100%


def sum_numbers(command: str, numbers_list: list):
    if command == 'negative':
        result_list = [i for i in numbers_list if i < 0]
    else:
        result_list = [i for i in numbers_list if i > 0]

    return sum(result_list)


nums = [int(i) for i in input().split()]
sum_negative = sum_numbers('negative', nums)
sum_positive = sum_numbers('positive', nums)

print(sum_negative)
print(sum_positive)

if abs(sum_negative) > sum_positive:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
