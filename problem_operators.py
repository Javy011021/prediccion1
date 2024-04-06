import random
from decimal import Decimal

STEP = 0.01
MIN_VALUE=-1
MAX_VALUE=1

def exact_add(*nbs):
    return float(sum([Decimal(str(nb)) for nb in nbs]))

def get_decimal_digits(number):
    parts = str(number).split('.')
    decimal_digits_count = len(parts[1]) if len(parts) > 0 else 0
    return decimal_digits_count

def round_to_nearest_multiple(number, multiple=STEP, min_value=MIN_VALUE, max_value=MAX_VALUE):
    rounded_num = round(number / multiple) * multiple
    if min_value is not None and rounded_num < min_value:
        while rounded_num < min_value:
            rounded_num += multiple
    
    if max_value is not None and rounded_num > max_value:
        while rounded_num > max_value:
            rounded_num -= multiple
    
    return round(rounded_num, get_decimal_digits(STEP))

def random_value(min: float = MIN_VALUE, max: float = MAX_VALUE, intv: int = STEP):
    return float(f'{round(random.uniform(min, max) / intv) * intv:.3f}')

# MUTATION. The value of a random position is randomly changed
def change_one(solution, MIN_VALUE=MIN_VALUE, MAX_VALUE=MAX_VALUE): 
    random_index = random.randint(0, len(solution) - 1)
    solution[random_index] = random_value(min=MIN_VALUE, max=MAX_VALUE)
    return solution

# MUTATION. Reverse the subsequence between pos1 and pos2
def reverse_mutation(solution):
    pos1 = random.randint(0, len(solution) - 1)
    pos2 = random.randint(0, len(solution) - 1)
    while pos1 == pos2:
        pos2 = random.randint(0, len(solution) - 1)

    if pos1 > pos2:
        pos1, pos2 = pos2, pos1

    solution[pos1:pos2 + 1] = reversed(solution[pos1:pos2 + 1])
    return solution

# MUTATION. The value of a random position  por la normal
def gaussian_mutation_2(solution, mean=0, std_dev=0.1):
    
    mutated_solution = solution.copy()
    index1, index2 = random.sample(range(len(mutated_solution)), 2)    
    g1 = round_to_nearest_multiple(random.gauss(mean, std_dev))
    g2 = round_to_nearest_multiple(random.gauss(mean, std_dev))
    
    mutated_solution[index1] = exact_add(g1, mutated_solution[index1])
    mutated_solution[index2] = exact_add(g2, mutated_solution[index2])
        
    return mutated_solution

# CROSSOVER. Reverse the subsequence between pos1 and pos2
def simple_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)    
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child
