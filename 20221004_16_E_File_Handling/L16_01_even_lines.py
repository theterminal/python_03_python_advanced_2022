# 20221004 - Python - Python Advanced - File Handling
# 01 - Even Lines


# _______________ version 2 _________________


file_path = 'L16_01_files/text_01.txt'
symbols = ['-', '.', ',', '!', '?']

with open(file_path, 'r') as text_file:
    all_rows = text_file.readlines()                            # list where every row from 'text-file' is an element

for row_i in range(0, len(all_rows), 2):
    for symbol in symbols:
        all_rows[row_i] = all_rows[row_i].replace(symbol, '@')

    # print(' '.join(all_rows[row_i].split()[::-1]))
    print(*all_rows[row_i].split()[::-1])


# _______________ version 1 _________________


import re


file_path = 'L16_01_files/text_01.txt'
pattern = r'[\-\.\,\!\?]+'

with open(file_path, 'r') as file_content:
    counter = 0
    for line in file_content:
        if counter % 2 == 0:
            line_reversed = reversed(line.split())
            line_out = ' '.join(line_reversed)
            line_out = re.sub(pattern, '@', line_out)
            print(line_out)
        counter += 1
