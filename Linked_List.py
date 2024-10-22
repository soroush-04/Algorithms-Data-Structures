class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_at_beginning(2)
ll.insert_at_beginning(4)
ll.traverse()