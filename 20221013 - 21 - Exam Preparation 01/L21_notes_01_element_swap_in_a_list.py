# 20221013
# Element Swap in a List


print('\n------ ex. 1 --------\n')


eggs = [1, 2, 3, 4, 5]
print(eggs)

eggs[1], eggs[-1] = eggs[-1], eggs[1]
print(eggs)


print('\n------- ex. 2 -------\n')


eggs = [1, 2, 3, 4, 5]
print(eggs)

eggs[0], eggs[1] = eggs[2], eggs[4]
print(eggs)


print('\n------- ex. 3 -------\n')


eggs = [1, 2, 3, 4, 5, 6]
print(eggs)

eggs[0], eggs[-1], eggs[1], eggs[-2] = eggs[-1], eggs[0], eggs[-2], eggs[1]
print(eggs)


print('\n------ ex. 4 --------\n')


eggs = [1, 2, 3, 4, 5, 6]
print(eggs)

eggs[0], eggs[1] = eggs[-1], eggs[-2]
print(eggs)
