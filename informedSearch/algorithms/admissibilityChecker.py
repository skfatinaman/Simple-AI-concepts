import heapq

def graphAndHeuristicsBuilder():
    # take the nodes and edges for the graph
    nodes,edges = map(int,input("Nodes and edges : ").strip().split())

    #take the start and goal destinations
    start, goal = map(int,input("Start and goal : ").strip().split())

    heuristics = {i:None for i in range(1,nodes+1)}
    #input the heuristics
    for i in range(nodes):
        node, heuristicValue = map(int,input("Node and heuristic value : ").strip().split())
        heuristics[node] = heuristicValue

    graph = {i:{} for i in range(1,nodes+1)}
    for i in range(edges):
        fromNode, toNode, cost = map(int,input("Edge and edge cost : ").strip().split())
        graph[toNode][fromNode] = cost
    
    return nodes,edges,start,goal,heuristics,graph

def dijsktraAlgo(nodes,start,goal,graph):
    #starting a dijsktra from goal node to start node
    distance = {}
    minHeap = []
    minHeap.append((0,goal))
    while minHeap:
        cost,thisNode = heapq.heappop(minHeap)
        if thisNode not in distance or distance[thisNode]>cost:
            distance[thisNode] = cost
            for neighbor,dist in graph[thisNode].items():
                pushTuple = (cost+dist,neighbor)
                heapq.heappush(minHeap,pushTuple)
        if thisNode == start:
            print(distance)
            return distance
    return None

def admissiblityChecker(distance,heuristics):
    admissible = True
    inadmissibleNodes = []
    if distance is not None:
        for node,cost in distance.items():
            if cost < heuristics[node]:
                admissible = False
                inadmissibleNodes.append(node)
    else:
        return False
    return admissible,inadmissibleNodes
    
def main():
    nodes,edges,start,goal,heuristics,graph = graphAndHeuristicsBuilder()
    admissible,inadmissibleNodes = admissiblityChecker(dijsktraAlgo(nodes,start,goal,graph),heuristics)
    if admissible:
        print("Admissible")
    else:
        print("Not Admissible")
        print("Inadmissible nodes: ")
        print(inadmissibleNodes)

main()