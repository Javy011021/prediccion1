import random
from decimal import Decimal

STEP = 0.01
MIN_VALUE=-1
MAX_VALUE=1

def exact_add(*nbs):
    return float(sum([Decimal(str(nb)) for nb in nbs]))

def random_value(min: float = MIN_VALUE, max: float = MAX_VALUE, intv: int = STEP):
    return float(f'{round(random.uniform(min, max) / intv) * intv:.2f}')

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



# CROSSOVER. Reverse the subsequence between pos1 and pos2

