# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(curr):
            if curr:
                traverse(curr.left)
                result.append(curr.val)
                traverse(curr.right)
        traverse(root)
        return result