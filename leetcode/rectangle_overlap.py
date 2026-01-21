from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
      return not (rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3])

print(Solution().isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))
print(Solution().isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))
print(Solution().isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))