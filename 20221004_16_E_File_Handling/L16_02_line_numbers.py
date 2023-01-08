# 20221004 - Python - Python Advanced - File Handling
# 02 - Line Numbers


# _______________ version 1 _________________


from string import punctuation
# print(punctuation)


input_file_path = 'L16_02_files/text_02.txt'
output_file_path = 'L16_02_files/output_02.txt'

with open(input_file_path, 'r') as text_file:
    text = text_file.readlines()

with open(output_file_path, 'w') as output_file:
    for i in range(len(text)):
        row = text[i]

        letters = 0
        marks = 0

        for symbol in row:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                marks += 1

        output_file.write(f'Line {i + 1}: {"".join(row[:-1])} ({letters}) ({marks})\n')


# _______________ version 2 _________________


from os import path
import re

absolute_path = path.dirname(path.abspath(__file__))
file_path = path.join(absolute_path, "text.txt")

with open(file_path, "r") as file, open("./output.txt", "w") as output_file:
    for idx, line in enumerate(file.readlines(), 1):
        letters_number = len(re.findall(r"[A-z]", line))
        punctuation_marks_count = len(re.findall(r"[^\w\s\d]", line))
        output_file.writelines(f"Line {idx}: {line.strip()} ({letters_number})({punctuation_marks_count})" + "\n")
