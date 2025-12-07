import heapq
from mazes import maze1, start1, goal1, maze2, start2, goal2, maze3, start3, goal3

# Manhattan distance heuristic
def manhattan(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

# Check if a move is valid
def valid(graph, node, row, col):
    r, c = node
    return 0 <= r < row and 0 <= c < col and graph[r][c] != "#"

# Possible moves
def moves(node):
    r, c = node
    return [
        ("R", (r, c + 1)),
        ("L", (r, c - 1)),
        ("U", (r - 1, c)),
        ("D", (r + 1, c))
    ]

# A* maze solver
def mazeSolver(graph, start, end):
    rows = len(graph)
    cols = len(graph[0])
    parent = {start: None}
    distance = {start: 0}
    directions = {start: None}

    minHeap = []
    heapq.heappush(minHeap, (manhattan(start, end), 0, start))

    while minHeap:
        heuristics, cost, node = heapq.heappop(minHeap)

        if node == end:
            path = []
            while node != start:
                path.append(directions[node])
                node = parent[node]
            path.reverse()
            return path, cost

        for moveDir, vNode in moves(node):
            if valid(graph, vNode, rows, cols):
                totalCost = cost + 1
                node_goodness = manhattan(vNode, end)
                if vNode not in distance or distance[vNode] > totalCost:
                    heapq.heappush(minHeap, (node_goodness + totalCost, totalCost, vNode))
                    directions[vNode] = moveDir
                    parent[vNode] = node
                    distance[vNode] = totalCost

    return None, None

# Solve all mazes
mazes = [
    (maze1, start1, goal1, "Maze1"),
    (maze2, start2, goal2, "Maze2"),
    (maze3, start3, goal3, "Maze3")
]

for graph, start, goal, name in mazes:
    path, steps = mazeSolver(graph, start, goal)
    if path:
        print(f"{name} Directions: {' → '.join(path)}")
        print(f"{name} Total Steps: {steps}\n")
    else:
        print(f"{name}: No path found.\n")
