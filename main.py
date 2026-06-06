import time

from maze.generator import generate_maze
from algorithms.bfs import bfs
from algorithms.astar import astar
from visualization.visualize import show_maze


def main():
    size = 50
    obstacle_prob = 0.25
    seed = 42

    start = (0, 0)
    goal = (size - 1, size - 1)

    maze = generate_maze(
        rows=size,
        cols=size,
        obstacle_prob=obstacle_prob,
        seed=seed
    )

    bfs_start_time = time.perf_counter()
    bfs_result = bfs(maze, start, goal)
    bfs_runtime = (time.perf_counter() - bfs_start_time) * 1000

    astar_start_time = time.perf_counter()
    astar_result = astar(maze, start, goal)
    astar_runtime = (time.perf_counter() - astar_start_time) * 1000

    print("\n=== Dungeon Pathfinder Demo ===")
    print(f"Maze size: {size}x{size}")
    print(f"Obstacle probability: {obstacle_prob}")
    print(f"Start: {start}")
    print(f"Goal: {goal}")

    print("\n=== BFS Result ===")
    print(f"Runtime: {bfs_runtime:.4f} ms")
    print(f"Path length: {bfs_result['path_length']}")
    print(f"Explored nodes: {bfs_result['explored_nodes']}")
    print(f"Max frontier size: {bfs_result['max_frontier_size']}")

    print("\n=== A* Result ===")
    print(f"Runtime: {astar_runtime:.4f} ms")
    print(f"Path length: {astar_result['path_length']}")
    print(f"Explored nodes: {astar_result['explored_nodes']}")
    print(f"Max frontier size: {astar_result['max_frontier_size']}")

    print("\n=== Cross-check ===")

    if bfs_result["path_length"] == astar_result["path_length"]:
        print("PASS: BFS and A* found the same shortest path length.")
    else:
        print("WARNING: Path lengths are different.")

    show_maze(
        maze=maze,
        path=astar_result["path"],
        start=start,
        goal=goal,
        title="Dungeon Pathfinder - A* Shortest Path"
    )


if __name__ == "__main__":
    main()