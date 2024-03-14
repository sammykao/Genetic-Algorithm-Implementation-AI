


 # BACKPACK PROBLEM INTRO
    - Given a set of boxes with weights and importance, how can we fill
    a backpack with max weight 250 to maximize importance
    - We cannot repeat these weights, they are all individualistic

 # IMPLEMENTING AND DEFINING AS GENETIC ALGORITHM
    - We need to define an initial population of 'individuals' and phenotypes.
    We can do this by randomly sampling part of the grand population. 
    There are 1(all vars) + 11! + 10! + ... + 2! * 1 different individuals we can
    represent. So, 43,954,714 solutions in the search space! Let's represent the 
    effectiveness  of genetic algorithms by creating an intial population that is 
    ~0.023 perecent the size of the search space (i.e 10k individual) We will 
    randomly sample up to 10k elements into our initial population

    - How we define Phenotypes or individuals: We can represent an individual 
    representing a phenotype as one possible solution. A solution is any set of 
    the weights from size 0 to size 12 (length of our weight set)

    - A genotype will be a weight, since our phenotype is a combination
    of our genotypes. Note: in most genetics, we have set phenotype size,
    but this problem is particularly interesting since we have a dynamic 
    phenotype length. In biology when we have different numbers of chromosomes,
    there are possibilities of survival, but at a lower rate.

    - So, as mentioned before the Genome is all the weights --> then, 
    they come together to represent a phenotype (possible solution) --> then,
    we can assign a fitness to that solution ---> apply natural fitness and SELECTION --> then,
    over many generations our populations excels and becomes more optimal

    - Our fitness function will represent how important it is. (Just like society!).
    If the weights exceed our max weight (250), then it is unimportant with fitness
    value as 0.


# APPLYING SELECTION AND REPRODUCTION:
    - For our selection pressures, we implement Truncated Based Selection,
    with CULLING our populaton by around 50 percent for every generation.

    - Only the top 50 percent of individuals are able to reproduce 

    - Within this 50 percent, we can assign probabilistic weights for
    the fittest individuals to have better chances of reproducing

    - For our reproduction measures or FRINGE OPERARTIONS, we use
    recombination or crossovers to create new children. We use 
    single point crossover to create consistency within maximizing
    the fitness of children reproduced

    - Note: It is best to not implement mutations with our algorithm
    because the genomes are singular and the phenotype size is dynamic.
    That means imeplementing individualistic mutations is very challenging
    and debatedably redundant.

# ASSUMPTIONS:
    - As mentioned, we assume max weight is 250
    - We also assume that weights cannot be repeated
    


