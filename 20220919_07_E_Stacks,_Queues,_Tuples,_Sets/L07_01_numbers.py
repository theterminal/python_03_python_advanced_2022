# 20220919 - Python - Python Advanced - Stacks, Queues, Tuples, Sets
# 01 - Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/3159#0


# _______________ version 3 _________________ judge 100%


set_1 = {*input().split()}
set_2 = {*input().split()}
N = int(input())

for _ in range(N):
    command = input()

    if 'Check Subset' in command:
        print('True' if set_1.issubset(set_2) or set_2.issubset(set_1) else 'False')
    else:
        numbers = command.split()[2:]

        if 'Add First' in command:
            set_1 = set_1.union(numbers)

        elif 'Add Second' in command:
            set_2 = set_2.union(numbers)

        elif 'Remove First' in command:
            for number in numbers:
                set_1.discard(number)

        elif 'Remove Second' in command:
            for number in numbers:
                set_2.discard(number)

print(', '.join(map(str, sorted(map(int, set_1)))))
print(', '.join(map(str, sorted(map(int, set_2)))))


# _______________ version 2 _________________ judge 100%


set_1 = {*input().split()}
set_2 = {*input().split()}
N = int(input())

for _ in range(N):
    command = input()

    if 'Add First' in command:
        numbers = command.split()[2:]
        set_1 = set_1.union(numbers)

    elif 'Add Second' in command:
        numbers = command.split()[2:]
        set_2 = set_2.union(numbers)

    elif 'Remove First' in command:
        numbers = command.split()[2:]
        for number in numbers:
            if number in set_1:
                set_1.remove(number)

    elif 'Remove Second' in command:
        numbers = command.split()[2:]
        for number in numbers:
            if number in set_2:
                set_2.remove(number)

    elif 'Check Subset' in command:
        print('True' if set_1.issubset(set_2) or set_2.issubset(set_1) else 'False')

print(', '.join(map(str, sorted(map(int, set_1)))))
print(', '.join(map(str, sorted(map(int, set_2)))))


# _______________ version 1 _________________ judge 100%


set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
N = int(input())

flag_1 = flag_2 = False
if set_1.issubset(set_2) or set_2.issubset(set_1):
    flag_1 = True

for i in range(N):
    command_in = input().split()
    command = command_in[0] + command_in[1]

    if command == 'AddFirst':
        for j in range(2, len(command_in)):
            num = int(command_in[j])
            set_1.add(num)

    elif command == 'AddSecond':
        for j in range(2, len(command_in)):
            num = int(command_in[j])
            set_2.add(num)

    elif command == 'RemoveFirst':
        for j in range(2, len(command_in)):
            num = int(command_in[j])
            if num in set_1:
                set_1.discard(num)

    elif command == 'RemoveSecond':
        for j in range(2, len(command_in)):
            num = int(command_in[j])
            if num in set_2:
                set_2.discard(num)

    elif command == 'CheckSubset':
        flag_2 = True

if flag_1 and flag_2:
    print('True')
elif flag_2:
    print('False')

if set_1:
    list_1 = sorted(list(set_1))
    print(*list_1, sep=', ')
if set_2:
    list_2 = sorted(list(set_2))
    print(*list_2, sep=', ')
