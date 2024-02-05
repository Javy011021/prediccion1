import random
import numpy as np

ITERATIONS = 20
DAYS = [23, 24, 25]
PAST_DAYS = [[45,20,38,25,32],[46,21,39,26,33], [47,22,40,27,34]]




def alt_function(min: float = 0, max: float = 1, intv: int = 0.2, num_vals: int = 5):
    return [float(f'{round(random.uniform(min, max) / intv) * intv:.2f}') for _ in range(num_vals)]


def obj_function(vals: []):
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
        

#socion que empece a hacer
def h_solution():
    alt = alt_function()
    alt = sorted(alt)
    dif = [[0,0],[1,0],[2,0],[3,0],[4,0]]


    for i in range(len(PAST_DAYS)):
        for j in range(len(DAYS)):
            dif[j][1] += abs(DAYS[j] - PAST_DAYS[i][j])
    
    dif_ordenada = sorted(dif, key=lambda x: x[1])
    print(dif_ordenada)
    

def test ():
    l = alt_function()
    r = obj_function([0.02, 0.8, 1.5, 0.5, 0.92])
    print(f'valores: {l}')
    print(f'error: {r}')


best_alt_solution()
# test()
# h_solution()

