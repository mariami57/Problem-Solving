"""
# Definition for a Node.

"""
from collections import deque
from typing import Optional, List


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        max_depth = 0

        q = deque([root])

        while q:
            level_size = len(q)
            max_depth += 1

            for _ in range(level_size):
                node = q.popleft()

                for child in node.children:
                    q.append(child)

        return max_depth

