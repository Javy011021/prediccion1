import random
import math

from operators import random_list, \
                      change1, uniform_crossover, \
                      first_list, next_list

# ----------------------------------------------------------------------
# global parameters
# ----------------------------------------------------------------------

LIST_LENGTH = 7    # number of variables (or genes) in each solution
VALUES_RND  = False # True: profits and size generated at random, False: generated in arbitrary way
CAPACITY    = 3     # Capacity of the Knapsack
MIN_VALUE   = 0     # The item is in the Knapsack
MAX_VALUE   = 1     # The item is not in the Knapsack

# ----------------------------------------------------------------------
# configuration of the problem
# ----------------------------------------------------------------------

Presentation  = 'Knapsack Problem'

def present_problem():
    print('----------------------------------------------------------------------')
    print(Presentation)
    print(f'LIST_LENGTH = {LIST_LENGTH}, CAPACITY = {CAPACITY}, MAX_VALUE = {MAX_VALUE}, VALUES_RND = {VALUES_RND}')
    print(f'Profits and sizes of the items = {prof_size}')
    print('----------------------------------------------------------------------')

def objective_function(solution):
    return knapsack(solution)

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
# objective functions
# ----------------------------------------------------------------------

def knapsack(solution):
    fitness = 0
    volume = 0
    penalty = 0
    for i in range(0, len(solution)):
        fitness += prof_size[0][i]*solution[i]  # profits
        volume  += prof_size[1][i]*solution[i] # volumes
    if volume > CAPACITY: # the knapsack is overloaded
        penalty = 10 * (volume - CAPACITY) # a penalty applied to unfeasible solutions
    return fitness - penalty

# ----------------------------------------------------------------------
# auxiliary functions
# ----------------------------------------------------------------------

def random_volprofs(number):
    prof_size = [[0] * number, [0] * number] # volumes and profits
    for i in range(0, number):
        prof_size[0][i] = random.randint(0, 100) # volumes
        prof_size[1][i] = random.randint(0, 100) # profits
    return prof_size

def arbitrary_volprofs(number):
    raw_prof_size = [[2, 3, 2  , 4, 6, 6.5, 5, 2, 3, 2  , 4, 6, 6.5, 5, 2, 3, 2  , 4, 6, 6.5, 5],
                     [1, 2, 2.5, 1, 2, 3  , 1, 1, 2, 2.5, 1, 2, 3  , 1, 1, 2, 2.5, 1, 2, 3  , 1]]
    # list[start:end:step] start> the first to be included 0.., end>the first to be ignored
    prof_size =   [raw_prof_size[0][:number],
                   raw_prof_size[1][:number]]
    return prof_size

if VALUES_RND:
    prof_size = random_volprofs(LIST_LENGTH)
else:
    prof_size = arbitrary_volprofs(LIST_LENGTH)

