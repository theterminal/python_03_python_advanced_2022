# 20220912 - Python - Python Advanced - Lists as Stacks and Queues
# Reverse Strings - judge url: https://judge.softuni.org/Contests/Practice/Index/1830#0


# _____________________ version 3 ____________________ judge 100%


text = list(input())

while len(text) > 0:
    print(text.pop(), end='')


# _____________________ version 2 ____________________ judge 100%


text = list(input())

for i in range(len(text)):
    print(text.pop(), end='')


# _____________________ version 1 ____________________ judge 100%


text = input()

text_to_list = []

for letter in text:
    text_to_list.append(letter)

result = []
for element in range(len(text_to_list)):
    result.append(text_to_list.pop())

print(''.join(result))
