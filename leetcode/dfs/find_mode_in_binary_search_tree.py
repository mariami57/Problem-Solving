# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#
#         counts = {}
#         max_count = 0
#         modes = []
#
#         def inorder(node):
#             if not node:
#                 return
#
#             inorder(node.left)
#
#             nonlocal max_count, modes
#
#             counts[node.val]  = 1 + counts.get(node.val, 0)
#
#             if counts[node.val] > max_count:
#                 max_count = counts[node.val]
#                 modes = [node.val]
#             elif counts[node.val] == max_count:
#                 modes.append(node.val)
#
#             inorder(node.right)
#
#         inorder(root)
#         return modes
#


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.prev = None
        self.modes = []
        self.max_count = 0
        self.count  = 0

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if node.val == self.prev:
                self.count += 1
            else:
                self.count = 1
                self.prev = node.val

            if self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                self.modes.append(node.val)

            inorder(node.right)

        inorder(root)
        return self.modes


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
    tree1 = build_tree([0])
    tree = build_tree([1,None,2,2])
    print(Solution().findMode(tree))
    print(Solution().findMode(tree1))
