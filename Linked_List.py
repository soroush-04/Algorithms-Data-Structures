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
        
    def delete_first_occurence(self, value):
        if self.head is None:
            return print("linked list is empty")
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
            
    def delete_all_occurence(self, value):
        if self.head is None:
            return print("linked list is empty")
        
        while self.head.value == value and self.head is not None:
            self.head = self.head.next
        
        current = self.head
        prev = None
        
        while current:
            if current.value == value:
                prev.next = current.next
            else:
                prev = current
            current = current.next
    
    def delete_by_index(self, index):
        if self.head is None:
            return print("linked list is empty")
        
        if index == 0:
            self.head = self.head.next
            return
        
        i = 0
        current = self.head
        prev = None
        
        while current:
            if i == index:
                prev.next = current.next
                return
            prev = current
            current = current.next
            i += 1
        
        print(f"index {index} is out of bound")

    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
    
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
ll.insert_at_beginning(7)
ll.insert_at_beginning(18)
ll.delete_by_index(0)
ll.traverse()
ll.reverse()
ll.traverse()