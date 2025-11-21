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
#         min_depth = 1
#
#         queue = deque()
#         queue.append(root)
#
#         while queue:
#             node = queue.popleft()
#
#
#             if not node.left and not node.right:
#                 return min_depth
#
#             if node.left:
#                 queue.append(node.left)
#
#             if node.right:
#                 queue.append(node.right)
#             min_depth += 1
#         return min_depth

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque([root])
        min_depth = float('inf')
        curr_depth = 0

        while q:
            curr_depth += 1

            for _ in range(len(q)):
                node = q.popleft()

                if not node.left and not node.right:
                    min_depth = min(min_depth, curr_depth)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
        return min_depth

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

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

if __name__ == '__main__':
    tree = build_tree([3,9,20,None,None,15,7])
    tree1 = build_tree([2,None,3,None,4,None,5,None,6])
    print(Solution().minDepth(tree))
    print(Solution().minDepth(tree1))