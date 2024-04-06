import random
import numpy as np
from decimal import Decimal
from MHPython.operators import uniform_crossover

ITERATIONS = 20
DAYS = [18.38, 45.74, 47.88, 19.19, 32.81, 39.32, 20.88, 27.97, 34.59, 3.7]

PAST_DAYS = [
    [13.76, 9.72, 35.23, 5.62, 17.09],
    [37.89, 27.56, 8.8, 14.43, 44.45],
    [34.03, 21.89, 12.79, 4.58, 47.85],
    [48.65, 15.03, 31.43, 11.02, 41.61],
    [30.99, 12.82, 41.73, 13.98, 43.13],
    [0.74, 25.71, 42.11, 28.45, 41.18],
    [38.11, 16.64, 32.57, 3.24, 22.23],
    [33.39, 14.95, 9.88, 24.15, 10.54],
    [21.04, 41.36, 48.63, 25.3, 16.5],
    [12.77, 30.26, 3.46, 16.65, 13.98],
]
STEP = 0.1
MIN_VALUE=-1
MAX_VALUE=1

Presentation  = 'Rain Problem'
def present_problem():
    print('---------------------------------------------------------------------------------------------')
    print(Presentation)
    # print(f'LIST_LENGTH = {LIST_LENGTH}, CAPACITY = {CAPACITY}, MAX_VALUE = {MAX_VALUE}, VALUES_RND = {VALUES_RND}')
    # print(f'Profits and sizes of the items = {prof_size}')
    print('---------------------------------------------------------------------------------------------')
    

def exact_add(*nbs):
    return float(sum([Decimal(str(nb)) for nb in nbs]))

def random_value(min: float = MIN_VALUE, max: float = MAX_VALUE, intv: int = STEP):
    return float(f'{round(random.uniform(min, max) / intv) * intv:.2f}')
    
def obj_function(vals: list):
    error = 0
    for i in range(len(DAYS)):
        predict = 0
        for j in range(len(PAST_DAYS[i])):
            predict += PAST_DAYS[i][j]*vals[j]
        error += abs((DAYS[i]-predict))
    return error

def random_solution(min: float = MIN_VALUE, max: float = MAX_VALUE, intv: int = STEP, num_vals: int = 5):
    return [random_value(min=min, max=max, intv=intv) for _ in range(num_vals)]

def heuristic_solution(iterations: int = 10000):
    current_solution = random_solution()
    print(current_solution)
    current_error = obj_function(current_solution)

    for _ in range(iterations):
        neighbor_solution = current_solution.copy()
        random_index = random.randint(0, len(neighbor_solution) - 1)
        change = random.choice([STEP*-1,STEP])

        if neighbor_solution[random_index] + change >= 0:
            neighbor_solution[random_index] = exact_add(neighbor_solution[random_index], change)
            neighbor_error = obj_function(neighbor_solution)

            if neighbor_error < current_error:
                current_solution = neighbor_solution
                current_error = neighbor_error

    print(f'Mejor solución: {current_solution} \t Error: {current_error}')
    return current_solution


# the value of a random position is randomly changed
def random_change(solution, MIN_VALUE=MIN_VALUE, MAX_VALUE=MAX_VALUE): 
    random_index = random.randint(0, len(solution) - 1)
    solution[random_index] = random_value(min=MIN_VALUE, max=MAX_VALUE)
    return solution

def not_random_change(solution, interval=0.1):
    changed_solution = [val + interval for val in solution]
    return changed_solution


# each value is chosen randomly from any of the solutions
def random_combination(solution1, solution2):
    return uniform_crossover(solution1, solution2)


#Test Functions
def test ():
    l = random_solution()
    r = obj_function(l)
    print(f'valores: {l}')
    print(f'error: {r}')

def best_alt_solution():
    solution = random_solution()
    min_error = obj_function(solution)
    for i in range(ITERATIONS):
        actual_sol = random_solution()
        error = obj_function(actual_sol)
        if error < min_error:
            min_error = error
            solution = actual_sol
    
    print(f'solucion: {solution} \t error:{min_error}')
    return [solution]

# best_alt_solution()
# test()
# heuristic_solution()

