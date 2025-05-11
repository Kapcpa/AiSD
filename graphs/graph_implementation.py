class Graph:
    def __init__(self, nodes: int): pass

    def add_edge(self, u: int, v: int): pass

    def print(self): pass

    def find(self): pass

    @property
    def start_node(self) -> int | None: pass

    def bfs(self): pass

    def dfs(self): pass

    def topological_sort_kahn(self): pass

    def topological_sort_tarjan(self): pass


class AdjacencyListGraph(Graph):
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.adjacent = [[] for _ in range(nodes)]

    def add_edge(self, u: int, v: int):
        self.adjacent[u].append(v)

    def print(self):
        for i in range(self.nodes):
            print(f"{i}: {self.adjacent[i]}")
    
    def find(self):
        u = int(input("from> "))
        v = int(input("to> "))
        print(f"Edge {(u, v)} {"does" if v in self.adjacent[u] else "does not"} exist in the graph")

    @property
    def start_node(self) -> int | None:
        for node in range(self.nodes):
            if all([node not in edges for edges in self.adjacent]):
                return node
        return None

    def bfs(self):
        start = self.start_node

        visited = [False] * self.nodes
        queue = [start]
        visited[start] = True

        print("BFS> ", end=" ")
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            for v in self.adjacent[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        print()

    def dfs(self):
        visited = [False] * self.nodes

        def dfs_recursive(u):
            visited[u] = True
            print(u, end=" ")
            for v in self.adjacent[u]:
                if not visited[v]:
                    dfs_recursive(v)
        
        print("DFS> ", end=" ")
        dfs_recursive(self.start_node)
        print()


class EdgeTableGraph(Graph):
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, u: int, v: int):
        self.edges.append((u, v))

    def print(self):
        print("Edges:")
        for u, v in self.edges:
            print(f"{u} -> {v}")

    def find(self):
        u = int(input("from> "))
        v = int(input("to> "))
        print(f"Edge {(u, v)} {'does' if (u, v) in self.edges else 'does not'} exist in the graph")

    @property
    def start_node(self) -> int | None:
        all_nodes = set(range(self.nodes))
        destinations = {v for _, v in self.edges}
        sources = all_nodes - destinations
        return min(sources) if sources else None

    def bfs(self):
        start = self.start_node
        visited = [False] * self.nodes
        queue = [start]
        visited[start] = True

        print("BFS> ", end=" ")
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            for v in [v for (x, v) in self.edges if x == u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        print()

    def dfs(self):
        visited = [False] * self.nodes

        def dfs_recursive(u):
            visited[u] = True
            print(u, end=" ")
            for v in [v for (x, v) in self.edges if x == u]:
                if not visited[v]:
                    dfs_recursive(v)
        
        print("DFS> ", end=" ")
        dfs_recursive(self.start_node)
        print()


class MatrixGraph(Graph):
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.matrix = [[0] * nodes for _ in range(nodes)]

    def add_edge(self, u: int, v: int):
        self.matrix[u][v] = 1

    def print(self):
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def find(self):
        u = int(input("from> "))
        v = int(input("to> "))
        print(f"Edge {(u, v)} {'does' if self.matrix[u][v] else 'does not'} exist in the graph")

    @property
    def start_node(self) -> int | None:
        for node in range(self.nodes):
            if all(self.matrix[other][node] == 0 for other in range(self.nodes)):
                return node
        return None

    def bfs(self):
        start = self.start_node
        visited = [False] * self.nodes
        queue = [start]
        visited[start] = True

        print("BFS> ", end=" ")
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            for v in range(self.nodes):
                if self.matrix[u][v] and not visited[v]:
                    visited[v] = True
                    queue.append(v)
        print()

    def dfs(self):
        visited = [False] * self.nodes

        def dfs_recursive(u):
            visited[u] = True
            print(u, end=" ")
            for v in range(self.nodes):
                if self.matrix[u][v] and not visited[v]:
                    dfs_recursive(v)
        
        print("DFS> ", end=" ")
        dfs_recursive(self.start_node)
        print()
