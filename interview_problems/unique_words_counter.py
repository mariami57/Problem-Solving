
# def count_words(text: str) -> dict:
#     words = text.split()
#
#     unique_words = {}
#     for word in words:
#         if not word[-1].isalpha():
#             word = word.strip(word[-1]).lower()
#         unique_words[word] = unique_words.get(word, 0) + 1
#
#     return unique_words

import re
from collections import Counter


def count_words(text: str) -> dict:
    matches = re.findall(r'[A-Za-z]+', text.lower())
    unique_words = Counter(matches)

    return unique_words


print(count_words("Python is great. Python is easy to learn, and Python is fun!"))