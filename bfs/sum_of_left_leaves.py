# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        left_sum = 0

        while q:
            curr = q.popleft()

            if curr.left:
                if not curr.left.left and not curr.left.right:
                    left_sum += curr.left.val
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)
        return left_sum

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
    tree = build_tree([1,2,3,4,5])
    tree1 = build_tree([1])
    print(Solution().sumOfLeftLeaves(tree))
    print(Solution().sumOfLeftLeaves(tree1))
