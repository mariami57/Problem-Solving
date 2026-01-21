# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(magazine) < len(ransomNote):
#             return False
#
#         used = []
#
#         for char in ransomNote:
#             if ransomNote.count(char) > magazine.count(char):
#                 return False
#             if char not in magazine:
#                 return False
#             used.append(char)
#
#
#         return True
from collections import Counter


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         maga_hash = {}
#
#         for c in magazine:
#             maga_hash[c] = 1 + maga_hash.get(c, 0)
#
#         for c in ransomNote:
#             if c not in maga_hash or maga_hash[c] <= 0:
#                 return False
#             maga_hash[c] -= 1
#
#         return True

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return st1 & st2 == st1

print(Solution().canConstruct(ransomNote = "fffbfg", magazine = "effjfggbffjdgbjjhhdegh"))
print(Solution().canConstruct(ransomNote = "a", magazine = "b"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "ab"))
print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))
