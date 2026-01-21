# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        default_val = root.val

        def dfs(node):
            nonlocal default_val
            if not node:
                return True

            if node.val != default_val:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            return left and right

        return dfs(root)

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
    tree1 = build_tree([1,1])
    tree = build_tree([1,1,1,1,1,None,1])
    print(Solution().isUnivalTree(tree1))
    print(Solution().isUnivalTree(tree))
