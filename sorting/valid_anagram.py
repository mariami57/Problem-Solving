# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         ana_dict1 = {}
#         ana_dict2 = {}
#
#         for char in s:
#             if char not in t:
#                 return False
#             ana_dict1[char] = ana_dict1.get(char, 0) + 1
#
#         for char in t:
#             if char not in s:
#                 return False
#             ana_dict2[char] = ana_dict2.get(char, 0) + 1
#
#         for key in ana_dict1:
#             if ana_dict1[key] == ana_dict2[key]:
#                 continue
#             return False
#         return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana_dict1 = {}

        for char in s:
            if char not in t:
                return False
            ana_dict1[char] = ana_dict1.get(char, 0) + 1

        for char in t:
            if char not in s or ana_dict1[char] == 0:
                return False
            ana_dict1[char] -= 1

        return True


print(Solution().isAnagram(s = "aa", t = "a"))
print(Solution().isAnagram(s = "rat", t = "car"))


