"""
Maximum Depth of Binary Tree
"""

from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root or root.val == val:
#             return root
#         if root.val > val:
#             return self.searchBST(root.left, val)
#         else:
#             return self.searchBST(root.right, val)


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)

    def searchBST(self, val):
        self._searchBST(self.root, val)

    def _searchBST(self, node, val):
        if not node:
            return None
        if node.value == val:
            return node
        elif node.value > val:
            return self._searchBST(node.left, val)
        else:
            return self._searchBST(node.right, val)
