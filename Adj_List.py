from typing import List

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
            

graph1 = Graph_List(5)
graph1.add_edge(2, 4)
graph1.add_edge(0, 3)
graph1.add_edge(0, 2)
graph1.display()