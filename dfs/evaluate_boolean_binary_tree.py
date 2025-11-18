# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if node.val == 1 or node.val == 0:
                return node.val == 1
            elif node.val == 2:
                return helper(node.left) or helper(node.right)
            elif node.val == 3:
                return helper(node.left) and helper(node.right)
            return False

        return helper(root)


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
    tree1 = build_tree([0])
    tree = build_tree([2,1,3,None,None,0,1])
    print(Solution().evaluateTree(tree1))
    print(Solution().evaluateTree(tree))



