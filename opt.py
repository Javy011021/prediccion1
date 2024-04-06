from scipy.optimize import minimize
import numpy as np

# Nuevos datos
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

def objective_function(coefs):
    # Calculamos la suma de los productos
    sum_products = np.sum([np.dot(coefs, past_day) for past_day in PAST_DAYS], axis=0)
    # Calculamos la diferencia cuadrada entre la suma de los productos y los valores en DAYS
    difference = sum_products - np.array(DAYS)
    # Devolvemos la suma de las diferencias cuadradas
    return np.sum(difference**2)

# Condiciones iniciales para los coeficientes
initial_guess = [1, 1, 1, 1, 1]

# Restricciones para los coeficientes (ninguna)
constraints = []

# Optimizamos la función objetivo
result = minimize(objective_function, initial_guess, constraints=constraints)

# Coeficientes óptimos
optimal_coefs = result.x
print("Coeficientes óptimos:", optimal_coefs)

# Calculamos la suma de los productos con los coeficientes óptimos
sum_products_optimal = np.sum([np.dot(optimal_coefs, past_day) for past_day in PAST_DAYS], axis=0)

print("Suma de productos con coeficientes óptimos:", sum_products_optimal)

# Calculamos la suma de los productos con los coeficientes óptimos
sum_products_optimal = np.sum([np.dot(optimal_coefs, past_day) for past_day in PAST_DAYS], axis=0)

# Calculamos el error
error = np.abs(sum_products_optimal - np.array(DAYS))

print("Error asociado con los coeficientes óptimos:", error)


print('Real error', objective_function(optimal_coefs))
