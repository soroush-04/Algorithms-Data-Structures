from typing import List


class GraphPractice:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.adj_matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
        
    def add_edge(self, node1, node2):
        self.adj_matrix[node1][node2] = 1
        self.adj_matrix[node2][node1] = 1
        
    def remove_edge(self, node1, node2):
        self.adj_matrix[node1][node2] = 0
        self.adj_matrix[node2][node1] = 0
        
    def dfs(self, start, visited: List[int]):
        visited.append(start)
        print(f"current node is {start}")
        for i in range(self.nodes):
            if self.adj_matrix[start][i] == 1 and i not in visited:
                self.dfs(i, visited)
        
    def display_graph(self):
        for i in range(self.nodes):
            for j in range(i+1, self.nodes):
                if self.adj_matrix[i][j] == 1:
                    print(f"connected edge between node {i} and {j}")
    
    def display_matrix(self):
        for row in self.adj_matrix:
            print(row)
        print()
    
graph1 = GraphPractice(5)
graph1.display_matrix()
graph1.add_edge(2, 4)
graph1.add_edge(4, 0)
graph1.display_matrix()
graph1.display_graph()
#test dfs
visited_nodes = []
graph1.dfs(0, visited_nodes)