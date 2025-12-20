from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []

        some_str = s1 + ' ' + s2
        word_counter = Counter(some_str.split())
        for word in word_counter:
            if word_counter[word] == 1:
                res.append(word)


        return res

print(Solution().uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(Solution().uncommonFromSentences(s1 = "apple apple", s2 = "banana"))