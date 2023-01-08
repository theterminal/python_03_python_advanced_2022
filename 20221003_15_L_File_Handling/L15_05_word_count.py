
# 20221003 - Python - Python Advanced - File Handling
# 05 - Word Count


# _______________ version 1 _________________

import re


words_dict = {}
pattern = r'[a-zA-Z\']+'

with open('L15_05_word_count/words.txt', 'r') as words_file:
    all_words = words_file.read().split()
    words_dict = {word.lower(): 0 for word in all_words}

with open('L15_05_word_count/input.txt', 'r') as text_file:
    for line in text_file:
        all_line_words = re.findall(pattern, line)
        for word in all_line_words:
            word_lower = word.lower()
            if word_lower in words_dict:
                words_dict[word_lower] += 1

with open('./L15_05_word_count/output.txt', 'w') as result_file:
    sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])
    for word, count in sorted_words:
        result_file.write(f'{word} - {count}\n')


# ---------------------- version 2 -------------------------

import re


def read_target_words(path):
    result = []
    with open(path, 'r') as words_file:
        for line in words_file:
            result.extend(line.split())
    return result


def count_target_words(path, words):
    count_words = {word: 0 for word in words}
    with open(path, 'r') as text_file:
        for line in text_file:
            all_line_words = re.findall('[a-zA-Z\']+', line)
            for word in all_line_words:
                word_lower = word.lower()
                if word_lower in count_words:
                    count_words[word_lower] += 1
    return count_words


def write_result_to_file(path, count_words_dict):
    with open(path, 'w') as result_file:
        sorted_words = sorted(count_words_dict.items(), key=lambda x: -x[1])
        for word, count in sorted_words:
            result_file.write(f'{word} - {count}\n')


target_words = read_target_words('L15_05_word_count/words.txt')
count_words = count_target_words('L15_05_word_count/input.txt', target_words)
write_result_to_file('L15_05_word_count/output.txt', count_words)
