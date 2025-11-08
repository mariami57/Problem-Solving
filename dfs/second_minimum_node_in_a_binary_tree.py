# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root or not root.left:
            return -1

        left, right = root.left, root.right

        if left.val == root.val:
            left_second = self.findSecondMinimumValue(left)
        else:
            left_second = left.val

        if right.val == root.val:
            right_second = self.findSecondMinimumValue(right)
        else:
            right_second = right.val

        if left_second != -1 and right_second != -1:
            return min(left_second, right_second)
        elif left_second != -1:
            return left_second
        else:
            return right_second



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
    tree1 = build_tree([5,5,6])
    # tree = build_tree([2,2,5,None,None,5,7])

    print(Solution().findSecondMinimumValue(tree1))
    # print(Solution().findSecondMinimumValue(tree1))

