from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        check = ''

        for i in range(len(words)):
            check += words[i]

            if s.startswith(check) and len(check) == len(s):
                return True

        return False

print(Solution().isPrefixString(s = "iloveleetcode", words = ["i","apples","love","leetcode"]))
print(Solution().isPrefixString(s = "a", words = ["a","ad","cookie"]))