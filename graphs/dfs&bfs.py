from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Adding the edge from u to v (directed or undirected, you can modify accordingly)
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start_node):
        visited = set()  # Track visited nodes
        queue = deque([start_node])  # Initialize queue for BFS
        visited.add(start_node)

        print("BFS Traversal:")
        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print()

    def dfs(self, start_node):
        visited = set()  # Track visited nodes

        def dfs_recursive(node):
            visited.add(node)
            print(node, end=" ")

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        print("DFS Traversal:")
        dfs_recursive(start_node)
        print()

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform BFS and DFS starting from node 2
g.bfs(2)
g.dfs(2)
