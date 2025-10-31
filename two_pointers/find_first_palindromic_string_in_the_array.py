from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ''

print(Solution().firstPalindrome(words = ["abc","car","ada","racecar","cool"]))
print(Solution().firstPalindrome(words = ["notapalindrome","racecar"]))
print(Solution().firstPalindrome( words = ["def","ghi"]))