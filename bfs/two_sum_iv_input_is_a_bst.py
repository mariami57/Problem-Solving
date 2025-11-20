# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        queue = deque([root])
        diffs = set()

        while queue:
            node = queue.popleft()

            if node.val in diffs:
                return True
            diffs.add(k - node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False



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
    tree = build_tree([5,3,6,2,4,None,7])
    tree1 = build_tree([5,3,6,2,4,None,7])
    print(Solution().findTarget(tree, 9))
    print(Solution().findTarget(tree1, 28))
