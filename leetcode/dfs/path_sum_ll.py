# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, curSum):
            if not node:
                return
            curSum += node.val
            path.append(node.val)
            if not node.left and not node.right and curSum == targetSum:
                res.append(path[:])
            dfs(node.left, path, curSum)
            dfs(node.right, path, curSum)
            path.pop()
        dfs(root, [], 0)
        return res

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
    tree = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    tree1 = build_tree([1,2,3])
    tree2 = build_tree([1,2])
    print(Solution().pathSum(tree,  targetSum = 22))
    print(Solution().pathSum(tree1, targetSum = 5))
    print(Solution().pathSum(tree2, targetSum = 0))