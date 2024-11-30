import numpy as np

# Definición de los datos
X = np.array([1, 2, 3, 4, 5, 6, 7])
Y = np.array([1.0000, 1.2599, 1.4422, 1.5874, 1.7100, 1.8171, 1.9129])
x_interp = 3.5  # Punto a interpolar

# Función de interpolación de Lagrange
def lagrange_interpolation(X, Y, x_interp):
    n = len(X)
    L = 0  # Inicialización del resultado
    for i in range(n):
        term = Y[i]  # Valor inicial de cada término
        for j in range(n):
            if i != j:
                term *= (x_interp - X[j]) / (X[i] - X[j])
        L += term  # Sumar el término al resultado total
    return L

# Calcular el valor interpolado
resultado = lagrange_interpolation(X, Y, x_interp)

# Mostrar el resultado con más precisión
print(f"El valor interpolado en x = {x_interp:.1f} es: {resultado:.10f}")
