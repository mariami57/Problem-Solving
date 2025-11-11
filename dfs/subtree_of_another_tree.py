# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def is_same_tree(self, node, subnode):
        if not node and not subnode:
            return True

        if not node or not subnode:
            return False

        if node.val != node.val:
            return False

        return (self.is_same_tree(node.left, subnode.left) and
                self.is_same_tree(node.right, subnode.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        if self.is_same_tree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))


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

def build_subtree(values):
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
    tree1 = build_tree([3,4,5,1,2,None,None,None,None,0])
    subtree1 = build_subtree([4,1,2])
    tree = build_tree([3,4,5,1,2])
    subtree = build_subtree([4,1,2])
    print(Solution().isSubtree(tree, subtree))
    print(Solution().isSubtree(tree1, subtree1))