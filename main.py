import random
import numpy as np

ITERATIONS = 100
DAYS = [23, 24, 25]
PAST_DAYS = [
    [45, 20, 38, 25, 32],
    [46, 21, 39, 26, 33],
    [47, 22, 40, 27, 34]
]

def alt_function(min: float = 0, max: float = 1, num_vals: int = 5):
    return [float(f'{random.uniform(min, max):.2f}') for _ in range(num_vals)]


def obj_function(currentDay: int, pastDays: [], vals: []):
    error = 0
    predict = 0
    for i in range(len(pastDays)):
        predict += pastDays[i] * vals[i]
    error = (currentDay - predict) ** 2
    return error

def gradient(currentDay, pastDays, vals):
    m = len(pastDays)
    gradient_vals = np.zeros(m)

    predict = np.dot(pastDays, vals)
    error = currentDay - predict

    for i in range(m):
        gradient_vals[i] = -2 * error * pastDays[i]

    return gradient_vals

def gradient_descent(currentDay, pastDays, vals, learning_rate=0.0001):
    vals = np.array(vals)

    for _ in range(ITERATIONS):
        grad = gradient(currentDay, pastDays, vals)
        vals = vals - learning_rate * grad

    return vals.tolist()

def heuristica_variabilidad(lluvia_real, vals_generados):
    # Calcular la variabilidad de la lluvia
    variabilidad_lluvia = max(lluvia_real) - min(lluvia_real)

    # Asignar valores de K en función de la variabilidad
    k_asignados = [val * variabilidad_lluvia for val in vals_generados]

    return k_asignados

def heuristica_ordena_k(lluvia_real, vals_generados):
    # Ordenar los datos de lluvia y asignar los valores generados en el mismo orden
    lluvia_ordenada = sorted(lluvia_real)
    k_asignados = sorted(vals_generados)

    return k_asignados

# Generar valores de k para una sola instancia
original_vals = alt_function()
print("Valores originales: ", original_vals)

# Aplicar heurística para obtener valores de k para las 3 instancias
k_for_3_instances = heuristica_variabilidad(DAYS, original_vals)

# Imprimir valores de k para las 3 instancias
print("Valores de k para las 3 instancias: ", k_for_3_instances)

# Optimizar valores de k para todas las instancias
optimized_vals = gradient_descent(DAYS[0], PAST_DAYS[0], original_vals)

# Iterar sobre las instancias
for i, current_day in enumerate(DAYS):
    past_days = PAST_DAYS[i]

    print(f"\nInstancia {i + 1}:")
    result = obj_function(current_day, past_days, original_vals)
    print("Error con valores sin optimizar: ", result)

    print("Valores optimizados:", optimized_vals)

    optimzed_result = obj_function(current_day, past_days, optimized_vals)
    print("Error con valores optimizados: ", optimzed_result)
