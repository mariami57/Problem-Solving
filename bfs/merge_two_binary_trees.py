# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            return root2

        if not root2:
            return root1

        queue = deque([(root1, root2)])

        while queue:
            c1, c2 = queue.popleft()

            if not c1 or not c2:
                continue

            c1.val = c1.val + c2.val

            if not c1.left:
                c1.left = c2.left
            else:
                queue.append((c1.left, c2.left))

            if not c1.right:
                c1.right = c2.right
            else:
                queue.append((c1.right, c2.right))
        return root1






