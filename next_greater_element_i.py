from collections import defaultdict
from typing import List


# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = []
#
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i] == nums2[j] and j < len(nums2) - 1:
#                     for x in range(j, len(nums2)):
#                         if nums2[x] > nums2[j]:
#                             result.append(nums2[x])
#                             break
#                     else:
#                         result.append(-1)
#                 elif nums1[i] == nums2[j] and j == len(nums2) - 1:
#                     result.append(-1)
#         return result


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        ng = defaultdict(lambda:-1)

        for num in nums2:
            while result and result[-1] < num:
                ng[result.pop()] = num
            result.append(num)
        return [ng[num] for num in nums1]

print(Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(Solution().nextGreaterElement(nums1 = [2,1,3], nums2 = [2,3,1]))
print(Solution().nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
