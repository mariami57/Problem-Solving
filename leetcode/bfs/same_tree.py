# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if p is None and q is None:
#             return True
#
#         if p is None or q is None:
#             return False
#
#         queue = deque()
#         queue.append((p,q))
#
#         while queue:
#             node1, node2 = queue.popleft()
#
#             if not node1 and not node2:
#                 continue
#             if not node1 or not node2:
#                 return False
#             if node1.val != node2.val:
#                 return False
#
#             queue.append((node1.left, node2.left))
#             queue.append((node1.right, node2.right))
#         return True


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        queue = deque([(p, q)])

        while queue:
            np, nq = queue.popleft()

            if np.val != nq.val:
                return False

            if np.left and nq.left:
                queue.append((np.left, nq.left))
            elif np.left or nq.left:
                return False

            if np.right and nq.right:
                queue.append((np.right, nq.right))
            elif np.right or nq.right:
                return False
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

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

if __name__ == '__main__':
    tree = build_tree([1,2,1])
    tree1 = build_tree([1,1,2])
    print(Solution().isSameTree(tree, tree1))
