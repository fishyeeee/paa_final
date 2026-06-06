import random


def generate_maze(rows, cols, obstacle_prob=0.25, seed=None):
    """
    Generate a random dungeon maze.

    0 = walkable cell
    1 = obstacle/wall

    This generator guarantees that at least one path exists
    from start (0, 0) to goal (rows - 1, cols - 1).
    """

    if seed is not None:
        random.seed(seed)

    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    guaranteed_path = set()

    r, c = 0, 0
    guaranteed_path.add((r, c))

    while r < rows - 1 or c < cols - 1:
        if r == rows - 1:
            c += 1
        elif c == cols - 1:
            r += 1
        else:
            if random.random() < 0.5:
                r += 1
            else:
                c += 1

        guaranteed_path.add((r, c))

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in guaranteed_path:
                if random.random() < obstacle_prob:
                    maze[row][col] = 1

    maze[0][0] = 0
    maze[rows - 1][cols - 1] = 0

    return maze