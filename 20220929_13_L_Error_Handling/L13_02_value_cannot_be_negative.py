# 20220929 - Python - Python Advanced - Error Handling
# 02 - Value Cannot Be Negative - judge: No judge for this problem


# _______________ version 1 _________________


class ValueCannotBeNegative(Exception):
    """Value cannot be below zero!"""


for i in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative
