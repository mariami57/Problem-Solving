# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#
#         if word == word.upper() or (word[0] == word[0].upper() and word[1:] == word[1:].lower()) or word == word.lower():
#             return True
#         return False

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
            return True
        return False

print(Solution().detectCapitalUse(word = "Leetcode"))
print(Solution().detectCapitalUse(word = "USA"))
print(Solution().detectCapitalUse(word = "FlaG"))
