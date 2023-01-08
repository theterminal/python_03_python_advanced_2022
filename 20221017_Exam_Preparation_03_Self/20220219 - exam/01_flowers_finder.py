# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 01 - Flowers Finder - judge: https://judge.softuni.org/Contests/Practice/Index/3374#0


# _______________ version 1 _________________ judge 100%


from collections import deque


vow = deque(input().split())
con = deque(input().split())

words = {
    'rose': 'rose',
    'tulip': 'tulip',
    'lotus': 'lotus',
    'daffodil': 'daffodil'
}

flag = False

while vow and con:
    vow_l = vow.popleft()
    con_r = con.pop()

    for word in words.keys():
        words[word] = words[word].replace(vow_l, '')
        words[word] = words[word].replace(con_r, '')

        if words[word] == '':
            print(f'Word found: {word}')
            flag = True
            break
    if flag:
        break

if not flag:
    print('Cannot find any word!')
if vow:
    print(f'Vowels left: {" ".join(vow)}')
if con:
    print(f'Consonants left: {" ".join(con)}')
