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
    
    def preorder_traversal(self, node: Node):
        if node is None:
            return
        print(node.value)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
        
    def inorder_traversal(self, node:Node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.value)
        self.inorder_traversal(node.right)

    def postorder_traversal(self, node:Node):
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.value)
                
    def print_tree(self, node: Node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)
            
        
binary_tree = BinaryTree()

binary_tree.insert_node(10)
binary_tree.insert_node(5)
binary_tree.insert_node(15)
binary_tree.insert_node(3)
binary_tree.insert_node(7)
binary_tree.insert_node(12)
binary_tree.insert_node(18)

print("Pre-order Traversal:")
binary_tree.preorder_traversal(binary_tree.root)
print("In order Traversal:")
binary_tree.inorder_traversal(binary_tree.root)
print("Post order Traversal:")
binary_tree.postorder_traversal(binary_tree.root)