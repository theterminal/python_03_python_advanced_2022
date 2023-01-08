# 20221017 - Python - Python Advanced - Exam Preparation 3 - Self
# 01 - Ramen Shop - judge: https://judge.softuni.org/Contests/Practice/Index/3430#0


# _______________ version 1 _________________judge 100%


from collections import deque


ramen = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))


while ramen and customers:
    last_ramen = ramen.pop()
    first_customer = customers.popleft()

    if last_ramen == first_customer:
        continue
    elif last_ramen > first_customer:
        ramen.append(last_ramen - first_customer)
    elif first_customer > last_ramen:
        customers.appendleft(first_customer - last_ramen)

if not customers:
    print('Great job! You served all the customers.')
    if ramen:
        print(f'Bowls of ramen left: {", ".join(list(map(str, ramen)))}')
else:
    print('Out of ramen! You didn\'t manage to serve all customers.')
    print(f'Customers left: {", ".join(list(map(str, customers)))}')
