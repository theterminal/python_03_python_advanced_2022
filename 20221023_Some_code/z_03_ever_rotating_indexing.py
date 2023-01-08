# 20220921 - Python - Python Advanced - Multidimensional Lists
# Ever rotating indexing...


# using '%' for incrementing index depending on the needed length of the string


rows = 100
columns = 153
string = 'There is a war on for your mind!'
index = 0

for row in range(rows):
    result = ''
    for col in range(columns):
        result += string[index % len(string)]
        # print(index % len(string), end='')
        index += 1
    # print()
    print(result)
    # print()
