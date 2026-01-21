# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
#         if not root:
#             return []
#
#         q = deque([root])
#         p = deque([root])
#         res = []
#         while q:
#             if p:
#                 p_len = len(p)
#                 avg = sum(n.val for n in p) / p_len
#                 res.append(avg)
#             p = deque([])
#
#             for _ in range(len(q)):
#                 curr = q.popleft()
#
#                 if curr.left:
#                     q.append(curr.left)
#                     p.append(curr.left)
#
#                 if curr.right:
#                     q.append(curr.right)
#                     p.append(curr.right)
#         return res


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_sum = 0
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            res.append(level_sum / len_q)
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

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

if __name__ == '__main__':
    tree = build_tree([3,1,5,0,2,4,6])
    tree1 = build_tree([3,9,20,15,7])
    print(Solution().averageOfLevels(tree))
    print(Solution().averageOfLevels(tree1))
