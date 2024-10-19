class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value):
        if isinstance(value, list):
            self.stack.extend(value)
        else:
            self.stack.append(value)
        
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
stack = Stack()
print(stack.isEmpty())
stack.push([1,2,3])
print(stack.peek())
stack.pop()
print(stack.peek())