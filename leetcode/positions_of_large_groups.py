from typing import List


# class Solution:
#     def largeGroupPositions(self, s: str) -> List[List[int]]:
#         result = []
#         i = 1
#         while i < len(s)-1:
#             if s[i-1] == s[i] == s[i+1]:
#                 start_idx = i - 1
#                 while s[i] == s[start_idx] and i < len(s)-1:
#                     i+=1
#                 if i == len(s) - 1 and s[i-1] == s[-1]:
#                     end_idx = i
#                 else:
#                     end_idx = i - 1
#                 result.append([start_idx, end_idx])
#             i += 1
#
#         return result

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0

        while start < len(s):
            end = start
            while end < len(s) and s[end] == s[start]:
                end += 1
            if end - start >= 3:
                result.append([start, end-1])

            start = end
        return result
print(Solution().largeGroupPositions(s = "bababbaaab"))
print(Solution().largeGroupPositions(s = "aaa"))
print(Solution().largeGroupPositions(s = "abbxxxxzzy"))
print(Solution().largeGroupPositions(s = "abc"))
print(Solution().largeGroupPositions(s = "abcdddeeeeaabbbcd"))

