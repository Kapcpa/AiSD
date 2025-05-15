import random
from graph_implementation import *


graph_types: dict[str, type[Graph]] = {
    "list": AdjacencyListGraph,
    "table": EdgeTableGraph,
    "matrix": MatrixGraph
}


def graph_generated() -> Graph:
    try:
        nodes = int(input("nodes> "))

        saturation = int(input("saturation> "))
        if saturation < 0 or saturation > 100:
            raise ValueError("Saturation must be between 0 and 100")
    except ValueError:
        raise ValueError("Provided input wasn't a number")

    graph_type = input("type> ")
    while graph_type not in graph_types:
        print("ERROR: Please pick one of the following types: list table matrix")
        graph_type = input("type> ")
    
    edges = [(u, v) for u in range(nodes) for v in range(u + 1, nodes)]
    edge_count = (saturation * len(edges)) // 100
    selected_edges = random.sample(edges, edge_count)

    graph = graph_types[graph_type](nodes)
    for u, v in selected_edges:
        graph.add_edge(u, v)

    return graph


def graph_provided() -> Graph:
    try:
        nodes = int(input("nodes> "))
    except ValueError:
        raise ValueError("Provided input wasn't a number")

    adjacent = []
    for i in range(nodes):
        try:
            adjacent_nodes = [int(node) for node in input(f"{i}> ").strip().split()]
        except ValueError:
            raise ValueError("Provided input wasn't a number")

        if any(node < 0 or node >= nodes for node in adjacent_nodes):
            raise ValueError("Invalid nodes were provided")
        adjacent.append(adjacent_nodes)
    
    graph_type = input("type> ")
    while graph_type not in graph_types:
        print("ERROR: Please pick one of the following types: list table matrix")
        graph_type = input("type> ")
    
    graph = graph_types[graph_type](nodes)
    for i in range(nodes):
        for node in adjacent[i]:
            graph.add_edge(i, node)

    return graph
