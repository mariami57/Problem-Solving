from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []
        res = []

        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path)
                return

            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))

            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))


        dfs(root, str(root.val))


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
    tree = build_tree([1,2,3,None,5])
    tree1 = build_tree([1])
    print(Solution().binaryTreePaths(tree))
    print(Solution().binaryTreePaths(tree1))



