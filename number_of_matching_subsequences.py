from collections import Counter
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        def is_substring(str1, str2):
            st, wp = 0, 0
            count = 0
            while st < len(str1) and wp < len(str2):
                if str1[st] == str2[wp]:
                    wp += 1
                    st += 1
                    count += 1
                else:
                    wp += 1

            return count == len(str1)

        c = Counter(words)
        for w in set(words):
            if is_substring(w,s):
                cnt += c[w]
        return cnt

print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
