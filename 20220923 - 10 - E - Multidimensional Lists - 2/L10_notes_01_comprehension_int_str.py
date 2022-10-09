# 20220923 - Python - Python Advanced - Multidimensional Lists

# The following list comprehension converts only the numbers from a string to 'int', the rest stays as str.


result = [int(x) if x.isdigit() else x for x in input().split()]

print(result)


'''
____________ Test Data ______________


Input 1:
-------
1 2 3 4 Tonny 45 Rick 23 test 5 4 3 4 5


Output 1:
--------
[1, 2, 3, 4, 'Tonny', 45, 'Rick', 23, 'test', 5, 4, 3, 4, 5]
'''
