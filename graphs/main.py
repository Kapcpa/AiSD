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
        action = input("action> ").strip().upper()
        if action == "PRINT":
            graph.print()
        elif action == "FIND":
            graph.find()
        elif action == "BFS":
            graph.bfs()
        elif action == "DFS":
            graph.dfs()
        elif action == "KAHN":
            graph.topological_sort_kahn()
        elif action == "TARJAN":
            graph.topological_sort_tarjan()
        elif action == "HELP":
            print("Help - Shows this message")
            print("Print - Prints the graph in its representation")
            print("Find - Checks if an edge exists from start node to end node")
            print("BFS - Prints the graph nodes in a Breadth First Search order")
            print("DFS - Prints the graph nodes in a Depth First Search order")
            print("Kahn - Prints topologically sorted graph using Kahn's Algorithm")
            print("Tarjan - Prints topologically sorted graph using Tarjan's Algorithm")
            print("Exit - Exits the program")
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
