class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert_bst(self, node):
        new_node = Node(node)
        
        if self.root == None:
            self.root = new_node
        else:
            self._insert_bst(self.root, new_node)
    
    def _insert_bst(self, current: Node, new_node: Node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_bst(current.left, new_node)
                
        elif new_node.value > current.value:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_bst(current.right, new_node)
    