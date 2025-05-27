from adjacency_graph import AdjacencyListGraph
import random


def generate_hamiltonian_graph() -> AdjacencyListGraph:
    n = int(input("nodes> "))
    saturation = int(input("saturation> "))

    graph = AdjacencyListGraph(n)   

    nodes = list(range(n))
    random.shuffle(nodes)
    for i in range(n):
        graph.add_edge(nodes[i], nodes[(i + 1) % n])

    total_edges = (n * (n - 1)) // 2
    target_edges = int((saturation / 100) * total_edges)

    while graph.edge_count < target_edges:
        u, v = random.sample(range(n), 2)
        if not graph.has_edge(u, v):
            graph.add_edge(u, v)

    return graph


def generate_non_hamiltonian_graph() -> AdjacencyListGraph:
    n = int(input("nodes> "))

    graph = AdjacencyListGraph(n)   
    
    generate_hamiltonian_graph(graph, n, 50)
    for i in range(n - 1):
        graph.remove_edge(i, n - 1)
    
    return graph
