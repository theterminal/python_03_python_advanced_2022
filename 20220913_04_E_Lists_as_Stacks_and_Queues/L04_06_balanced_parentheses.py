# 20220913 - Python - Python Advanced - Lists as Stacks and Queues
# 06 - Balanced Parentheses - judge url: https://judge.softuni.org/Contests/Compete/Index/1831#5


# ______________ version 2 _______________ judge 100%


data = input()
stack = []
loop = len(data)
flag = 0

for i in range(loop):
    if data[i] in ['{', '[', '(']:
        stack.append(data[i])
    elif data[i] == '}' and stack and stack[-1] == '{':
        stack.pop()
    elif data[i] == ']' and stack and stack[-1] == '[':
        stack.pop()
    elif data[i] == ')' and stack and stack[-1] == '(':
        stack.pop()
    else:
        flag = 1
        break

print('YES') if not flag else print('NO')


# ______________ version 1 _______________ judge 100%


data = input()
stack = []
loop = len(data)
flag = 0

for i in range(loop):
    if loop % 2 == 1:
        flag = 1
        break
    if data[i] == '{':
        stack.append(data[i])
    elif data[i] == '[':
        stack.append(data[i])
    elif data[i] == '(':
        stack.append(data[i])
    elif data[i] == '}':
        if len(stack) > 0:
            if stack[-1] == '{':
                stack.pop()
            else:
                flag = 1
                break
        else:
            flag = 1
            break
    elif data[i] == ']':
        if len(stack) >= 0:
            if stack[-1] == '[':
                stack.pop()
            else:
                flag = 1
                break
        else:
            flag = 1
            break
    elif data[i] == ')':
        if len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                flag = 1
                break
        else:
            flag = 1
            break
    else:
        flag = 1
        break

if not flag:
    print('YES')
else:
    print('NO')
