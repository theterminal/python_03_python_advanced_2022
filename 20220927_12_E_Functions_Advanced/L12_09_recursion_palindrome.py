# 20220927 - Python - Python Advanced - Functions Advanced
# 09 - Recursion Palindrome - judge: https://judge.softuni.org/Contests/Compete/Index/1839#8


# _______________ version 1 _________________ judge 100%


def palindrome(word: str, index: int):
    if index == len(word) // 2:
        return f'{word} is a palindrome'

    first, last = word[index], word[-1 - index]
    if first != last:
        return f'{word} is not a palindrome'

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
