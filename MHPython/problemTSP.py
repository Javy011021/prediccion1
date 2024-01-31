import random
import math

from operators import random_permutation, \
                      interchange, ox_crossover, \
                      first_permutation, next_permutation

# ----------------------------------------------------------------------
# global parameters
# ----------------------------------------------------------------------

LIST_LENGTH = 10  # number of variables (or genes) in each solution
COORDINATES_RND = False       # True: coordinates generated at random, False: generated in arbitrary way

# ----------------------------------------------------------------------
# configuration of the problem
# ----------------------------------------------------------------------

Presentation  = 'Travelling Salesman Problem'

def present_problem():
    print('----------------------------------------------------------------------')
    print(Presentation)
    print(f'LIST_LENGTH = {LIST_LENGTH},  COORDINATES_RND = {COORDINATES_RND}')
    print(f'Coordinates for TSP = {coordinates}')
    print('----------------------------------------------------------------------')

def objective_function(solution):
    return tsp(solution)

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

def tsp(solution):
    fitness = 0
    for i in range(0, len(solution) - 1):
        d= (coordinates[0][solution[i]]-coordinates[0][solution[i+1]])**2+\
                   (coordinates[1][solution[i]]-coordinates[1][solution[i+1]])**2
        d = math.sqrt(d)
        fitness += d
    d = (coordinates[0][solution[len(solution)-1]] - coordinates[0][solution[0]]) ** 2 +\
        (coordinates[1][solution[len(solution)-1]] - coordinates[1][solution[0]]) ** 2
    d = math.sqrt(d)
    fitness += d
    return fitness

# ----------------------------------------------------------------------
# auxiliary functions
# ----------------------------------------------------------------------

def random_coordinates(number):
    coordinates = [[0] * number,[0] * number]
    for i in range(0, number):
        coordinates[0][i] = random.randint(0, 100)
        coordinates[1][i] = random.randint(0, 100)
    return coordinates

def arbitrary_coordinates(number):
    raw_coordinates = [[10,24,96,15,79, 10,24,96,15,79, 10,24,96,15,79, 10,24,96,15,79, 10,24,96,15,79],
                       [80,39, 6,82,69, 80,39, 6,82,69, 80,39, 6,82,69, 80,39, 6,82,69, 80,39, 6,82,69]]
    # list[start:end:step] start> the first to be included 0.., end>the first to be ignored
    coordinates = [raw_coordinates[0][:number],
                   raw_coordinates[1][:number]]
    return coordinates

if COORDINATES_RND:
    coordinates = random_coordinates(LIST_LENGTH)
else:
    coordinates = arbitrary_coordinates(LIST_LENGTH)

