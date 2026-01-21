# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_root = None
        tail = None

        def inorder(node):
            nonlocal new_root, tail
            if not node:
                return

            inorder(node.left)

            if new_root is None:
                new_root = node
                tail = node
            else:
                tail.right = node
                tail = node
            node.left = None
            inorder(node.right)

        inorder(root)
        return new_root