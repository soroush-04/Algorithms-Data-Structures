from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue = deque()
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.popleft()
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)