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
        
    def insert_at_end(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def insert_at_position(self, value, index):
        if index == 0:
            return self.insert_at_beginning(value)
        
        new_node = Node(value)
        current = self.head
        i = 0
        
        while current:
            if i == index - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            i += 1
        
        print("index out of bound")
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_at_end(4)
ll.insert_at_position(3, 0)
ll.insert_at_position(3, 2)
ll.insert_at_position(3, 10)
ll.traverse()