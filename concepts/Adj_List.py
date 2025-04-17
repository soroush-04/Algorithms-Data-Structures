from typing import List
from collections import deque

class Graph_List:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.adj_list = [[] for _ in range(nodes)]
        
    def add_edge(self, node1, node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
        
    def display(self):
        for i in range(self.nodes):
            print(f"{i}: {self.adj_list[i]}")
    
    def dfs_recursive(self, start):
        visited = []
        
        def helper(current):
            visited.append(current)
            
            for i in self.adj_list[current]:
                if i not in visited:
                    helper(i)
            
        helper(start)
        return visited
    
    def dfs_iterative(self, start):
        visited = []
        stack = []
        stack.append(start)

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.append(current)
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return visited
    
    def bfs(self, start):
        visited = []
        queue = deque()
        
        queue.append(start)

        while queue:
            current = queue.popleft()
            
            if current not in visited:
                visited.append(current)
                
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return visited
            
    

graph1 = Graph_List(5)
graph1.add_edge(2, 4)
graph1.add_edge(0, 3)
graph1.add_edge(0, 2)
graph1.display()
print(graph1.dfs_recursive(3))
print(graph1.dfs_iterative(2))
print("BFS:", graph1.bfs(0))