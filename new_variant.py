import random
from decimal import Decimal
import numpy as np

ITERATIONS = 20
DAYS = [23, 24, 25]
PAST_DAYS = [[45,20,38,25,32],[46,21,39,26,33], [47,22,40,27,34]]
INTERVAL = 0.2


def exact_add(*nbs):
    return float(sum([Decimal(str(nb)) for nb in nbs]))


def alt_function(min: float = 0, max: float = 1, intv: int = INTERVAL, num_vals: int = 5):
    return [float(f'{round(random.uniform(min, max) / intv) * intv:.2f}') for _ in range(num_vals)]


def obj_function(vals: list):
    error = 0
    for i in range(len(DAYS)):
        predict = 0
        for j in range(len(PAST_DAYS[i])):
            predict += PAST_DAYS[i][j]*vals[j]
        error += abs((DAYS[i]-predict))
    return error

def best_alt_solution():
    solution = alt_function()
    min_error = obj_function(solution)
    for i in range(ITERATIONS):
        actual_sol = alt_function()
        error = obj_function(actual_sol)
        if error < min_error:
            min_error = error
            solution = actual_sol
    
    print(f'solucion: {solution} \t error:{min_error}')
    return [solution]
        


def h_solution(iterations: int = 10000):
    current_solution = alt_function()
    print(current_solution)
    current_error = obj_function(current_solution)

    for _ in range(iterations):
        neighbor_solution = current_solution.copy()
        random_index = random.randint(0, len(neighbor_solution) - 1)
        change = random.choice([INTERVAL*-1,INTERVAL])

        if neighbor_solution[random_index] + change >= 0:
            neighbor_solution[random_index] = exact_add(neighbor_solution[random_index], change)
            neighbor_error = obj_function(neighbor_solution)

            if neighbor_error < current_error:
                current_solution = neighbor_solution
                current_error = neighbor_error

    print(f'Mejor solución: {current_solution} \t Error: {current_error}')
    return current_solution

def test ():
    l = alt_function()
    r = obj_function(l)
    print(f'valores: {l}')
    print(f'error: {r}')


best_alt_solution()
# test()
h_solution()

