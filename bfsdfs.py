class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start):
        visited = {node: False for node in self.graph}
        self.dfs_recursive(start, visited)

    def bfs(self, start):
        visited = {node: False for node in self.graph}
        queue = [start]
        visited[start] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

def print_menu():
    print("\nMenu:")
    print("1. Add Edge")
    print("2. Depth First Search (DFS)")
    print("3. Breadth First Search (BFS)")
    print("4. Exit")

# Example usage:
g = Graph()

while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        u = int(input("Enter source vertex: "))
        v = int(input("Enter destination vertex: "))
        g.add_edge(u, v)
        print("Edge ({}, {}) added.".format(u, v))
    elif choice == '2':
        start_vertex = int(input("Enter the starting vertex for DFS: "))
        print("DFS traversal:")
        g.dfs(start_vertex)
    elif choice == '3':
        start_vertex = int(input("Enter the starting vertex for BFS: "))
        print("BFS traversal:")
        g.bfs(start_vertex)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
