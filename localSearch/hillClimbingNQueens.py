import random
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

def hillClimb(N,restarts):
    mainSol = None
    heuristic = None
    for restart in range(1,restarts+1):
        initSol = generateRandomSolution(N)
        currentSol = initSol
        currentSolHeuristics = checkAttackingQueens(currentSol)
        
        betterExists = True

        while betterExists:
            neighbors = generateNeighbors(currentSol)
            best = None
            bestHeuristics = None
            foundThisIteration = False
            for sol in neighbors:
                solHeuristics = checkAttackingQueens(sol)
                if best == None:
                    best = sol
                    bestHeuristics = solHeuristics
                elif solHeuristics < bestHeuristics:
                    best = sol
                    bestHeuristics = solHeuristics
                    
            if bestHeuristics < currentSolHeuristics:
                currentSol = best
                currentSolHeuristics = bestHeuristics
                foundThisIteration = True
                print(f"Better solution found with {currentSolHeuristics} attacking queens : " )
                print(currentSol)

            if not foundThisIteration:
                betterExists = False
        if mainSol == None:
            mainSol = currentSol
            heuristic = currentSolHeuristics
        else:
            if currentSolHeuristics < heuristic:
                mainSol = currentSol
                heuristic = currentSolHeuristics
        if heuristic == 0:
            break
        print("Randomly restarting....")
        print(f"Restart number : {restart}")
    return mainSol,heuristic

sol,attackingQueens = hillClimb(N,100)
print(f"found soltion with {attackingQueens} attacking queens: ")
print(sol)