"""Connected Components
Problem Statement: Given an undirected graph, count the number of connected components.

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
                
    def count_connected_components(self):
        visited = []
        counter = 0
        
        for i in range(self.nodes):
            if i not in visited:
                self.dfs_recursive(i, visited)
                counter += 1
        
        return print(counter)
    
graph1 = Graph(6)
graph1.add_edge(2, 0)
graph1.add_edge(2, 3)
graph1.add_edge(4, 0)
graph1.count_connected_components()
    