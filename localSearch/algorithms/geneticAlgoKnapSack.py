import random,heapq

items = {
    # (weight, value)
    1:  (4, 12),
    2:  (2, 4),
    3:  (6, 14),
    4:  (3, 7),
    5:  (5, 10),
    6:  (7, 18),
    7:  (1, 3),
    8:  (9, 22),
    9:  (8, 20),
    10: (4, 9),
    11: (2, 5),
    12: (3, 8),
    13: (5, 15),
    14: (6, 17),
    15: (7, 19),
    16: (1, 2),
    17: (8, 21),
    18: (4, 11),
    19: (3, 6),
    20: (5, 13)
}

capacity = 35


def fitness(chromosome, items, capacity):
    currentCapacity = 0
    currentProfit = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            weight = items[i+1][0]
            value = items[i+1][1]
            currentCapacity += weight
            currentProfit += value
    if currentCapacity > capacity:
        return -1
    else:
        return currentProfit
    
def generateChromosome(items):
    numberOfItems = len(items.keys())
    choices = [0,1]
    chromosome = []
    for _ in range(numberOfItems):
        chromosome.append(random.choice(choices))
    return chromosome

def crossingOver(chromo1, chromo2, childrenNumber,mutations):
    children = []
    for _ in range(childrenNumber):
        crossingOverPoint = random.choice(range(len(chromo1)))

        chromo1_part1 = chromo1[:crossingOverPoint]
        chromo1_part2 = chromo1[crossingOverPoint:]

        chromo2_part1 = chromo2[:crossingOverPoint]
        chromo2_part2 = chromo2[crossingOverPoint:]

        child1 = chromo1_part1 + chromo2_part2
        child2 = chromo2_part1 + chromo1_part2

        child1 = mutate(child1,mutations)
        child2 = mutate(child2,mutations)

        children.append(child1)
        children.append(child2)
    return children

def mutate(chromosome, mutations):
    chromoRange= range(len(chromosome))
    for _ in range(mutations):
        mutationPoint = random.choice(chromoRange)
        if chromosome[mutationPoint] == 1:
            chromosome[mutationPoint] = 0
        else:
            chromosome[mutationPoint] = 1
    return chromosome

def generation_replacement(items,capacity, generations, childrenPerGen,mutations):
    parent1 = generateChromosome(items)
    fitnessP1 = fitness(parent1, items, capacity)
    parent2 = generateChromosome(items)
    fitnessP2 = fitness(parent2, items, capacity)
    for gen in range(1,generations+1):
        minHeap = []
        children = crossingOver(parent1,parent2,childrenPerGen,mutations)
        for child in children :
            fitnessOfChild = fitness(child, items, capacity)
            pushTuple = (-fitnessOfChild,child)
            heapq.heappush(minHeap,pushTuple)
        p1 = heapq.heappop(minHeap)
        parent1 = p1[1]
        fitnessP1 = p1[0]
        p2 = heapq.heappop(minHeap)
        parent2 = p2[1]
        fitnessP2 = p2[0]
        print(f"Fittest of the generation {gen}: ")
        print(parent1)
        print(f"Score : {-fitnessP1}")
        print(parent2)
        print(f"Score : {-fitnessP2}")
    bestSolution = None
    if -fitnessP1 > -fitnessP2:
        print(f"Best solution is with fitness : {-fitnessP1}")
        print(parent1)
        return parent1
    else:
        print(f"Best solution is with fitness : {-fitnessP2}")
        print(parent2)
        return parent1

def elitism(items,capacity, generations, childrenPerGen,mutations):
    #to be implemented
    pass

sol = generation_replacement(items,capacity, 10, 10, 3)