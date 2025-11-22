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

        q = deque([root])
        depth = 0
        while q:
            depth += 1
            q_len = len(q)

            for _ in range(len(q)):
                node = q.popleft()

                for child in node.children:
                    q.append(child)
        return depth



