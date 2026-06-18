import heapq
from itertools import count
from typing import List, Tuple, Dict, Any
from algorithms.bfs import reconstruct_path


def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Dict[str, Any]:
    """
    A* Search using Manhattan distance heuristic.
    
    Time Complexity: O(E log V) in the worst case using a Binary Heap (Priority Queue).
                     In a grid where E <= 4V, this is O(V log V).
    Space Complexity: O(V) for the priority queue, closed_set, g_score, and parent dict.
    """

    rows = len(maze)
    cols = len(maze[0])

    priority_queue = []
    counter = count()

    g_score = {start: 0}
    parent = {}
    closed_set = set()

    start_h = manhattan_distance(start, goal)

    heapq.heappush(
        priority_queue,
        (start_h, start_h, next(counter), start)
    )

    explored_nodes = 0
    max_frontier_size = 1

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while priority_queue:
        _, _, _, current = heapq.heappop(priority_queue)

        if current in closed_set:
            continue

        closed_set.add(current)
        explored_nodes += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)

            return {
                "path": path,
                "path_length": len(path) - 1,
                "explored_nodes": explored_nodes,
                "max_frontier_size": max_frontier_size
            }

        r, c = current

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            neighbor = (nr, nc)

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                maze[nr][nc] == 0 and
                neighbor not in closed_set
            ):
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g

                    h = manhattan_distance(neighbor, goal)
                    f = tentative_g + h

                    heapq.heappush(
                        priority_queue,
                        (f, h, next(counter), neighbor)
                    )

        max_frontier_size = max(max_frontier_size, len(priority_queue))

    return {
        "path": None,
        "path_length": None,
        "explored_nodes": explored_nodes,
        "max_frontier_size": max_frontier_size
    }