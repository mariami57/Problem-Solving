# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return []

            leaves = dfs(root.left) + dfs(root.right)

            return leaves or [root.val]
        return dfs(root1) == dfs(root2)

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
    tree = build_tree([3,5,1,6,2,9,8,None,None,7,4])
    tree2 = build_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    tree1 = build_tree([1,0,48,None,None,12,49])
    print(Solution().leafSimilar(tree, tree2))


