# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#
#         result = []
#         def preorder(node):
#             if not node:
#                 return
#
#             result.append(node.val)
#             preorder(node.left)
#             preorder(node.right)
#
#         preorder(root)
#         return result

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = [root]
        res = []


        while s:
            node = s.pop()
            res.append(node.val)

            if node.right:
                s.append(node.right)

            if node.left:
                s.append(node.left)
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

        if i <len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i +=1
    return root

if __name__ =='__main__':
    # tree = build_tree([1,None,2,3])
    tree1 = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
    # print(Solution().preorderTraversal(tree))
    print(Solution().preorderTraversal(tree1))