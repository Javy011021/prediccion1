import random
import math

# ----------------------------------------------------------------------
# initializers
# ----------------------------------------------------------------------

def random_list(LIST_LENGTH=10, MIN_VALUE=0, MAX_VALUE=10, INTEGER=True):
    lista = [0] * LIST_LENGTH
    for i in range(LIST_LENGTH):
        if INTEGER:
            lista[i] = random.randint(MIN_VALUE, MAX_VALUE)
        else:
            lista[i] = MIN_VALUE + random.random()*(MAX_VALUE-MIN_VALUE)
    return lista

def random_permutation(LIST_LENGTH=10):
    a = [i for i in range(LIST_LENGTH)]
    b = [0] * LIST_LENGTH
    for i in range(LIST_LENGTH):
        pos = random.randint(0, len(a)-1)
        b[i] = a[pos]
        a.remove(b[i])
    return b

# ----------------------------------------------------------------------
# operators
# ----------------------------------------------------------------------

def change1(solution, MIN_VALUE=0, MAX_VALUE=10, INTEGER=True): # the value of a random position is randomly changed
    l = len(solution)
    pos1 = random.randint(0, l - 1)
    if INTEGER:
        solution[pos1] = random.randint(MIN_VALUE, MAX_VALUE)
    else:
        solution[pos1] = MIN_VALUE + random.random() * (MAX_VALUE - MIN_VALUE)
    return solution

def add1(solution, MIN_VALUE=0, MAX_VALUE=10, INTEGER=True): # the value of a position is randomly change +-1
    l = len(solution)
    pos1 = random.randint(0, l - 1)
    if INTEGER:
        if solution[pos1] == MIN_VALUE:
            solution[pos1] += 1
        elif solution[pos1] == MAX_VALUE:
            solution[pos1] -= 1
        else:
            if random.random() >= 0.5:
                solution[pos1] += 1
            else:
                solution[pos1] -= 1
    else:
        solution[pos1] = solution[pos1] + 2*(random.random()-0.5)
        while (solution[pos1]>MAX_VALUE) or (solution[pos1]<MIN_VALUE):
            solution[pos1] = solution[pos1] + 2*(random.random()-0.5)
    return solution

def add1all(solution, MIN_VALUE=0, MAX_VALUE=10, INTEGER=True): # the value of all positions is randomly change +-1
    l = len(solution)
    for pos1 in range(l):
        if INTEGER:
            if solution[pos1] == MIN_VALUE:
                solution[pos1] += 1
            elif solution[pos1] == MAX_VALUE:
                solution[pos1] -= 1
            else:
                if random.random() >= 0.5:
                    solution[pos1] += 1
                else:
                    solution[pos1] -= 1
        else:
            solution[pos1] = solution[pos1] + 2*(random.random()-0.5)
            while (solution[pos1]>MAX_VALUE) or (solution[pos1]<MIN_VALUE):
                solution[pos1] = solution[pos1] + 2*(random.random()-0.5)
    return solution

def random_change_for_lists(solution, MIN_VALUE=0, MAX_VALUE=10, INTEGER=True):
    r = random.random()
    if r>= 0.66:
        # print('change1')
        solution =  change1(solution, MIN_VALUE, MAX_VALUE,INTEGER)
    elif r>= 0.33:
        # print('add1')
        solution = add1(solution, MIN_VALUE, MAX_VALUE, INTEGER)
    else:
        # print('add1all')
        solution = add1all(solution, MIN_VALUE, MAX_VALUE, INTEGER)
    return solution

'''
MIN_VALUE = 0
MAX_VALUE = 10
LIST_LENGTH = 4
INTEGER = False
sol =  random_list(LIST_LENGTH,MIN_VALUE,MAX_VALUE,INTEGER)
for i in range(10):
    #print(2*(random.random()-0.5))
    print(sol)
    sol = random_change_for_lists(sol,MIN_VALUE,MAX_VALUE,INTEGER)
'''

def interchange(solution): # the values in two positions is interchanged
    l = len(solution)
    pos1 = random.randint(0, l - 1)
    pos2 = random.randint(0, l - 1)
    v = solution[pos1]
    solution[pos1] = solution[pos2]
    solution[pos2] = v
    return solution

def uniform_crossover(solution, solutionAlt): # each value is chosen randomly from any of the solutions
    l = len(solution)
    for i in range(0, len(solution)):
        if random.randint(0, l):
            solution[i] = solutionAlt[i]
    return solution

def ox_crossover(solution, solutionAlt): # OX crossover for permutation. A random section from one solution and the order values from the other solution
    size = len(solution)
    start, end = sorted([random.randint(0, size - 1) for _ in range(2)])
    new_solution = [-1] * size
    new_solution[start:end + 1] = solution[start:end + 1]
    to_add=[]
    for gene in solutionAlt: # get the values in solutionAlt not yet in new_solution
        if gene not in new_solution:
            to_add.append(gene)
    pos_to_add=0
    for i, v in enumerate(new_solution):
        if v == -1:
            new_solution[i] = to_add[pos_to_add]
            pos_to_add+=1
    return new_solution

# ----------------------------------------------------------------------
# for exhaustive search
# ----------------------------------------------------------------------

def first_list(LIST_LENGTH=10, MIN_VALUE=0, MAX_VALUE=10):
    number= LIST_LENGTH
    solution= [MIN_VALUE for i in range(number)]
    return solution

def next_list(solution,LIST_LENGTH=10, MIN_VALUE=0, MAX_VALUE=10, INTEGER=True, resolution=10):
    # resolution : steps between MIN_VALUE and MAX_VALUE
    number = LIST_LENGTH
    j= number-1
    while (solution[j]==MAX_VALUE) and j>=0:
        j-=1
    if j==-1:
        solution = first_list(number)
    else:
        if INTEGER:
            solution[j]+=1
            for j in range(j+1,number):
                solution[j]=MIN_VALUE
        else: # imposible exhaustive searh with infinite not integer... an approximation with steps
            step = (MAX_VALUE-MIN_VALUE)/ resolution
            solution[j]+=step
            if solution[j]>MAX_VALUE:
                solution[j] = MAX_VALUE
            for j in range(j+1,number):
                solution[j]=MIN_VALUE
    return solution

def first_permutation(LIST_LENGTH=10):
    number= LIST_LENGTH
    solution= [i for i in range(number)]
    return solution

def next_permutation(solution,LIST_LENGTH=10):
    number= LIST_LENGTH
    # go backward to find the first value that is smaller than the next (pair of consecutive values in ascending order)
    # take the elements after this value and sort them
    # place the first of these element that is greater than the value and place it in the position of the value
    # put the rest of these elements and the value after this position, in ascending order
    end_list=[]
    j= number-1
    end_list.append(solution[j])
    while (solution[j-1]>=solution[j])and(j>0):
        j-=1
        end_list.append(solution[j])
    if j==0:
        solution=first_permutation(number)
    else:
        end_list.sort()
        k=0
        while solution[j-1] >= end_list[k]:
            k += 1
        tmp = solution[j-1]
        solution[j-1] = end_list[k]
        end_list[k] = tmp
        shft = j
        for i in range(j,number):
            solution[i]=end_list[i-shft]
    return solution