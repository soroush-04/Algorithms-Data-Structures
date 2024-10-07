from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert_node(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
        else:
            queue = deque([self.root])

            while queue:
                current = queue.popleft()

                if current.left is None:
                    current.left = new_node
                    return
                
                queue.append(current.left)
                
                if current.right is None:
                    current.right = new_node
                    return
                
                queue.append(current.right)
                
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)  # Print right subtree
            print(' ' * 4 * level + '->', node.value)  # Print current node
            self.print_tree(node.left, level + 1)
            
        
# Create a binary tree instance
binary_tree = BinaryTree()

# Insert nodes
binary_tree.insert_node(10)
binary_tree.insert_node(5)
binary_tree.insert_node(15)
binary_tree.insert_node(3)
binary_tree.insert_node(7)
binary_tree.insert_node(12)
binary_tree.insert_node(18)

binary_tree.print_tree(binary_tree.root)
