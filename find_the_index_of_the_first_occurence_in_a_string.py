# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle in haystack:
#             return haystack.find(needle)
#         else:
#             return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, h = len(needle), len(haystack)
        if n == 0:
            return -1

        for i in range(h - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1

print(Solution().strStr("leetcode", "leeto"))