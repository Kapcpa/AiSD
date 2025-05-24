import math
import sys
from collections import defaultdict, deque


sys.setrecursionlimit(2**20)


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
        in_degree = [0] * self.nodes
        for u in range(self.nodes):
            for v in self.adjacent[u]:
                in_degree[v] += 1

        queue = deque([u for u in range(self.nodes) if in_degree[u] == 0])
        ordered = []

        while queue:
            u = queue.popleft()
            ordered.append(u)
            for v in self.adjacent[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(ordered) != self.nodes:
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
        in_degree = [0] * self.nodes
        adjacency = defaultdict(list)

        for u, v in self.edges:
            adjacency[u].append(v)
            in_degree[v] += 1

        queue = deque([u for u in range(self.nodes) if in_degree[u] == 0])
        ordered = []

        while queue:
            u = queue.popleft()
            ordered.append(u)
            for v in adjacency[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(ordered) != self.nodes:
            raise ValueError("Graph has a cycle")
        print(f"Topological order using Kahn Algorithm: {ordered}")

    def topological_sort_tarjan(self):
        adjacency = defaultdict(list)
        for u, v in self.edges:
            adjacency[u].append(v)

        visited = [0] * self.nodes  # 0: unvisited, 1: visiting, 2: visited
        ordered = []

        def visit(n):
            if visited[n] == 1:
                raise ValueError("Graph has a cycle")
            if visited[n] == 2:
                return
            visited[n] = 1
            for m in adjacency[n]:
                visit(m)
            visited[n] = 2
            ordered.append(n)

        for n in range(self.nodes):
            if visited[n] == 0:
                visit(n)
        
        print(f"Topological order using Tarjan Algorithm: {list(reversed(ordered))}")


class MatrixGraph(Graph):
    def __init__(self, nodes: int):
        self.nodes = nodes
        self.matrix = [[0] * nodes for _ in range(nodes)]

    def add_edge(self, u: int, v: int):
        self.matrix[u][v] = 1

    def print(self):
        print("Adjacency Matrix:")
        print("    | " + " ".join(str(i) for i in range(self.nodes)))
        print(" ---+" + "-" * (3 * self.nodes - 4))
        for i in range(self.nodes):
            label = f"{i:>3} | "
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
        in_degree = [0] * self.nodes
        for u in range(self.nodes):
            for v in range(self.nodes):
                if self.matrix[u][v]:
                    in_degree[v] += 1

        queue = deque([u for u in range(self.nodes) if in_degree[u] == 0])
        ordered = []

        while queue:
            u = queue.popleft()
            ordered.append(u)
            for v in range(self.nodes):
                if self.matrix[u][v]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

        if len(ordered) != self.nodes:
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


def export_tikz(graph: AdjacencyListGraph | EdgeTableGraph | MatrixGraph, radius: int = 3):
    nodes = set()
    edges = []
    if type(graph) is AdjacencyListGraph:
        for u in range(graph.nodes):
            nodes.add(u)
            for v in graph.adjacent[u]:
                nodes.add(v)
                edges.append((u, v))
    elif type(graph) is EdgeTableGraph:
        for u, v in graph.edges:
            nodes.add(u)
            nodes.add(v)
            edges.append((u, v))
    elif type(graph) is MatrixGraph:
        for u in range(graph.nodes):
            nodes.add(u)
            for v in range(graph.nodes):
                if graph.matrix[u][v]:
                    nodes.add(v)
                    edges.append((u, v))
    else:
        return
    
    nodes = sorted(nodes)
    node_pos = {}
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / graph.nodes
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        node_pos[node] = (x, y)       

    file = open("graph.txt", "w")

    file.write("\\begin{tikzpicture}[->,>=stealth,thick] \n") 
    file.write("  % Nodes \n")
    for node in nodes:
        x, y = node_pos[node]
        file.write(f"  \\node[circle,draw] ({node}) at ({x:.2f},{y:.2f}) {{{node}}}; \n")

    file.write("\n  % Edges \n")
    for u, v in edges:
        file.write(f"  \\draw[->] ({u}) -- ({v}); \n")
    file.write("\\end{tikzpicture}")
