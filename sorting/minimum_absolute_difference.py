from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        result = []

        i = 0
        j = 1

        while i < len(arr) and j < len(arr):
            min_diff = min(min_diff, abs(arr[i] - arr[j]))
            i += 1
            j += 1

        i = 0
        j = 1
        while i < len(arr) and j < len(arr):
            if abs(arr[i] - arr[j]) == min_diff:
                result.append([arr[i], arr[j]])
            i += 1
            j += 1

        return result


# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         arr.sort()
#         min_diff = float('inf')
#         result = []
#
#         i = 0
#         j = 1
#
#         while i < len(arr) and j < len(arr):
#             if min_diff > abs(arr[i] - arr[j]):
#                 min_diff = abs(arr[i] - arr[j])
#                 result = [[arr[i], arr[j]]]
#             elif abs(arr[i] - arr[j]) == min_diff:
#                 result.append([arr[i], arr[j]])
#             i += 1
#             j += 1
#
#         return result


print(Solution().minimumAbsDifference([4,2,1,3]))
print(Solution().minimumAbsDifference([1,3,6,10,15]))
print(Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))