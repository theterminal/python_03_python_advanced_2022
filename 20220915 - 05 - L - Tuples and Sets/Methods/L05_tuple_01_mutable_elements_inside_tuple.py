# 20220915 - Python - Python Advanced - Tuples and Sets


# Tuples are IMMUTABLE but the elements are! (If a list is an elements of Tuple, the elements in the list are MUTABLE)
# Main use of tuples is to transfer data from one place (section, program...) to another

# -----------------------------------------

t = (1, 2, 3)                   # 't' is a tuple - it is immutable
print(t)

t_1 = (1, [100, 200], 3)        # 't_1' is a tuple and includes a list as element on index 1
print(t_1)

t_1[1][0] = 1000                # the list inside the tuple is mutable!
print(t_1)


# _________________________________________
# Tuple can be defined without parentheses!

t_3 = 10, 20, 30                # this is a valid tuple
print(t_3)


# _____________________________
# Tuple from 1 with one element

t_4 = (45, )
print(t_4)

t_5 = 55,
print(t_5)
