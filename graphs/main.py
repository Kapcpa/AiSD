import sys
from graph_init import *


graph_init = {
    "--generate": graph_generated,
    "--user-provided": graph_provided
}

def main():
    # Command-line arguments: python3 main.py --graphs <input-type>
    if len(sys.argv) != 3 or sys.argv[1] != "--graphs" or sys.argv[2] not in graph_init:
        print("Usage: python3 main.py --graphs <input-type>")
        print("<input-type> '--generate' or '--user-provided'")
        sys.exit(1)
    
    graph = graph_init[sys.argv[2]]()

    while True:
        action = input("action> ").strip()
        if action == "Print":
            graph.print()
        elif action == "Find":
            graph.find()
        elif action == "BFS":
            graph.bfs()
        elif action == "DFS":
            graph.dfs()
        elif action == "Kahn":
            graph.topological_sort_kahn()
        elif action == "Tarjan":
            graph.topological_sort_tarjan()
        elif action == "Exit":
            return
        else:
            print("ERROR: Invalid action. Type 'Help' to see possible actions.")
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
