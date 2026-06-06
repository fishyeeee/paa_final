# Dungeon Escape: BFS vs A* Maze Pathfinder

This project is a Python implementation of maze pathfinding using **Breadth-First Search (BFS)** and **A* Search**.

The maze is represented as a grid graph, where each walkable cell is a node and movement between adjacent cells is an edge. The program finds the shortest path from the start cell to the goal cell, compares both algorithms, and generates benchmark results.

## Features

* Random solvable maze generation
* BFS pathfinding
* A* pathfinding with Manhattan distance heuristic
* Maze visualization
* Runtime benchmark
* CSV and plot output

## Requirements

Install the required library:

```bash
pip install matplotlib
```

or:

```bash
pip install -r requirements.txt
```

## How to Run Demo

Run:

```bash
python main.py
```

This will generate a maze, run BFS and A*, compare their path lengths, and show the A* path visualization.

## How to Run Benchmark

Run:

```bash
python run_benchmark.py
```

This will test multiple maze sizes and generate the results in the `results/` folder:

```text
results/benchmark_results.csv
results/runtime_comparison.png
results/explored_nodes_comparison.png
```

## Project Structure

```text
dungeon_pathfinder/
├── algorithms/
│   ├── bfs.py
│   └── astar.py
├── maze/
│   └── generator.py
├── visualization/
│   └── visualize.py
├── results/
├── main.py
├── run_benchmark.py
├── requirements.txt
└── README.md
```

## Algorithms

* **BFS** is used as the baseline algorithm.
* **A*** is used as the informed search algorithm with Manhattan distance heuristic.

Both algorithms are implemented manually without using external graph libraries.
