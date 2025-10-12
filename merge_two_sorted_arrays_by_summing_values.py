from typing import List


# class Solution:
#     def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
#         result = []
#         i, j = 0, 0
#
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i][0] == nums2[j][0]:
#                 result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
#                 i += 1
#                 j += 1
#             elif nums1[i][0] < nums2[j][0]:
#                 result.append(nums1[i])
#                 i += 1
#
#             else:
#                 result.append(nums2[j])
#                 j += 1
#         result.extend(nums1[i:])
#         result.extend(nums2[j:])
#
#         return result


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1.extend(nums2)
        nums1.sort()
        result = []
        for id, val in nums1:
            if result and result[-1][0] == id:
                result[-1][1] += val
            else:
                result.append([id,val])
        return result

print(Solution().mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))