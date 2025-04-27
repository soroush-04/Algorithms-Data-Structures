"""
Diameter of Binary Tree

        1
       / \
      2   3
     / \
    4   5


"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def calculate_max_diameter(self):
        self.diameter = 0

        def dfs(node: TreeNode):
            if not node:
                return 0

            letf_height = dfs(node.left)
            right_height = dfs(node.right)

            self.diameter = max(self.diameter, letf_height + right_height)

            return max(letf_height, right_height) + 1

        dfs(self.root)

        return self.diameter


tree = Tree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

print(tree.calculate_max_diameter())
