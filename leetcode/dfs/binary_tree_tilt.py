# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.node_sum = 0
        def find_sum(node):
            if not node:
                return 0

            left = find_sum(node.left)
            right = find_sum(node.right)

            self.node_sum += abs(left - right)

            return left + right + node.val

        find_sum(root)
        return self.node_sum

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
    tree1 = build_tree([4, 2, 9, 3, 5, None, 7])
    tree = build_tree([1,2,3])
    tree2 = build_tree([21,7,14,1,1,2,2,3,3])

    print(Solution().findTilt(tree1))
    print(Solution().findTilt(tree))
    print(Solution().findTilt(tree2))

