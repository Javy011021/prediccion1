import math

from operators import random_list, \
                      change1, uniform_crossover, \
                      first_list, next_list

# ----------------------------------------------------------------------
# global parameters
# ----------------------------------------------------------------------

MIN_VALUE: int = 0  # minimum value to be used in the generation of random values for a variable
MAX_VALUE = 100  # maximum value to be used in the generation of random values for a variable
LIST_LENGTH = 2  # number of variables (or genes) in each solution

# ----------------------------------------------------------------------
# configuration of the problem
# ----------------------------------------------------------------------

Presentation  = 'Optimize de function z = sin(x) + tan(y) + 1.25(x+ y)'

def present_problem():
    print('----------------------------------------------------------------------')
    print(Presentation)
    print(f'LIST_LENGTH = {LIST_LENGTH}, MIN_VALUE = {MIN_VALUE}, MAX_VALUE = {MAX_VALUE}')
    print('----------------------------------------------------------------------')

def objective_function(solution):
    return MathFunction5(solution)

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

def MathFunction5(solution):  # I am going to give you z dollars
    # after you tell me the value of x and ya particular case)
    # z= sin(x) + tan(y) + 1.25(x+ y)
    fitness = math.sin(solution[0]) + \
              math.tan(solution[1])  + \
              math.pow(1.25, solution[0] + solution[1])
    return fitness

