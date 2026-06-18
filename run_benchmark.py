import csv
import time
import statistics
import matplotlib.pyplot as plt

from maze.generator import generate_maze
from algorithms.bfs import bfs
from algorithms.astar import astar


def average_runtime(algorithm, maze, start, goal, repeats=3):
    runtimes = []
    final_result = None

    for _ in range(repeats):
        start_time = time.perf_counter()
        result = algorithm(maze, start, goal)
        runtime_ms = (time.perf_counter() - start_time) * 1000

        runtimes.append(runtime_ms)
        final_result = result

    return statistics.mean(runtimes), final_result


def run_benchmark():
    sizes = [32, 64, 128, 256, 512]
    obstacle_prob = 0.25
    repeats = 3
    base_seed = 42

    rows = []

    print("Running benchmark...")
    print("This may take a while for 256x256 and 512x512.")

    for size in sizes:
        print(f"\nTesting size {size}x{size}...")

        start = (0, 0)
        goal = (size - 1, size - 1)
        current_seed = base_seed + size

        maze = generate_maze(
            rows=size,
            cols=size,
            obstacle_prob=obstacle_prob,
            seed=current_seed
        )

        bfs_time, bfs_result = average_runtime(
            bfs,
            maze,
            start,
            goal,
            repeats=repeats
        )

        astar_time, astar_result = average_runtime(
            astar,
            maze,
            start,
            goal,
            repeats=repeats
        )

        same_path_length = (
            bfs_result["path_length"] == astar_result["path_length"] if bfs_result["path"] and astar_result["path"] else False # type: ignore
        )

        row = {
            "grid_size": f"{size}x{size}",
            "nodes": size * size,
            "seed": current_seed,
            "bfs_runtime_ms": round(bfs_time, 4),
            "astar_runtime_ms": round(astar_time, 4),
            "bfs_explored_nodes": bfs_result["explored_nodes"], # type: ignore
            "astar_explored_nodes": astar_result["explored_nodes"], # type: ignore
            "bfs_path_length": bfs_result["path_length"], # type: ignore
            "astar_path_length": astar_result["path_length"], # type: ignore
            "same_path_length": same_path_length
        }

        rows.append(row)

        print(row)

    csv_path = "results/benchmark_results.csv"

    with open(csv_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=rows[0].keys()
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nBenchmark CSV saved to {csv_path}")

    plot_runtime(rows)
    plot_explored_nodes(rows)


def plot_runtime(rows):
    nodes = [row["nodes"] for row in rows]
    bfs_times = [row["bfs_runtime_ms"] for row in rows]
    astar_times = [row["astar_runtime_ms"] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.plot(nodes, bfs_times, marker="o", label="BFS")
    plt.plot(nodes, astar_times, marker="o", label="A*")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Runtime (ms)")
    plt.title("Runtime Comparison: BFS vs A*")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/runtime_comparison.png")
    plt.show()


def plot_explored_nodes(rows):
    nodes = [row["nodes"] for row in rows]
    bfs_explored = [row["bfs_explored_nodes"] for row in rows]
    astar_explored = [row["astar_explored_nodes"] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.plot(nodes, bfs_explored, marker="o", label="BFS")
    plt.plot(nodes, astar_explored, marker="o", label="A*")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Explored Nodes")
    plt.title("Explored Nodes Comparison: BFS vs A*")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/explored_nodes_comparison.png")
    plt.show()


if __name__ == "__main__":
    run_benchmark()