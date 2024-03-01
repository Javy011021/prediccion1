
from operators import random_list, \
                      change1, uniform_crossover, \
                      first_list, next_list

# ----------------------------------------------------------------------
# global parameters
# ----------------------------------------------------------------------

MIN_VALUE: int = 0  # minimum value to be used in the generation of random values for a variable
MAX_VALUE = 1  # maximum value to be used in the generation of random values for a variable
LIST_LENGTH = 10  # number of variables (or genes) in each solution

# ----------------------------------------------------------------------
# configuration of the problem
# ----------------------------------------------------------------------

Presentation  = 'Optimize de presence of the MAX_VALUE'

def present_problem():
    print('----------------------------------------------------------------------')
    print(Presentation)
    print(f'LIST_LENGTH = {LIST_LENGTH}, MIN_VALUE = {MIN_VALUE}, MAX_VALUE = {MAX_VALUE}')
    print('----------------------------------------------------------------------')

def objective_function(solution):
    return OneMax(solution)

def random_solution():
    return random_list(LIST_LENGTH, MIN_VALUE, MAX_VALUE)

def not_random_solution():
    return first_list(LIST_LENGTH, MIN_VALUE, MAX_VALUE)

def random_change(solution):
    return change1(solution, MIN_VALUE, MAX_VALUE)

def not_random_change(solution):
    return next_list(solution, LIST_LENGTH, MIN_VALUE, MAX_VALUE)

def random_combination(solution1, solution2):
    return uniform_crossover(solution1, solution2)

# ----------------------------------------------------------------------
# objective function
# ----------------------------------------------------------------------

def OneMax(solution):  # version of OneMax counting the presence of MAX_VALUE (1 as a particular case)
    fitness = 0
    for i in range(0, len(solution) - 1):
        if solution[i]==MAX_VALUE:
            fitness += 1
    return fitness

