from typing import List


# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         indexes = {}
#
#         for i in range(len(nums)):
#             if nums[i] not in indexes:
#                 indexes[nums[i]] = [i]
#             else:
#                 indexes[nums[i]].append(i)
#
#         for val in indexes.values():
#             for j in range(len(val) - 1):
#                 if abs(val[j] - val[(j + 1)]) <= k:
#                     return True
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        return False
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1))


