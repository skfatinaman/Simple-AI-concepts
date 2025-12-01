import distanceGraph

def bestFirstSearch(graph,heuristics, start, goal):
    path = [start]
    total_cost = 0
    node = start
    while node != goal:
        bestOptionFromThatNode = None
        for neighbor,cost in graph[node].items():
            if bestOptionFromThatNode == None :
                bestOptionFromThatNode = neighbor
            else :
                if heuristics[neighbor] < heuristics [bestOptionFromThatNode]:
                    bestOptionFromThatNode = neighbor
        total_cost += graph[node][bestOptionFromThatNode]
        node = bestOptionFromThatNode
        path.append(node)
    return path, total_cost

graph = distanceGraph.graph
start = "A"
goal = "L"
heuristics = distanceGraph.heuristicsFunction(distanceGraph.coordinates, goal)

path, cost = bestFirstSearch(graph,heuristics, start, goal)

print(f"The path is : {path}")
print(f"The cost is : {cost}")