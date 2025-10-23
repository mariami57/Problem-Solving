# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = set()

        def preorder(node):
            if not node:
                return False

            if k - node.val in values:
                return True
            values.add(node.val)

            if preorder(node.right):
                return True

            if preorder(node.left):
                return True

            return False

        return preorder(root)