import distanceGraph

def bestFirstSearch(graph,heuristics, start, goal):
    path = [start]
    total_cost = 0
    node = start
    nodesVisited = 1
    while node != goal:
        bestOptionFromThatNode = None
        for neighbor,cost in graph[node].items():
            nodesVisited +=1
            if bestOptionFromThatNode == None :
                bestOptionFromThatNode = neighbor
            else :
                if heuristics[neighbor] < heuristics [bestOptionFromThatNode]:
                    bestOptionFromThatNode = neighbor
        total_cost += graph[node][bestOptionFromThatNode]
        node = bestOptionFromThatNode
        path.append(node)
    return path, total_cost, nodesVisited

graph = distanceGraph.graph
start = "A"
goal = "L"
heuristics = distanceGraph.heuristicsFunction(distanceGraph.coordinates, goal)

path, cost, nodes = bestFirstSearch(graph,heuristics, start, goal)

print("Best First Search Algorithm Results : ")
print(f"The path is : {path}")
print(f"The cost is : {cost}")
print(f"Nodes visited : {nodes}")