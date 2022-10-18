# 20221003 - Python - Python Advanced - File Handling
# 02 - File reader

# _______________ version 3 _________________


print(sum([int(line.strip()) for line in open('L15_02_file_reader/numbers.txt', 'r')]))


# _______________ version 2 _________________


file_path = 'L15_02_file_reader/numbers.txt'
file = open(file_path, 'r')

print(sum([int(line.strip()) for line in file]))


# _______________ version 1 _________________


file_path = 'L15_02_file_reader/numbers.txt'
file = open(file_path, 'r')

total = 0
for line in file:
    total += int(line.strip())

print(total)
