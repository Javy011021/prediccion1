
from operators import random_permutation, \
                      interchange, ox_crossover, \
                      first_permutation, next_permutation

# ----------------------------------------------------------------------
# global parameters
# ----------------------------------------------------------------------

LIST_LENGTH = 10  # number of variables (or genes) in each solution

# ----------------------------------------------------------------------
# configuration of the problem
# ----------------------------------------------------------------------

Presentation  = 'Sort a list in ascending order'

def present_problem():
    print('----------------------------------------------------------------------')
    print(Presentation)
    print(f'LIST_LENGTH = {LIST_LENGTH}')
    print('----------------------------------------------------------------------')

def objective_function(solution):
    return sorted_permutation(solution)

def random_solution():
    return random_permutation(LIST_LENGTH)

def not_random_solution():
    return first_permutation(LIST_LENGTH)

def random_change(solution):
    return interchange(solution)

def not_random_change(solution):
    return next_permutation(solution,LIST_LENGTH)

def random_combination(solution1,solution2):
    return ox_crossover(solution1,solution2)

# ----------------------------------------------------------------------
# objective functions
# ----------------------------------------------------------------------

def sorted_permutation(solution): # all precedences in ascending order
    fitness = 0
    for i in range(0, len(solution) - 1):
        for j in range(i+1, len(solution)):
            if solution[i]<=solution[j]:
                fitness += 1
    return fitness

