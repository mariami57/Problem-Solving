# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_list = []
#
#         for char in s:
#             if char.isalnum():
#                 s_list.append(char.lower())
#
#         if s_list == s_list[::-1]:
#             return True
#         else:
#             return False



class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all(s[i] == s[~i] for i in range(len(s)//2))
print(Solution().isPalindrome("race a car"))