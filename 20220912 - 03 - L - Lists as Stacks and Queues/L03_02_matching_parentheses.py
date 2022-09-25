# 20220912 - Python - Python Advanced - Lists as Stacks and Queues
# Matching Parentheses - judge url: https://judge.softuni.org/Contests/Practice/Index/1830#1


# _____________________ version 1 ____________________ judge 100%


text = input()

parentheses_start_index = []

for i in range(len(text)):
    if text[i] == '(':
        parentheses_start_index.append(i)
    elif text[i] == ')':
        print(text[parentheses_start_index.pop(): i + 1])
