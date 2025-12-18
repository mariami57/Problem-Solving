import re
from collections import Counter, defaultdict
from typing import List


# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         new_p = []
#         curr_str = ''
#
#         for char in paragraph:
#             if char.isalpha():
#                 curr_str += char
#             elif not char.isalpha() and curr_str:
#                 new_p.append(curr_str)
#                 curr_str = ''
#         if curr_str:
#             new_p.append(curr_str)
#
#
#         word_counter = {}
#
#         for w in new_p:
#             w = w.lower()
#             if w in word_counter:
#                 word_counter[w] += 1
#             else:
#                 word_counter[w] = 1
#
#         word_count = sorted(word_counter.items(), key=lambda x: -x[1])
#
#         for word, count in word_count:
#             if word not in banned:
#                 return word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(word.lower() for word in banned)

        words = re.split(r'[^A-Za-z]+', paragraph.lower())

        counter = defaultdict(int)
        max_count = 0
        result = ''

        for word in words:
            if word and word not in banned_set:
                counter[word] += 1
                if counter[word] > max_count:
                    max_count = counter[word]
                    result = word

        return result



print(Solution().mostCommonWord(paragraph = "Bob. hIt, baLl", banned = ["bob", "hit"]))
print(Solution().mostCommonWord(paragraph = "Bob", banned = [""]))
print(Solution().mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(Solution().mostCommonWord(paragraph = "a.", banned = []))

