# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        sum_values  = 0

        def dfs(node):
            nonlocal sum_values
            if not node:
                return

            if low <= node.val <= high:
                sum_values += node.val

            dfs(node.left)
            dfs(node.right)
            return sum_values
        dfs(root)
        return sum_values

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
    tree = build_tree([10,5,15,3,7,None,18])
    tree1 = build_tree([10,5,15,3,7,13,18,1,None,6])
    print(Solution().rangeSumBST(tree, low = 7, high = 15))
    print(Solution().rangeSumBST(tree1, low = 6, high = 10))