# 20220913 - Python - Python Advanced - Lists as Stacks and Queues
# 01 - Reverse Strings - judge url: https://judge.softuni.org/Contests/Compete/Index/1831#0


# ___________ version 1 ____________ judge 100%


stack = input().split()

result = []
for _ in range(len(stack)):
    result.append(stack.pop())
print(' '.join(result))


# ___________ version 2 ____________ judge 100%


stack = input().split()

for _ in range(len(stack)):
    print(stack.pop(), end=' ')
