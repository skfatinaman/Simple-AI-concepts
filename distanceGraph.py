import math

coordinates = {
    "A": (0, 0),
    "B": (3, 4),
    "C": (6, 1),
    "D": (8, 6),
    "E": (10, 0),
    "F": (4, 8)
}

graph = {
    "A": {"B": 6, "C": 7},
    "B": {"A": 6, "D": 4, "F": 5},
    "C": {"A": 7, "D": 6, "E": 6},
    "D": {"B": 4, "C": 6, "F": 4},
    "E": {"C": 6},
    "F": {"B": 5, "D": 4}
}

def euclideanDistance(coordinateA, coordinateB):
    x1,y1 = coordinateA
    x2,y2 = coordinateB
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def heuristicsFunction(coordinates, goal):
    heuristics = {}
    for node in coordinates.keys():
        heuristicValue = euclideanDistance(coordinates[node], coordinates[goal])
        heuristics[node] = heuristicValue
    return heuristics