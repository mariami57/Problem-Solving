# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return None
#         def convert(left, right):
#             if left > right:
#                 return
#
#             mid = (left + right)  // 2
#             node = TreeNode(nums[mid])
#
#             node.left = convert(left, mid -1)
#             node.right = convert(mid+1, right)
#
#             return node
#         return convert(0, len(nums)-1)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        mid = (len(nums) -1) // 2
        root = TreeNode(nums[mid])
        queue = deque([(root, 0, len(nums) - 1)])

        while queue:
            node, left, right = queue.popleft()

            mid = (left + right) // 2

            if left <= mid-1:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                queue.append((node.left, left, mid -1))

            if right >= mid + 1:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                queue.append((node.right, mid + 1, right))

        return root
print(Solution().sortedArrayToBST([1,3]))
print(Solution().sortedArrayToBST([-10,-3,0,5,9]))