from collections import Counter
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        def is_substring(str1, str2):
            s1, s2 = 0, 0
            count = 0
            while s1 < len(str1) and s2 < len(str2):
                if str1[s1] == str2[s2]:
                    s2 += 1
                    s1 += 1
                else:
                    s2 += 1

            return s1 == len(str1)

        c = Counter(words)
        for w in set(words):
            if is_substring(w,s):
                cnt += c[w]
        return cnt

print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
