import random

data = {'dia': 23, '5anteriores': [45,20,38,25,32]}

def alt_function(min: int = 0, max: int = 1, intv: int = 0.2):
    return format(round(random.uniform(min, max) / intv) * intv, '.2f')


def obj_function( dia_actual: int, dias_ant: [], vals: []):
    print(alt_function())
    
    # predict = 0
    # for i in range(len(dias_ant)):
    #     predict += dia_actual[i]*vals[i]

    # return dia_actual - predict

for i in range(10):
    obj_function(1,[],[])