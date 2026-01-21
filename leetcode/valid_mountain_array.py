from typing import List


# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         if len(arr) < 3:
#             return False
#
#         end = max(arr)
#         end_idx = arr.index(end)
#         if end_idx == len(arr) - 1 or end == arr[0]:
#             return False
#
#         first_half = arr[:end_idx]
#         second_half = arr[end_idx+1:]
#
#         if end in first_half or end in second_half:
#             return False
#
#         for i in range(1, len(first_half)):
#             if first_half[i-1] >= first_half[i]:
#                 return False
#
#         for i in range(1, len(second_half)):
#             if second_half[i-1] <= second_half[i]:
#                 return False
#
#         return True


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start = 1
        end = len(arr) - 1
        length = len(arr)

        if length < 3:
            return False

        while start < length and arr[start] > arr[start-1]:
            start += 1

        while end > 0 and arr[end] < arr[end-1]:
            end -= 1

        start -= 1

        if start == length -1 or start == 0:
            return False

        return start == end

print(Solution().validMountainArray([0,3,2,1]))
print(Solution().validMountainArray([6,7,7,8,6]))
print(Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9]))
print(Solution().validMountainArray([3,5,5]))

print(Solution().validMountainArray([2,1]))
