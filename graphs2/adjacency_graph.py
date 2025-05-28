class AdjacencyListGraph:
    def __init__(self, n: int):
        self.n = n
        self.adj = {i: set() for i in range(n)}

    @property
    def edges(self) -> int:
        return sum(len(neighbors) for neighbors in self.adj.values()) // 2

    def add_edge(self, u: int, v: int):
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self, u: int, v: int):
        self.adj[u].discard(v)
        self.adj[v].discard(u)

    def find(self, u: int, v: int):
        return v in self.adj[u]

    def print(self):
        for node, neighbors in self.adj.items():
            print(f"{node}: {sorted(neighbors)}")


def hamilton_cycle(graph: AdjacencyListGraph) -> list[int] | None:
    path = [0]
    visited = [False] * graph.n
    visited[0] = True

    def backtrack(pos):
        if len(path) == graph.n:
            if path[0] in graph.adj[path[-1]]:
                path.append(path[0])
                return True
            return False

        for neighbor in graph.adj[path[-1]]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)

                if backtrack(pos + 1):
                    return True
                
                visited[neighbor] = False
                path.pop()

        return False

    if backtrack(1):
        return path
    
    return None


def euler_cycle(graph: AdjacencyListGraph) -> list[int] | None:
    for neighbors in graph.adj.values():
        if len(neighbors) % 2 != 0:
            return None
        
    temp_adj = {u: set(vs) for u, vs in graph.adj.items()}
    stack = []
    cycle = []

    current = next(iter(temp_adj))
    stack.append(current)

    while stack:
        if temp_adj[current]:
            stack.append(current)
            neighbor = temp_adj[current].pop()
            temp_adj[neighbor].remove(current)
            current = neighbor
            continue

        cycle.append(current)
        current = stack.pop()

    if len(cycle) == graph.edges + 1:
        return cycle
   
    return None
