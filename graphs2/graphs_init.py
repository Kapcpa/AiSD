from adjacency_graph import AdjacencyListGraph
import random


def get_int(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        print("ERROR: Given value wasn't a number.")
        exit(-1)


def generate_graph(hamilton: bool) -> AdjacencyListGraph:
    n = get_int("nodes> ")
    if hamilton:
        saturation = get_int("saturation> ")
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

    
    attempts = 0
    max_attempts = n * n * 10

    # probujemy stworzyc graf z cyklem eulera, wiec jesli sa wierzcholki z nieparzysta 
    # iloscia to najpierw dodaje do nich krawedz a nastepnie losowo
    while graph.edges < target_edges and attempts < max_attempts:
        odd_degree_nodes = [u for u in range(n) if len(graph.adj[u]) % 2 != 0]
        if len(odd_degree_nodes) >= 2:
            u, v = random.sample(odd_degree_nodes, 2)
            if not graph.find(u, v):
                graph.add_edge(u, v)
                attempts = 0
                continue

        u, v = random.sample(range(n), 2)
        if not graph.find(u, v):
            graph.add_edge(u, v)

        attempts += 1

    return graph


def generate_non_hamiltonian_graph(n: int) -> AdjacencyListGraph:    
    graph = generate_hamiltonian_graph(n, 50)
    for i in range(n - 1):
        graph.remove_edge(i, n - 1)
    
    return graph
