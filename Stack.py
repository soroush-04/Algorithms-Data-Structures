class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def push(self, value):
        if isinstance(value, list):
            for i in value:
                self.push(i)
        else:
            self.stack.append(value)
            if not self.min_stack or value <= self.min_stack[-1]:
                self.min_stack.append(value)
            if not self.max_stack or value >= self.max_stack[-1]:
                self.max_stack.append(value)
        
    def pop(self):
        if self.isEmpty():
            return None
        else:
            if self.peek() == self.min_stack[-1]:
                self.min_stack.pop()
            if self.peek() == self.max_stack[-1]:
                self.max_stack.pop()
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]
        
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None
    
    def get_max(self):
        return self.max_stack[-1] if self.max_stack else None
    
    def isEmpty(self):
        return len(self.stack) == 0
    
stack = Stack()
print(stack.isEmpty())
stack.push([1,2,3])
print(stack.peek())
stack.pop()
print(stack.peek())