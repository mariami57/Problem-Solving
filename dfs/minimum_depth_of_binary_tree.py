# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#
#         left_depth = self.minDepth(root.left)
#         right_depth = self.minDepth(root.right)
#
#         if left_depth != 0 and right_depth != 0:
#             return 1 + min(left_depth, right_depth)
#         return 1 + max(left_depth, right_depth)

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#
#         current_depth = 1
#         queue = [root]
#
#         while queue:
#             for _ in range(len(queue)):
#                 node = queue.pop(0)
#
#                 if not node.left and not node.right:
#                     return current_depth
#
#                 if node.left:
#                     queue.append(node.left)
#
#                 if node.right:
#                     queue.append(node.right)
#             current_depth += 1
#         return current_depth


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if 1 + min(left, right) == 1:
            return 1 + max(left,right)
        return 1 + min(left,right)




def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i <len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i +=1
    return root

if __name__ =='__main__':
    tree = build_tree([3,9,20,None,None,15,7])
    tree1 = build_tree([2,None,3,None,4,None,5,None,6])
    print(Solution().minDepth(tree))
    print(Solution().minDepth(tree1))