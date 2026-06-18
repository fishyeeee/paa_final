from collections import deque
from typing import List, Tuple, Dict, Any


def reconstruct_path(parent: Dict[Tuple[int, int], Tuple[int, int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    return path


def bfs(maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Dict[str, Any]:
    """
    Breadth-First Search for shortest path in an unweighted grid graph.
    
    Time Complexity: O(V + E) where V is number of cells and E is number of edges.
                     In a grid, E <= 4V, so it simplifies to O(V).
    Space Complexity: O(V) for the queue, visited set, and parent dictionary.
                      At worst, it stores all walkable cells.
    """

    rows = len(maze)
    cols = len(maze[0])

    queue = deque([start])
    visited = {start}
    parent = {}

    explored_nodes = 0
    max_frontier_size = 1

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while queue:
        current = queue.popleft()
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
                neighbor not in visited
            ):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

        max_frontier_size = max(max_frontier_size, len(queue))

    return {
        "path": None,
        "path_length": None,
        "explored_nodes": explored_nodes,
        "max_frontier_size": max_frontier_size
    }