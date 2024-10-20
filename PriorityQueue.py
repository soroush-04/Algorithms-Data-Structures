import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        if self.isEmpty():
            return None
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0][1]

    def isEmpty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


pq = PriorityQueue()
pq.enqueue("Task A", 4)
pq.enqueue(999, 1)
pq.enqueue("Task C", 3)

print(pq.dequeue())
print(pq.peek())
print(pq.size())
