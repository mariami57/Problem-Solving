from typing import List
import heapq

# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums
#
#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort(reverse=True)
#
#         return self.nums[self.k-1]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
