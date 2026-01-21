# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        q = deque([(original, cloned)])

        while q:
            levels = len(q)

            for _ in range(levels):
                on, cn = q.popleft()
                if on == target:
                    return cn

                if on.left:
                    q.append((on.left, cn.left))

                if on.right:
                    q.append((on.right, cn.right))

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
    tree = build_tree([7,4,3,None,None,6,19])
    tree1 = build_tree([7,4,3,None,None,6,19])
    print(Solution().getTargetCopy(tree, tree1, 3))
