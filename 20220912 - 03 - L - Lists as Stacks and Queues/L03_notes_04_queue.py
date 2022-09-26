# 20220912 - Python - Python Advanced - Lists as Stacks and Queues

from collections import deque

q = deque([1, 2, 3])
print(q)

q.rotate(1)         # it rotates queue 1 position to the right
print(q)
q.rotate(1)
print(q)
q.rotate(1)
print(q)

q.rotate(3)         # it rotates queue 3 position to the right
print(q)

q.rotate(-1)        # it rotates queue 1 position to the left
print(q)
