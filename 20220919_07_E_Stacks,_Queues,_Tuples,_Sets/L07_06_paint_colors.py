# 20220919 - Python - Python Advanced - Stacks, Queues, Tuples, Sets
# 06 - Paint Colors - judge: https://judge.softuni.org/Contests/Compete/Index/3159#5


# _______________ version 2 _________________ judge 100%


from collections import deque

data_in = deque(input().split())
main_c = ['red', 'yellow', 'blue']
secondary_c = ['orange', 'purple', 'green']
result = deque()

while data_in:
    if len(data_in) > 1:
        first, last = data_in.popleft(), data_in.pop()
        test_1_2 = first + last
        test_2_1 = last + first

        if test_1_2 in main_c or test_1_2 in secondary_c:
            result.append(test_1_2)

        elif test_2_1 in main_c or test_2_1 in secondary_c:
            result.append(test_2_1)

        else:
            stripped_first = first[:-1]
            stripped_last = last[:-1]

            if stripped_first:
                data_in.insert(len(data_in) // 2, stripped_first)

            if stripped_last:
                data_in.insert(len(data_in) // 2, stripped_last)
    else:
        substring = data_in.popleft()

        if substring in main_c or substring in secondary_c:
            result.append(substring)

for _ in range(len(result)):
    if result[0] == 'orange':
        if 'red' not in result or 'yellow' not in result:
            result.popleft()
        else:
            result.append(result.popleft())

    elif result[0] == 'purple':
        if 'red' not in result or 'blue' not in result:
            result.popleft()
        else:
            result.append(result.popleft())

    elif result[0] == 'green':
        if 'yellow' not in result or 'blue' not in result:
            result.popleft()
        else:
            result.append(result.popleft())

    else:
        result.append(result.popleft())

print(list(result))


# _______________ version 1 _________________ judge 100%


from collections import deque

string_in = deque(input().split())
main_colors = ['red', 'yellow', 'blue']
secondary = ['orange', 'purple', 'green']
result = deque()

while string_in:
    while "" in string_in:
        string_in.remove("")

    if len(string_in) > 1:
        test_1 = string_in[0] + string_in[-1]
        test_2 = string_in[-1] + string_in[0]

        if test_1 in (secondary + main_colors) or test_2 in (secondary + main_colors):
            if test_1 in secondary:
                result.append(test_1)
            elif test_2 in secondary:
                result.append(test_2)
            elif test_1 in main_colors:
                result.append(test_1)
            elif test_2 in main_colors:
                result.append(test_2)
            string_in.popleft()
            string_in.pop()

        else:
            index = len(string_in) // 2

            string_in.insert(index, string_in[0][0: -1])
            string_in.insert(index, string_in[-1][0: -1])

            string_in.popleft()
            string_in.pop()
    else:
        test = string_in[0]
        if test in secondary:
            result.append(test)
            string_in.popleft()
        if test in main_colors:
            result.append(test)
            string_in.popleft()
        else:
            string_in.popleft()

loop = len(result)
for i in range(loop):
    if result[0] == 'orange':
        if 'red' not in result or 'yellow' not in result:
            result.popleft()
        else:
            result.append(result.popleft())

    elif result[0] == 'purple':
        if 'red' not in result or 'blue' not in result:
            result.popleft()
        else:
            result.append(result.popleft())

    elif result[0] == 'green':
        if 'yellow' not in result or 'blue' not in result:
            result.popleft()
        else:
            result.append(result.popleft())
    else:
        result.append(result.popleft())

print(list(result))
