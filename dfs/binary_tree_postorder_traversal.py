# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         res = []
#         def postorder(node):
#             if not node:
#                 return
#
#             postorder(node.left)
#             postorder(node.right)
#             res.append(node.val)
#
#             return res
#         postorder(root)
#         return res

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        s, res = [root], []


        while s:
            curr = s.pop()
            res.append(curr.val)
            if curr.left:
                s.append(curr.left)
            if curr.right:
                s.append(curr.right)
        return res[::-1]

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
    tree = build_tree([1,None,2,3])
    tree1 = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
    print(Solution().postorderTraversal(tree))
    print(Solution().postorderTraversal(tree1))

