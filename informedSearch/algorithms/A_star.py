import distanceGraph
import heapq

def aStartSearch(graph,heuristics, start, goal):
    minHeap = [(heuristics[start],0,start)]
    parent = {start : None}
    distance = {start : 0}
    nodes_visited = 1
    while minHeap:
        goodness, cost, node = heapq.heappop(minHeap)
        if node == goal :
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, cost, nodes_visited
        for neighbor, newCost in graph[node].items():
            totalCost = cost + newCost
            nodes_visited +=1
            if neighbor not in distance.keys() or distance[neighbor] > totalCost:
                heapq.heappush(minHeap, (totalCost+heuristics[neighbor], totalCost, neighbor))
                parent[neighbor] = node
                distance[neighbor] = totalCost
    return None, None, nodes_visited

graph = distanceGraph.graph
start = "A"
goal = "L"
heuristics = distanceGraph.heuristicsFunction(distanceGraph.coordinates, goal)

path, cost, nodes = aStartSearch(graph,heuristics, start, goal)
print("A star Algorithm Results : ")
print(f"The path is : {path}")
print(f"The cost is : {cost}")
print(f"Nodes visited : {nodes}")