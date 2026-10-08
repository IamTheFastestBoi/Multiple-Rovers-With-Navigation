So this is my rover navigation system (V.3) . I upgraded the V.2 . I added more rovers in the simulation . And the description:

A Python-based multi-agent pathfinding and swarm simulation where autonomous robotic rovers navigate through complex, constrained grid environments to reach target destinations using a custom Breadth-First Search (BFS) memory architecture and intelligent deadlock resolution.

---

## 🚀 Key Features

- **Object-Oriented Architecture:** Modular design utilizing custom rover classes with state tracking, path memory, and route optimization.
- **Custom BFS Pathfinding:** A memory-based search algorithm that explores the grid, evaluates valid passages, and dynamically calculates the shortest available path to targets.
- **Autonomous Backtracking (Deadlock Resolution):** If an agent runs out of valid paths or faces a blockage, it automatically triggers a `backtrack()` sequence, clears its history, and explores alternative routes without hardcoded rules.
- **Procedural Maze Generation:** Generates robust, maze-like grid layouts designed to test multi-agent coordination and navigation efficiency.

- `⬜` : **Open Path** (Passable terrain)
- `⬛` : **Wall / Obstacle** (Impassable barrier)
- `🎯` : **Target / Destination** (Objective zone)
- `🤖` : **Active Rover** (Autonomous agent)

- ## 🛠️ Logic & Workflow

1. **Exploration (`memory`):** Each rover inspects its surrounding grid cells using directional vectors `(-1, 0), (1, 0), (0, -1), (0, 1)`, filtering out obstacles and previously visited invalid nodes.
2. **Decision Making (`move`):** Valid routes leading to the target are evaluated, and the shortest path is selected. 
3. **Collision & Deadlock Handling (`backtrack`):** When movement is obstructed, agents retreat step-by-step through their previous positions, resetting their local route memory to dynamically bypass congestion.
4. **Target Completion:** Once a rover successfully reaches a target destination, it exits the active loop and restores the target marker on the map to ensure clear pathways for trailing agents.
