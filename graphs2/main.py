import sys
from graphs_init import generate_graph
from adjacency_graph import *


graph_init_arg = {"--hamilton": True,"--non-hamilton": False}


def main():
    # Command-line arguments: python3 main.py <graph-type>
    if len(sys.argv) != 2 or sys.argv[1] not in graph_init_arg:
        print("Usage: python3 main.py <graph-type>")
        print("<graph-type> '--hamilton' or '--non-hamilton'")
        sys.exit(1)
    
    graph = generate_graph(hamilton=graph_init_arg[sys.argv[1]])

    while True:
        action = input("action> ").strip().upper()
        if action == "HELP":
            print("Help - Shows this message")
            print("Print - Prints a graph in correct representation")
            print("Hamilton - Prints Hamilton's cycle (if exists)")
            print("Euler - Prints Eulers's cycle (if exists)")
            print("Exit - exits the program")
            print("Help - Shows this message")
        elif action == "PRINT":
            graph.print()
        elif action == "HAMILTON":
            cycle = hamilton_cycle(graph)
            print(f"Hamilton's Cycle: {cycle}") if cycle is not None else print("No Hamilton's Cycle found")
        elif action == "EULER":
            cycle = euler_cycle(graph)
            print(f"Euler's Cycle: {cycle}") if cycle is not None else print("No Euler's Cycle found")
        elif action == "EXIT":
            return
        else:
            print("ERROR: Invalid action. Type 'Help' to see possible actions.")
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
