class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_edge(self, u, v, weight):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.append((u, v, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        mst = []
        self.edges.sort(key=lambda edge: edge[2])
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}

        for edge in self.edges:
            u, v, weight = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst


def print_menu():
    print("\nMenu:")
    print("1. Add Edge")
    print("2. Find Minimal Spanning Tree (MST)")
    print("3. Exit")


# Example usage:
g = Graph()

while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        u = input("Enter source vertex: ")
        v = input("Enter destination vertex: ")
        weight = int(input("Enter weight of the edge: "))
        g.add_edge(u, v, weight)
        print("Edge ({}, {}) with weight {} added.".format(u, v, weight))
    elif choice == '2':
        mst = g.kruskal_mst()
        print("Minimal Spanning Tree (MST):")
        for u, v, weight in mst:
            print("Edge:", u, "-", v, ", Weight:", weight)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
