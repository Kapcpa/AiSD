import sys
from graphs_init import *
from adjacency_graph import hamilton_cycle, euler_cycle


graph_init = {
    "--hamilton": generate_hamiltonian_graph,
    "--non-hamilton": generate_non_hamiltonian_graph
}


def main():
    # Command-line arguments: python3 main.py <graph-type>
    if len(sys.argv) != 2 or sys.argv[1] not in graph_init:
        print("Usage: python3 main.py <graph-type>")
        print("<graph-type> '--hamilton' or '--non-hamilton'")
        sys.exit(1)
    
    graph = graph_init[sys.argv[1]]()

    while True:
        action = input("action> ").strip().upper()
        if action == "HELP":
            print("Help - Shows this message")
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
