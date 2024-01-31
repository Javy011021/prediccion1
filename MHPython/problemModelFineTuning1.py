import random
import math

from operators import random_list, \
                      random_change_for_lists, uniform_crossover, \
                      first_list, next_list

# ----------------------------------------------------------------------
# global parameters
# ----------------------------------------------------------------------

MIN_VALUE: int = -200  # minimum value to be used in the generation of random values for a variable
MAX_VALUE = 200  # maximum value to be used in the generation of random values for a variable
LIST_LENGTH = 4  # number of variables (or genes) in each solution
EXAMPLES_RND = False       # True: points to calibrate the model generated at random, False: generated in arbitrary way
RESOLUTION = 10

# ----------------------------------------------------------------------
# configuration of the problem
# ----------------------------------------------------------------------

Presentation  = 'Fine tuning the model Y= k0*X + k1*sin(k2*X+k3) + (X+k4)^k5'

def present_problem():
    print('----------------------------------------------------------------------')
    print(Presentation)
    print(f'LIST_LENGTH = {LIST_LENGTH},  EXAMPLES_RND = {EXAMPLES_RND}')
    print(f'MIN_VALUE = {MIN_VALUE},  MAX_VALUE = {MAX_VALUE}, RESOLUTION = {RESOLUTION}')
    print(f'Points to calibrate the model = {examples}')
    print('----------------------------------------------------------------------')

def print_solution_details(solution):
    print('Solution = ',solution)
    evaluation = error(solution,True)
    print(f'Solution:{solution} with evaluation {evaluation}')

def objective_function(solution):
    return error(solution)

def random_solution():
    # return [151.70390893980323, -8.520352464055922, 0.18814727435023762, -0.0012] # [153.79, -8.3201, 0.1888, -0.0012]
    return random_list(LIST_LENGTH, MIN_VALUE, MAX_VALUE,INTEGER=False)

def not_random_solution():
    return first_list(LIST_LENGTH, MIN_VALUE, MAX_VALUE)

def random_change(solution):
    return random_change_for_lists(solution, MIN_VALUE, MAX_VALUE,INTEGER=False)

def not_random_change(solution):
    return next_list(solution, LIST_LENGTH, MIN_VALUE, MAX_VALUE, INTEGER=False, resolution=RESOLUTION)

def random_combination(solution1, solution2):
    return uniform_crossover(solution1, solution2)

# ----------------------------------------------------------------------
# objective functions
# ----------------------------------------------------------------------

def error(solution, echo=False):
    # Model: Y = k0 * X + k1 * sin(k2 * X + k3) + (X + k4) ^ k5
    fitness = 0
    if echo:
        print(f'Solution = {solution}')
    for i in range(0, len(examples[0])):
        X = examples[0][i]
        Y = examples[1][i]
        estimate = solution[0]  + \
                   solution[1] * X + \
                   solution[2] * X**2 + \
                   solution[3] * X**3
#                   solution[2]*math.sin(solution[3] * X + solution[4]) + \
#                   math.pow(X,solution[5])
        d= abs(estimate-Y) # absolute error
        if echo:
            print(f'For ({X},{Y}) the estimation is {estimate} with error = {d}')
        fitness += d
    return fitness

# ----------------------------------------------------------------------
# auxiliary functions
# ----------------------------------------------------------------------

def random_examples():
    number_of_examples = 5
    examples = [[0] * number_of_examples,[0] * number_of_examples]
    for i in range(0, number_of_examples):
        examples[0][i] = random.randint(0, 100)
        examples[1][i] = random.randint(0, 100)
    return examples

def arbitrary_examples():
    examples = [[10,24,96,15,79],
                [80,39, 6,82,69]]
    return examples

if EXAMPLES_RND:
    examples = random_examples()
else:
    examples = arbitrary_examples()

'''
examples = random_examples()
print(f'examples = {examples}')
print(f'len(examples) = {len(examples)}')

examples = arbitrary_examples()
print(f'examples = {examples}')
print(f'len(examples) = {len(examples)}')
'''

# Solution:[-200, -200, -185, -52] with evaluation 76565

#solution = [-200, -200, -185, -52]
#y = -0.0012x3 + 0.1888x2 - 8.3201x + 153.79    R² = 0.9212
#solution = [153.79, - 8.3201, 0.1888, -0.0012]
#print_solution_details(solution)
#Solution:[153.79, -8.3201, 0.1888, -0.0012] with evaluation 71.6322000000001
