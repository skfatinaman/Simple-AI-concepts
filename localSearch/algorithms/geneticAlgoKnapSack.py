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

def generation_replacement(items, capacity, generations, childrenPerGen, mutations):
    # Generate initial parents
    parent1 = generateChromosome(items)
    parent2 = generateChromosome(items)

    # Track generational best
    generationalBest = parent1 if fitness(parent1, items, capacity) >= fitness(parent2, items, capacity) else parent2

    for gen in range(1, generations + 1):
        minHeap = []
        children = crossingOver(parent1, parent2, childrenPerGen, mutations)

        # Evaluate children and push to max-heap
        for child in children:
            f = fitness(child, items, capacity)
            heapq.heappush(minHeap, (-f, child))  # max-heap

        # Include parents for elitism
        heapq.heappush(minHeap, (-fitness(parent1, items, capacity), parent1))
        heapq.heappush(minHeap, (-fitness(parent2, items, capacity), parent2))

        # Select next generation parents (top 2 fittest)
        p1 = heapq.heappop(minHeap)
        p2 = heapq.heappop(minHeap)
        parent1 = p1[1]
        parent2 = p2[1]
        fitnessP1 = -p1[0]
        fitnessP2 = -p2[0]

        print(f"Fittest of generation {gen}:")
        print(f"Parent1: {parent1}, Score: {fitnessP1}")
        print(f"Parent2: {parent2}, Score: {fitnessP2}")

        # Update generational best
        currentBest = parent1 if fitnessP1 >= fitnessP2 else parent2
        if fitness(currentBest, items, capacity) > fitness(generationalBest, items, capacity):
            generationalBest = currentBest

    print(f"\nGenerational best solution is with fitness: {fitness(generationalBest, items, capacity)}")
    print(generationalBest)
    return generationalBest



def elitism(items,capacity, generations, childrenPerGen,mutations):
    #to be implemented
    pass

sol = generation_replacement(items,capacity, 100, 10, 3)