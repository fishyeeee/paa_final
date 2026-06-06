import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def show_maze(maze, path=None, start=None, goal=None, title="Dungeon Pathfinder"):
    """
    Visualization values:
    0 = open cell
    1 = wall
    2 = path
    3 = start
    4 = goal
    """

    display = [row[:] for row in maze]

    if path:
        for r, c in path:
            display[r][c] = 2

    if start:
        display[start[0]][start[1]] = 3

    if goal:
        display[goal[0]][goal[1]] = 4

    cmap = ListedColormap([
        "white",      # open cell
        "black",      # wall
        "deepskyblue",# path
        "lime",       # start
        "red"         # goal
    ])

    plt.figure(figsize=(8, 8))
    plt.imshow(display, cmap=cmap)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()