import sys
from sorting_algorithms import *


algorithms = {
    0: {"name": "insertion sort", "algorithm": insertion_sort},
    1: {"name": "selection sort", "algorithm": selection_sort},
    2: {"name": "heap sort", "algorithm": heap_sort},
    3: {"name": "quick sort with far-left pivot", "algorithm": quick_sort_left},
    4: {"name": "quick sort with random pivot", "algorithm": quick_sort_left},
}


def sort_using_algorithm(data, algorithm_id: int):
    algorithms[algorithm_id]["algorithm"](data)


def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_id = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input]
    except EOFError:
        print("Error reading input.")

    sort_using_algorithm(data, algorithm_id)

    # Print the sorted data
    print(f"Sorted data: {data[0:10]} using {algorithms[algorithm_id]["name"]} algorithm")


if __name__ == "__main__":
    main()
