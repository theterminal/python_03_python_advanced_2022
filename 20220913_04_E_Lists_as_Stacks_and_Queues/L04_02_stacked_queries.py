# 20220913 - Python - Python Advanced - Lists as Stacks and Queues
# 02 - Stacked Queries - judge url: https://judge.softuni.org/Contests/Compete/Index/1831#1


# _______________ version 1 ________________ judge 100%


stack = []
n = int(input())

for _ in range(n):
    entry = input().split()
    token_0 = int(entry[0])

    if token_0 == 1:
        token_1 = int(entry[1])
        stack.append(token_1)
    elif token_0 == 2:
        if len(stack) > 0:
            stack.pop()
    elif token_0 == 3:
        if len(stack) > 0:
            print(max(stack))
    elif token_0 == 4:
        if len(stack) > 0:
            print(min(stack))

result = []
for _ in range(len(stack)):
    result.append(str(stack.pop()))

print(', '.join(result))
