"""
# Definition for a Node.

"""
from typing import Optional, List


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#
#         self.res = [root.val]
#
#         def preorder_tr(children):
#             for child in children:
#                 if not child:
#                     return
#                 self.res.append(child.val)
#
#                 if child.children:
#                     preorder_tr(child.children)
#
#             return self.res
#
#         preorder_tr(root.children)
#         return self.res


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return res
