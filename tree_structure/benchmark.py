import sys
import time
import numpy
import os
import csv
from trees import *
from commands import *


# USES NANOSECONDS 1 ns = 1*10^-9 s
sys.setrecursionlimit(2**18)


def benchmark_build_avl(data: list[int]) -> float:
    start_time = time.perf_counter_ns()
    build_avl(data)
    return time.perf_counter_ns() - start_time


def benchmark_build_bst(data: list[int]) -> float:
    start_time = time.perf_counter_ns()
    build_bst(data)
    return time.perf_counter_ns() - start_time


def benchmark_avl_min_max(data: list[int]) -> float:
    tree = build_avl(data)
    start_time = time.perf_counter_ns()
    command_min_max(tree)
    return time.perf_counter_ns() - start_time


def benchmark_bst_min_max(data: list[int]) -> float:
    tree = build_bst(data)
    start_time = time.perf_counter_ns()
    command_min_max(tree)
    return time.perf_counter_ns() - start_time


def benchmark_avl_print_in_order(data: list[int]) -> float:
    tree = build_avl(data)
    start_time = time.perf_counter_ns()
    traverse_tree(tree, IN_ORDER)
    return time.perf_counter_ns() - start_time


def benchmark_bst_print_in_order(data: list[int]) -> float:
    tree = build_bst(data)
    start_time = time.perf_counter_ns()
    traverse_tree(tree, IN_ORDER)
    return time.perf_counter_ns() - start_time


def benchmark_rebalance(data: list[int]) -> float:
    tree = build_bst(data)
    start_time = time.perf_counter_ns()
    command_rebalance(tree)
    return time.perf_counter_ns() - start_time


def benchmark(array_type: str):
    sizes = [2**x for x in range(2, 18)]
    folder = f"benchmark_results/{array_type}"
    os.makedirs(folder, exist_ok=True)

    # Prepare CSV writers for each category
    build_file = open(f"{folder}/build.csv", "w", newline="")
    minmax_file = open(f"{folder}/min_max.csv", "w", newline="")
    inorder_file = open(f"{folder}/print_in_order.csv", "w", newline="")
    rebalance_file = open(f"{folder}/rebalance.csv", "w", newline="")

    build_writer = csv.writer(build_file)
    minmax_writer = csv.writer(minmax_file)
    inorder_writer = csv.writer(inorder_file)
    rebalance_writer = csv.writer(rebalance_file)

    # Write headers
    for writer in [build_writer, minmax_writer, inorder_writer, rebalance_writer]:
        writer.writerow(["Algorithm", "InputSize", "Time"])

    for size in sizes:
        data = numpy.loadtxt(f'benchmark/{array_type}_{size:08d}.txt', dtype=int)
        data_list = data.tolist()

        # Build
        build_writer.writerow(["build_avl", size, benchmark_build_avl(data_list)])
        build_writer.writerow(["build_bst", size, benchmark_build_bst(data_list)])

        # Min/max
        minmax_writer.writerow(["avl_min_max", size, benchmark_avl_min_max(data_list)])
        minmax_writer.writerow(["bst_min_max", size, benchmark_bst_min_max(data_list)])

        # In-order
        inorder_writer.writerow(["avl_print_in_order", size, benchmark_avl_print_in_order(data_list)])
        inorder_writer.writerow(["bst_print_in_order", size, benchmark_bst_print_in_order(data_list)])

        # Rebalance 
        rebalance_writer.writerow(["rebalance", size, benchmark_rebalance(data_list)])

    build_file.close()
    minmax_file.close()
    inorder_file.close()
    rebalance_file.close()


benchmark("random_array")
