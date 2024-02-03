import random
import numpy as np

data = {'day': 23, '5pastDays': [45,20,38,25,32]}

def alt_function(min: float = 0, max: float = 1, num_vals: int = 5):
    return [float(f'{random.uniform(min, max):.2f}') for _ in range(num_vals)]


def obj_function( currentDay: int, pastDays: [], vals: []):
    error = 0
    predict = 0
    for i in range(len(pastDays)):
        predict += pastDays[i]*vals[i]
    error = (currentDay-predict) ** 2 
    return error

def gradient(currentDay, pastDays, vals):
    m = len(pastDays)
    gradient_vals = np.zeros(m)
    
    predict = np.dot(pastDays, vals)
    error = currentDay - predict
    
    for i in range(m):
        gradient_vals[i] = -2 * error * pastDays[i]
    
    return gradient_vals

def gradient_descent(currentDay, pastDays, vals, learning_rate=0.0001, num_iterations=1000):
    vals = np.array(vals)
    
    for _ in range(num_iterations):
        grad = gradient(currentDay, pastDays, vals)
        vals = vals - learning_rate * grad
    
    return vals.tolist()

vals = alt_function()
print("Valores originales: ", vals)

result = obj_function(23, [45,20,38,25,32], vals)

print("Error con valores sin optimizar: ",result)

optimized_vals = gradient_descent(23,[45,20,38,25,32], vals)

print("Valores optimizados", optimized_vals)

optimzed_result = obj_function(23,[45,20,38,25,32],optimized_vals)

print("Error con valores optimizados: ", optimzed_result)
