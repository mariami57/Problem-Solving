# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#
#         def traverse(curr):
#             if curr:
#                 traverse(curr.left)
#                 result.append(curr.val)
#                 traverse(curr.right)
#         traverse(root)
#         return result

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#
#         res = []
#         def inorder(node):
#             if not node:
#                 return
#
#             inorder(node.left)
#             res.append(node.val)
#             inorder(node.right)
#             return res
#
#         inorder(root)
#         return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        s = []
        res = []
        curr = root

        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            res.append(curr.val)
            curr = curr.right
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
    tree = build_tree([1,None,2,3])
    tree1 = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
    print(Solution().inorderTraversal(tree))
    print(Solution().inorderTraversal(tree1))
