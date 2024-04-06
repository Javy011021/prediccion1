import random
from MHPython.operators import uniform_crossover
from problem_operators import MAX_VALUE, MIN_VALUE, STEP, change_one, exact_add, gaussian_mutation_2, random_value, reverse_mutation, simple_crossover

ITERATIONS = 20

DAYS = [12.32, 8.94, 29.77, 20.14, 27.83, 11.45, 26.68, 16.13, 4.56, 5.73]

PAST_DAYS = [
    [18.05, 19.62, 17.04, 3.13, 23.44],
    [23.07, 12.32, 27.09, 7.23, 8.19],
    [4.16, 14.88, 3.58, 28.55, 29.15],
    [29.71, 22.83, 4.05, 28.56, 27.77],
    [21.35, 10.84, 25.42, 16.79, 16.38],
    [20.21, 24.65, 7.62, 5.87, 6.84],
    [4.59, 21.93, 18.77, 14.73, 4.49],
    [16.87, 3.67, 24.52, 27.15, 20.09],
    [3.12, 1.87, 25.12, 10.43, 6.39],
    [4.25, 0.51, 20.56, 16.77, 29.17]
]

Presentation  = 'Rain Problem'
def present_problem():
    print('---------------------------------------------------------------------------------------------')
    print(Presentation)
    # print(f'LIST_LENGTH = {LIST_LENGTH}, CAPACITY = {CAPACITY}, MAX_VALUE = {MAX_VALUE}, VALUES_RND = {VALUES_RND}')
    # print(f'Profits and sizes of the items = {prof_size}')
    print('---------------------------------------------------------------------------------------------')
    
    
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


# MUTATION
def random_change(solution, MIN_VALUE=MIN_VALUE, MAX_VALUE=MAX_VALUE): 
    random_no = random.random()
    if random_no > 0.67 :
        return change_one(solution, MIN_VALUE=MIN_VALUE, MAX_VALUE=MAX_VALUE)
    elif random_no < 0.33:
        return gaussian_mutation_2(solution)
    else:
        return reverse_mutation(solution)

def not_random_change(solution, interval=0.1):
    changed_solution = [val + interval for val in solution]
    return changed_solution


# CROSSOVER
def random_combination(solution1, solution2):
    random_no = random.random()
    if(random_no > 0.50):
        return uniform_crossover(solution1, solution2)
    else:
        return simple_crossover(solution1, solution2)

#Test Functions
def test ():
    l = random_solution()
    r = obj_function(l)
    print(f'valores: {l}')
    print(f'error: {r}')


# best_alt_solution()
# test()
# heuristic_solution()

