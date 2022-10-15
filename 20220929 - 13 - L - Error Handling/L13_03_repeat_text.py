# 20220929 - Python - Python Advanced - Error Handling
# 03 - Repeat Text - judge url: No judge for this problem


# _______________ version 1 _________________ judge 100%


text = input()

while True:
    try:
        num_times_to_repeat_text = int(input())
        break
    except ValueError:
        print("Variable times must be an integer")


print(f'{text}\n' * num_times_to_repeat_text)
