# tsp requires a salesman to travel a whole graph
# exploring each node once and ensuring that start node = end node

import random

graph = {
    "A": {"B": 10, "C": 15, "D": 20, "E": 10, "F": 25},
    "B": {"A": 10, "C": 35, "D": 25, "E": 17, "F": 28},
    "C": {"A": 15, "B": 35, "D": 30, "E": 14, "F": 22},
    "D": {"A": 20, "B": 25, "C": 30, "E": 16, "F": 18},
    "E": {"A": 10, "B": 17, "C": 14, "D": 16, "F": 12},
    "F": {"A": 25, "B": 28, "C": 22, "D": 18, "E": 12}
}

def get_path_cost(graph,path):
    cost = 0
    for i in range(len(path)-1):
        fromNode = path[i]
        toNode = path[i+1]
        cost += graph[fromNode][toNode]
    return cost

def randomSolution(graph):
    nodes = list(graph.keys())
    random.shuffle(nodes)
    nodes.append(nodes[0])
    return nodes

def generateNeighbors(path):
    #generate neighbors by using two opt swap
    neighbors = []
    copyPath = path[1:len(path)-1]
    for i in range(len(copyPath)):
        for j in range(i+1,len(copyPath)):
            copyPath[i], copyPath[j] = copyPath[j], copyPath[i]
            neighbor = [path[0]] + copyPath + [path[0]]
            neighbors.append(neighbor)
    neighbors.append(path)
    return neighbors

def hillClimb(graph, restarts):
    mainSol = None
    mainCost = None
    for restart in range(1,restarts+1):
        initPath = randomSolution(graph)
        print("Generated random path: ")
        print(initPath)
        initCost = get_path_cost(graph,initPath)
        neighbors = generateNeighbors(initPath)
        for neighbor in neighbors:
            neighborCost = get_path_cost(graph,neighbor)
            if mainSol is None or neighborCost < mainCost:
                mainSol = neighbor
                mainCost = neighborCost
                print(f"Found a better path with cost{mainCost}: ")
                print(mainSol)
        print(f"No better path found with cost less than {mainCost}")
        print(f"Initiating restart : {restart}")
    
    print(f"Best solution after {restarts} restarts: ")
    print(f"Path: ", end = "")
    print(mainSol)
    print(f"Path cost: {mainCost}")

    return mainSol, mainCost

path,cost = hillClimb(graph,15)