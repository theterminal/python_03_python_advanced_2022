# 20221017 - Python - Python Advanced - Exam Preparation 3 - Self
# 03 - Words Sorting - judge: https://judge.softuni.org/Contests/Practice/Index/3430#2


# _______________ version 1 _________________ judge: 100%


def words_sorting(*words):
    word_dict = {}
    result = ''

    # creating a dictionary with all words from *words as keys,
    # calculating the sums of all ascii of the letters for each word,
    # adding the sums of each word as value in the dictionary
    for word in words:
        sum_ascii = 0
        for letter in word:
            sum_ascii += ord(letter)
        word_dict[word] = sum_ascii

    # finding the sum of all values in the dictionary (can be done in the previous step)
    sum_values = 0
    for k, v in word_dict.items():
        sum_values += v

    # sorting dictionary based on the sum of the values
    if sum_values % 2 == 0:
        # sort by keys in ascending order
        sorted_list = sorted(word_dict.items(), key=lambda x: x[0])
    else:
        # sort dict by values in descending order
        sorted_list = sorted(word_dict.items(), key=lambda x: -x[1])

    # creating a string as a result
    for k, v in sorted_list:
        result += f'{k} - {v}\n'

    return result


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape', 'charm', 'eye'))
print(words_sorting('cacophony', 'accolade'))
