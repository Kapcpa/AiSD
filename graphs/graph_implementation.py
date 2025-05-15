class Graph:
    def __init__(self, nodes: int): pass

    def add_edge(self, u: int, v: int): pass

    def print(self): pass

    def find(self): pass

    @property
    def start_nodes(self) -> list[int]: pass

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
        try:
            u = int(input("from> "))
            v = int(input("to> "))
        except ValueError:
            raise ValueError("Provided input wasn't a number")
        print(f"Edge {(u, v)} {"does" if v in self.adjacent[u] else "does not"} exist in the graph")

    @property
    def start_nodes(self) -> list[int]:
        start_nodes = []
        for node in range(self.nodes):
            if all([node not in edges for edges in self.adjacent]):
                start_nodes.append(node)
        return start_nodes

    def bfs(self):
        start = self.start_nodes[0]

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
        dfs_recursive(self.start_nodes[0])
        print()
    
    def topological_sort_kahn(self):
        queue = self.start_nodes.copy()
        ordered = []
        edges = [(u, v) for u in range(self.nodes) for v in self.adjacent[u]]

        while queue:
            node = queue.pop(0)
            ordered.append(node)
            for v in self.adjacent[node]:
                edges.remove((node, v))
                if not any((u, v) in edges for u in range(self.nodes)):
                    queue.append(v)
        
        if edges:
            raise ValueError("Graph has a cycle")
        print(f"Topological order using Kahn Algorithm: {ordered}")

    def topological_sort_tarjan(self):
        permanent = set()
        temporary = set()
        ordered = []

        def visit(n):
            if n in permanent:
                return
            if n in temporary:
                raise ValueError("Graph has a cycle")
            
            temporary.add(n)
            for m in self.adjacent[n]:
                visit(m)
            temporary.remove(n)
            permanent.add(n)
            ordered.append(n)

        for n in range(self.nodes):
            if n not in permanent:
                visit(n)

        ordered.reverse()
        print(f"Topological order using Tarjan Algorithm: {ordered}")
        

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
        try:
            u = int(input("from> "))
            v = int(input("to> "))
        except ValueError:
            raise ValueError("Provided input wasn't a number")
        print(f"Edge {(u, v)} {'does' if (u, v) in self.edges else 'does not'} exist in the graph")

    @property
    def start_nodes(self) -> list[int]:
        all_nodes = set(range(self.nodes))
        destinations = {v for _, v in self.edges}
        sources = all_nodes - destinations
        return sorted(sources)

    def bfs(self):
        start = self.start_nodes[0]
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
        dfs_recursive(self.start_nodes[0])
        print()

    def topological_sort_kahn(self):
        queue = self.start_nodes.copy()
        ordered = []
        edges = self.edges.copy()

        while queue:
            node = queue.pop(0)
            ordered.append(node)
            for _, v in [e for e in edges if e[0] == node]:
                edges.remove((node, v))
                if not any(u == other for u, other in edges if other == v):
                    queue.append(v)

        if edges:
            raise ValueError("Graph has a cycle")
        print(f"Topological order using Kahn Algorithm: {ordered}")

    def topological_sort_tarjan(self):
        permanent = set()
        temporary = set()
        ordered = []

        def visit(n):
            if n in permanent:
                return
            if n in temporary:
                raise ValueError("Graph has a cycle")
            temporary.add(n)
            for _, m in [e for e in self.edges if e[0] == n]:
                visit(m)
            temporary.remove(n)
            permanent.add(n)
            ordered.append(n)

        for n in range(self.nodes):
            if n not in permanent:
                visit(n)

        ordered.reverse()
        print(f"Topological order using Tarjan Algorithm: {ordered}")


class MatrixGraph(Graph):
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.matrix = [[0] * nodes for _ in range(nodes)]

    def add_edge(self, u: int, v: int):
        self.matrix[u][v] = 1

    def print(self):
        print("Adjacency Matrix:")
        print("    | " + " ".join(str(i + 1) for i in range(self.nodes)))
        print(" ---+" + "-" * (3 * self.nodes - 4))
        for i in range(self.nodes):
            label = f"{i + 1:>3} | "
            data = " ".join(str(value) for value in self.matrix[i])
            print(label + data)

    def find(self):
        try:
            u = int(input("from> "))
            v = int(input("to> "))
        except ValueError:
            raise ValueError("Provided input wasn't a number")

        print(f"Edge {(u, v)} {'does' if self.matrix[u][v] else 'does not'} exist in the graph")

    @property
    def start_nodes(self) -> list[int]:
        start_nodes = []
        for node in range(self.nodes):
            if all(self.matrix[other][node] == 0 for other in range(self.nodes)):
                start_nodes.append(node)
        return start_nodes

    def bfs(self):
        start = self.start_nodes[0]
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
        dfs_recursive(self.start_nodes[0])
        print()

    def topological_sort_kahn(self):
        queue = self.start_nodes.copy()
        ordered = []
        edges = [(u, v) for u in range(self.nodes) for v in range(self.nodes) if self.matrix[u][v]]

        while queue:
            node = queue.pop(0)
            ordered.append(node)
            for v in range(self.nodes):
                if self.matrix[node][v]:
                    edges.remove((node, v))
                    if not any((u, v) in edges for u in range(self.nodes)):
                        queue.append(v)

        if edges:
            raise ValueError("Graph has a cycle")
        print(f"Topological order using Kahn Algorithm: {ordered}")

    def topological_sort_tarjan(self):
        permanent = set()
        temporary = set()
        ordered = []

        def visit(n):
            if n in permanent:
                return
            if n in temporary:
                raise ValueError("Graph has a cycle")
            temporary.add(n)
            for m in range(self.nodes):
                if self.matrix[n][m]:
                    visit(m)
            temporary.remove(n)
            permanent.add(n)
            ordered.append(n)

        for n in range(self.nodes):
            if n not in permanent:
                visit(n)

        ordered.reverse()
        print(f"Topological order using Tarjan Algorithm: {ordered}")
