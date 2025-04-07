import sys
from sorting_algorithms import *


sys.setrecursionlimit(2**20)


algorithms = {
    1: {"name": "insertion sort", "algorithm": insertion_sort},
    2: {"name": "shell sort", "algorithm": shell_sort},
    3: {"name": "selection sort", "algorithm": selection_sort},
    4: {"name": "heap sort", "algorithm": heap_sort},
    5: {"name": "quick sort with far-left pivot", "algorithm": quick_sort_left},
    6: {"name": "quick sort with random pivot", "algorithm": quick_sort_rand},
}


def log_data(data: list[int], max_display: int = 8):
    if len(data) > 2 * max_display:
        return f"[{', '.join(map(str, data[:max_display]))}, ..., {', '.join(map(str, data[-max_display:]))}]"
    return str(data)


def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        print("<algorithm_number> <algorithm_name>")
        for i in algorithms:
            print(f"{i} - {algorithms[i]["name"]}")
        sys.exit(1)

    algorithm_id = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input]
    except EOFError:
        print("Error reading input.")


    # Print the unsorted data
    # print(f"Unsorted data: {log_data(data)}")

    # Executes the sorting function that corresponds to the algorithm_id
    algorithms[algorithm_id]["algorithm"](data)

    # Print the sorted data
    print(f"Sorted data: {log_data(data)} using {algorithms[algorithm_id]["name"]} algorithm")


if __name__ == "__main__":
    main()
