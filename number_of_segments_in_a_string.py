# class Solution:
#     def countSegments(self, s: str) -> int:
#         if s == 0:
#             return 0
#
#         start, end = 0, 0
#         segments = 0
#
#         while start < len(s) and end < len(s):
#             while s[end] != ' ' and end <= len(s)-2:
#                 end += 1
#             if s[start:end+1] != ' ':
#                 segments += 1
#             start, end = end + 1, end + 1
#
#         return segments

class Solution:
    def countSegments(self, s: str) -> int:
        if s == 0:
            return 0

        s = s.split()

        return len(s)

print(Solution().countSegments(s = "Of all the gin joints in all the towns in all the world,   "))
print(Solution().countSegments(s = "                "))
print(Solution().countSegments(s = "Hello, my name is John"))
print(Solution().countSegments(s = "Hello"))
