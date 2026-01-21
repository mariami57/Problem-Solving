from typing import List


# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         expected = heights.copy()
#         expected.sort()
#         res = 0
#         for i in range(len(heights)):
#             if heights[i] != expected[i]:
#                 res += 1
#         return res

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                        res += 1
        return res


print(Solution().heightChecker([1,1,4,2,1,3]))
print(Solution().heightChecker([5,1,2,3,4]))
print(Solution().heightChecker([1,2,3,4,5]))