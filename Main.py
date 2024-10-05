"""BFS traverse
"""

from typing import List
from collections import deque

class Graph:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
        
        
    def add_edge(self, node1, node2):
        self.adj_matrix[node1][node2] = 1
        self.adj_matrix[node2][node1] = 1
        
    
    def dfs_recursive(self, start, visited: List[int]):
        visited.append(start)
        
        for i in range(self.nodes):
            if self.adj_matrix[start][i] == 1 and i not in visited:
                self.dfs_recursive(i, visited)
                
    
    def dfs_iterative_check_cycle(self, start, visited: List[int]):
        stack =[(start, -1)]
        
        while stack:
            current, parent = stack.pop()
            visited.append(current)
            
            for i in range(self.nodes):
                if self.adj_matrix[current][i] == 1:
                    if i not in visited:
                        stack.append((i, current))
                    elif i != parent:
                        return True
        return False
                
    
    def count_component(self):
        counter = 0
        visited = []
        
        for i in range(self.nodes):
            if i not in visited:
                counter += 1
                self.dfs_recursive(i, visited)
        return counter
    
    
    def check_cycle(self, current, parent, visited: List[int]):
        visited.append(current)
        
        for i in range(self.nodes):
            if self.adj_matrix[current][i] == 1:
                if i not in visited:
                    if self.check_cycle(i, current, visited):
                        return True
                elif i != parent:
                    return True
        return False
        
                
    def check_valid_graph(self):
        visited = []

        if self.count_component() == 1 and self.dfs_iterative_check_cycle(0, visited) == 0 :
            return True
        else:
            return False 
    
    
    def find_path(self, start, end):
        path = []
        visited = []

        def dfs_helper(current):
            visited.append(current)
            path.append(current)

            if current == end:
                return True
            
            for i in range(self.nodes):
                if self.adj_matrix[current][i] == 1 and i not in visited:
                    if dfs_helper(i):
                        return True
                
            path.pop()
            return False
        
        dfs_helper(start)
        return path if end in path else []
    
    
    def bfs_traverse(self, start):
        queue = deque()
        visited = []
        
        queue.append(start)
        visited.append(start)
        
        while queue:
            current = queue.popleft()
            for i in range(self.nodes):
                if self.adj_matrix[current][i] == 1 and i not in visited:
                    queue.append(i)
                    visited.append(i)
        
        return visited
    
    def find_shortest_path(self, start, end):
        queue = deque()
        visited = []
        path = {}
        
        queue.append(start)
        visited.append(start)
        path[start] = None

        while queue:
            current = queue.popleft()
            
            for i in range(self.nodes):
                if self.adj_matrix[current][i] == 1 and i not in visited:
                    queue.append(i)
                    visited.append(i)
                    path[i] = current

                    if i == end:
                        shortest_path = []
                        while i is not None:
                            shortest_path.append(i)
                            i = path[i]
                        return shortest_path[::-1]
                    
        return []
    

graph1 = Graph(5)
graph1.add_edge(2, 0)
graph1.add_edge(2, 3)
graph1.add_edge(4, 3)
graph1.add_edge(1, 2)
graph1.add_edge(1, 3)
print(graph1.find_path(2, 4))
print(graph1.check_valid_graph()) 
print(graph1.bfs_traverse(1))
print(graph1.find_shortest_path(2, 4))
    
    
