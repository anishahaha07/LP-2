class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_edge(self, u, v, weight):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges[(u, v)] = weight
        self.edges[(v, u)] = weight

    def prim_mst(self):
        mst = set()
        visited = set()
        start_vertex = next(iter(self.vertices))
        visited.add(start_vertex)

        while len(visited) < len(self.vertices):
            min_edge = None
            min_weight = float('inf')

            for edge, weight in self.edges.items():
                u, v = edge
                if (u in visited and v not in visited) or (u not in visited and v in visited):
                    if weight < min_weight:
                        min_edge = edge
                        min_weight = weight

            if min_edge:
                mst.add(min_edge)
                visited.add(min_edge[0])
                visited.add(min_edge[1])

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
        mst = g.prim_mst()
        print("Minimal Spanning Tree (MST):")
        for edge in mst:
            print("Edge:", edge[0], "-", edge[1], ", Weight:", g.edges[edge])
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
