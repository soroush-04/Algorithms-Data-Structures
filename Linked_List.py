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
        while self.head is not None:
            print(self.head.value, end=" -> ")
            self.head = self.head.next
        print("None")


ll = LinkedList()
ll.insert_at_beginning(2)
ll.traverse()