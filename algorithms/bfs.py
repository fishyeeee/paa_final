from collections import deque


def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    return path


def bfs(maze, start, goal):
    """
    Breadth-First Search for shortest path in an unweighted grid graph.
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