# 20220912 - Python - Python Advanced - Lists as Stacks and Queues

from collections import deque


# _____ append() _____ popleft() _____ print(q[0]) _____ print(len(q)) _____


q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q)
print(q.popleft())
print(q.popleft())
print(q)

q.append(1)
q.append(2)
q.append(3)

print(q)

print(q[0])
print(len(q))
