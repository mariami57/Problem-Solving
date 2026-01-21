# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        sums = []
        counts = []

        def dfs(node, level):
            if not node:
                return
            if level == len(sums):
                sums.append(node.val)
                counts.append(1)
            else:
                sums[level] += node.val
                counts[level] += 1

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return [s /c for s,c in zip(sums,counts)]

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
    tree1 = build_tree([3,9,20,15,7])
    print(Solution().averageOfLevels(tree))
    print(Solution().averageOfLevels(tree1))

