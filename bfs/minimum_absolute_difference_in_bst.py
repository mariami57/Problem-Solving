# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        vals = []
        q = deque([root])

        while q:
            node = q.popleft()
            vals.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        vals.sort()

        return min(vals[i+1] - vals[i] for i in range(len(vals)-1))


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
    tree = build_tree([4,2,6,1,3])
    tree1 = build_tree([1,0,48,None,None,12,49])
    print(Solution().getMinimumDifference(tree))
    print(Solution().getMinimumDifference(tree1))