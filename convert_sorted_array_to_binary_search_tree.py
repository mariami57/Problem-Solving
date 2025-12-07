# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        def convert(left, right):
            if left > right:
                return

            mid = (left + right)  // 2
            node = TreeNode(nums[mid])

            node.left = convert(left, mid -1)
            node.right = convert(mid+1, right)

            return node
        return convert(0, len(nums)-1)

print(Solution().sortedArrayToBST([-10,-3,0,5,9]))