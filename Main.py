"""Graph Valid Tree
Problem Summary
A graph is a valid tree if:

It is connected (there is a path between every pair of vertices).
It contains no cycles.
"""

from typing import List

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

        if self.count_component() == 1 and self.check_cycle(0, -1, visited) == 0 :
            return True
        else:
            return False 
        

    

graph1 = Graph(5)
graph1.add_edge(2, 0)
graph1.add_edge(2, 3)
graph1.add_edge(4, 0)
graph1.add_edge(1, 2)
graph1.add_edge(1, 3)

print(graph1.check_valid_graph()) 
    
    
