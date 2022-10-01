# 20220915 - Python - Python Advanced - Tuples and Sets
# 06 - Summation Pairs - judge url: NOT in judge system


numbers = list(map(int, input().split()))
target = int(input())

while numbers:
    n1 = numbers.pop()
    for i in range(len(numbers)):
        if n1 + numbers[i] == target:
            print(f'{n1} + {numbers[i]} = {target}')
            numbers.remove(numbers[i])
            break
