# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        info = {}

        def dfs(node, parent, level):
            if not node:
                return

            if node.val == x or node.val == y:
                info[node.val] = (parent, level)

            dfs(node.left, node.val, level + 1)
            dfs(node.right, node.val, level + 1)

        dfs(root, None, 0)

        if x in info and y in info:
            px,lx=info[x]
            py,ly=info[y]

            return lx == ly and px != py
        return False

