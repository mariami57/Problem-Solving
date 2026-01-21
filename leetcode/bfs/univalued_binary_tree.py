# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        prev = None

        while q:
            node = q.popleft()

            if prev:
                if node.val != prev.val:
                    return False
            prev = node

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return True

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
    tree = build_tree([1,1,1,1,1,None,1])
    tree1 = build_tree([2,2,2,5,2])
    print(Solution().isUnivalTree(tree))
    print(Solution().isUnivalTree(tree1))