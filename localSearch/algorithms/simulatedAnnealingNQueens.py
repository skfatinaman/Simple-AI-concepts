import random, math
#N queens puzzle implementation using hill climbing algorithm
N = int(input("Enter number of queens : "))
#random solution should be generated 
# solution should be represented as a list of n entries
# i-th entry represents the row number of queen in i-th column

def generateRandomSolution(N):
    solution = [i for i in range(N)]
    random.shuffle(solution)
    print("Random Solution generated: ")
    print(solution)
    return solution

#heuristicFunction
def checkAttackingQueens(sol):
        attacking = 0
        for i in range(len(sol)):
            currentQueenCol = i
            currentQueenRow = sol[i]
            for j in range(len(sol)):
                if i !=j:
                    compQueenCol = j
                    compQueenRow = sol[j]
                    rowComparator = abs(currentQueenRow - compQueenRow)
                    colComparator = abs(currentQueenCol-compQueenCol)
                    if (rowComparator == colComparator) or (currentQueenCol == compQueenCol) or (currentQueenRow == compQueenRow):
                         attacking +=1
        return attacking

def generateNeighbors(sol):
    neighbors = []
    #picking one column and moving the queen to different rows
    for col in range(len(sol)):
        currentRow = sol[col]
        for row in range(len(sol)):
            toModify = sol.copy()
            if row != currentRow:
                toModify[col] = row
                neighbors.append(toModify)
    return neighbors

#Everything above is the same as from hill climbing algorithm

def simulatedAnnealing(N,temperature,cooling, minTemperature):
    mainSol = generateRandomSolution(N)
    mainHeuristics = checkAttackingQueens(mainSol)
    while temperature > minTemperature:
        neighbors = generateNeighbors(mainSol)
        randomNeigbour = random.choice(neighbors)
        randomNeigbourHeuristics = checkAttackingQueens(randomNeigbour)
        if randomNeigbourHeuristics < mainHeuristics:
            mainSol = randomNeigbour
            mainHeuristics = randomNeigbourHeuristics
        else :
            d = randomNeigbourHeuristics - mainHeuristics
            p = math.exp(-d/temperature)
            if random.random()<p:
                print("Accepting probable state: ")
                print(randomNeigbour)
                mainSol = randomNeigbour
                mainHeuristics = randomNeigbourHeuristics
        if randomNeigbourHeuristics == 0:
            print(f"Solution found : ")
            print(mainSol)
            return mainSol,mainHeuristics
        temperature *= cooling
        print("Cooling the temperature.....")
    print(f"Best possible solution that can be found is with {mainHeuristics} attacking queens: ")
    print(mainSol)
    return mainSol, mainHeuristics

sol,cost = simulatedAnnealing(N,50,0.99,0.001)