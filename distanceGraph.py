import math
coordinates = {
    "A": (0, 0),
    "B": (3, 5),
    "C": (7, 2),
    "D": (10, 6),
    "E": (13, 1),
    "F": (4, 10),
    "G": (8, 11),
    "H": (12, 9),
    "I": (15, 4),
    "J": (6, 15),
    "K": (11, 14),
    "L": (14, 12)
}

graph = {
    "A": {"B": 7, "C": 9},
    "B": {"A": 7, "F": 7, "C": 7},
    "C": {"A": 9, "B": 7, "D": 6, "G": 10},
    "D": {"C": 6, "G": 6, "H": 7, "E": 8},
    "E": {"D": 8, "H": 7, "I": 7},
    "F": {"B": 7, "G": 7, "J": 6},
    "G": {"F": 7, "C": 10, "D": 6, "K": 8},
    "H": {"D": 7, "E": 7, "K": 7, "L": 8},
    "I": {"E": 7, "L": 6},
    "J": {"F": 6, "K": 9},
    "K": {"J": 9, "G": 8, "H": 7, "L": 5},
    "L": {"K": 5, "H": 8, "I": 6}
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