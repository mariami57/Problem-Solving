# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         def dfs(node):
#             if not node:
#                 return
#
#             if node.val == target.val:
#                 return node
#
#             return dfs(node.left) or dfs(node.right)
#
#
#
#         return dfs(cloned)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None

        if original == target:
            return cloned

        return (self.getTargetCopy(original.left, cloned.left, target) or
                self.getTargetCopy(original.right, cloned.right, target))