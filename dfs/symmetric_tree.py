# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#
#         def is_mirror(n1, n2):
#             if not n1 and not n2:
#                 return True
#
#             if not n1 or not n2:
#                 return False
#
#             return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
#
#
#         return is_mirror(root.left, root.right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right

        if not left and not right:
            return True

        if (left and not right) or (not left and right):
            return False

        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
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

        if i <len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i +=1
    return root

if __name__ =='__main__':
    tree = build_tree([1,2,2,None,3,None,3])
    print(Solution().isSymmetric(tree))
