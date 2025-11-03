# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(left_child, right_child, level):
            if not left_child or not right_child:
                return
            if level % 2 == 0:
                left_child.val, right_child.val = right_child.val, left_child.val
            dfs(left_child.left, right_child.right, level+1)
            dfs(left_child.right, right_child.left, level+1)

        dfs(root.left, root.right, 0)
        return root


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
    tree = build_tree([2,3,5,8,13,21,34])
    tree1 = build_tree([7,13,11])
    tree2 = build_tree([0,1,2,0,0,0,0,1,1,1,1,2,2,2,2])
    print(Solution().reverseOddLevels(tree))
    print(Solution().reverseOddLevels(tree1))
    print(Solution().reverseOddLevels(tree2))