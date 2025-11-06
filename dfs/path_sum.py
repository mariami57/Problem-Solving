# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#
#         if not root.left and not root.right:
#             return targetSum - root.val == 0
#
#         targetSum -= root.val
#
#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right and targetSum - root.val == 0:
            return True
        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#         node_sum  = []
#
#         def calc_sum(node):
#             if not node:
#               return False
#
#             node_sum.append(node.val)
#
#             if not node.left and not node.right and sum(node_sum) == targetSum:
#                 return True
#
#
#             left = calc_sum(node.left)
#             right = calc_sum(node.right)
#
#             node_sum.pop()
#
#             return left or right
#
#
#         return calc_sum(root)



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
    tree = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    tree1 = build_tree([1,2,3])
    print(Solution().hasPathSum(tree,  targetSum = 22))
    print(Solution().hasPathSum(tree1, targetSum = 5))