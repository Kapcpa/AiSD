from adjacency_graph import AdjacencyListGraph
import random


def generate_graph(hamilton: bool) -> AdjacencyListGraph:
    n = int(input("nodes> "))
    if hamilton:
        saturation = int(input("saturation> "))
        return generate_hamiltonian_graph(n, saturation)
    return generate_non_hamiltonian_graph(n)


def generate_hamiltonian_graph(n: int, saturation: int) -> AdjacencyListGraph:
    graph = AdjacencyListGraph(n)   

    nodes = list(range(n))
    random.shuffle(nodes)
    for i in range(n):
        graph.add_edge(nodes[i], nodes[(i + 1) % n])

    total_edges = (n * (n - 1)) // 2
    target_edges = int((saturation / 100) * total_edges)

    while graph.edges < target_edges:
        u, v = random.sample(range(n), 2)
        if not graph.find(u, v):
            graph.add_edge(u, v)

    return graph


def generate_non_hamiltonian_graph(n: int) -> AdjacencyListGraph:    
    graph = generate_hamiltonian_graph(n, 50)
    for i in range(n - 1):
        graph.remove_edge(i, n - 1)
    
    return graph
