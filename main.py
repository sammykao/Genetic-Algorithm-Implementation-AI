import random


def genetic_algorithm(variables, population, max_weight):
    # with an init pop size of 10k,
    # we can do 9 iterations if we cull and
    # reduce by 50% each time
    # this will lead to a finishing pop. size
    # of around 19 individuals
    for i in range(9):
        sorted_fitness = sorted(population, key=lambda x: x[0], reverse=True)
        # print current best after iteration
        indexes = []
        worst_solution = sorted_fitness[len(sorted_fitness)  - 1][1]
        for item in worst_solution:
            indexes.append(str(variables.index(item) + 1))
        print(f'Worst individual in population after iteration #{i+1}: #{", #".join(indexes)}')
        # end print

        #cull population
        n = len(sorted_fitness) // 2
        sorted_fitness = sorted_fitness[:n]

        new_population = []
        weights = [i for i in range(n, 0, -1)]
        for i in range(n):
            # we create weights to give higher probability of most fit reproducing
            x = random.choices(sorted_fitness, weights=weights, k=1)[0]
            y = random.choices(sorted_fitness, weights=weights, k=1)[0]

            child = reproduce(x[1], y[1])
            new_population.append((fitness_func(child, max_weight), child))

        population = new_population
    sorted_fitness = sorted(population, key=lambda x: x[0], reverse=True)

    # then we return the top individual out of our ~19 individuals
    return sorted_fitness[0][1]

def reproduce(x, y):
    n = min(len(x), len(y))
    split = random.randint(0, n - 1)
    # random one point crossover
    child = list(set(x[:split] + y[split:]))

    return child



def fitness_func(phenotype, max_weight):
    # our fitness function is the sum of importance
    # of variables in our phenotype.
    importance = 0
    weight = 0
    for i in range(len(phenotype)):
        importance += phenotype[i][1]
        weight += phenotype[i][0]

        # If the weight is over 250, it will return 0 
        if weight > max_weight:
            return 0

    return importance

def initialize_population(variables, max_weight):
    # There are 1(all vars) + 11! + 10! + ... + 2! * 1 different individuals we can
    # represent. So, 43,954,714 solutions in the search space!
    # let's represent the effectiveness  of genetic algorithms by creating an 
    # intial population that is ~0.023% the size of the search space (i.e 10k individual)
    # We will randomly sample up to 10k elements into our initial population
    init_population = []
    for i in range(10000):
        random_size = random.randint(1, len(variables))
        individual = random.sample(variables, random_size)
        random_individual = (fitness_func(individual, max_weight), individual)
        init_population.append(random_individual)
    return init_population


def main():
    # All the possible genotypes in our search problem
    variables = [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9), \
    (30, 4), (30, 5), (70, 4), (20, 9), (20, 2), (60, 1)]
    # Maximum weigth of backpack
    max_weight = 250
    init_population = initialize_population(variables, max_weight)
    solution = genetic_algorithm(variables, init_population, max_weight)
    indexes = []
    for item in solution:
        indexes.append(str(variables.index(item) + 1))
    print("--------------------------------------------------------------------------------")
    print(f'Optimal Solution after Genetic Algorithm: #{", #".join(indexes)}')

main()