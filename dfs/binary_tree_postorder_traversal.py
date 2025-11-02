# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#
#         def postorder(root):
#             if not root:
#                 return []
#             postorder(root.left)
#             postorder(root.right)
#             result.append(root.val)
#
#             return result
#
#         return postorder(root)


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        s = [root]

        while s:
            node = s.pop()
            res.append(node.val)

            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return res[::-1]