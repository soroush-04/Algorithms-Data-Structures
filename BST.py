"""450. Delete Node in a BST"""

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
    
    def preorder_traversal(self, node: Node):
        if node is None:
            return
        print(node.value)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
    
    def inorder_traversal(self, node: Node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.value)
        self.inorder_traversal(node.right)
    
    def postorder_traversal(self, node: Node):
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.value)
    
    def search(self, target, current = None):
        if current is None:
            current = self.root
        
        if current is None:
            return None
        
        elif target == current.value:
            return current

        elif target < current.value:
            if current.left is None:
                return
            return self.search(target, current.left)
        
        elif target > current.value:
            if current.right is None:
                return
            return self.search(target, current.right)
    
    def delete_bst(self, key, current: Node = None):
        if current is None:
            current = self.root
        
        if current is None:
            return None #tree is empty
        
        if key < current.value:
            return self.delete_bst(key, current.left)
        elif key > current.value:
            return self.delete_bst(key, current.right)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            
            temp = self._find_min(current.right)
            current.value = temp.value
            current.right = self.delete_bst(temp.value, current.right)
        return current
    
    def _find_min(self, node: Node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        
    
bst = BST()
test_case = [5, 3, 7, 2, 4, 6, 8]

for i in test_case:
    bst.insert_bst(i)

print("Pre-order Traversal:")
bst.preorder_traversal(bst.root)
print("\nIn-order Traversal:")
bst.inorder_traversal(bst.root)
print("\nPost-order Traversal:")
bst.postorder_traversal(bst.root)
print(bst.search(5))
print(bst.delete_bst(3))
print("\nIn-order Traversal:")
bst.inorder_traversal(bst.root)