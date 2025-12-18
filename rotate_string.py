# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         i = 0
#
#         while i < len(s):
#             first_char = s[0]
#             rest = s[1:]
#             s = rest + first_char
#             if s == goal:
#                 return True
#             i += 1
#         return False

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s
print(Solution().rotateString(s = "abcde", goal = "cdeab"))
print(Solution().rotateString(s = "abcde", goal = "abced"))