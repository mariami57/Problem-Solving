# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.prev = None
        self.min_dis = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if self.prev is not None:
                self.min_dis = min(self.min_dis, abs(self.prev - node.val))
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_dis


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
    tree = build_tree([4,2,6,1,3])
    tree1 = build_tree([1,0,48,None,None,12,49])
    print(Solution().minDiffInBST(tree))
    print(Solution().minDiffInBST(tree1))
