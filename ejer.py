import numpy as np

def factorizacion_LU(A, b):
    n = A.shape[0]
    if A.shape[1] != n:
        print('La matriz A no es cuadrada.')
        return None
    if len(b) != n:
        print('El vector b no tiene el mismo número de filas que la matriz A.')
        return None

    # Factorización LU
    for i in range(n):
        A[i, i] = A[i, i] - np.dot(A[i, :i], A[:i, i])
        if A[i, i] == 0:
            print('La matriz A no admite factorización LU.')
            return None
        for j in range(i+1, n):
            A[i, j] = A[i, j] - np.dot(A[i, :i], A[:i, j])
        for j in range(i+1, n):
            A[j, i] = 1/A[i, i] * (A[j, i] - np.dot(A[j, :i], A[:i, i]))

    y = solve_for_y(A, b)  # Resolver L * y = b
    x = solve_for_x(A, y)  # Resolver U * x = y
    return x

def solve_for_y(A, b):
    n = A.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= A[i, j] * y[j]
    return y

def solve_for_x(A, y):
    n = A.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i, j] * x[j]
        x[i] = (y[i] - s) / A[i, i]
    return x

# Ejemplo de uso
A = np.array([[1, 4, 9, 16],
              [4, 9, 16, 25],
              [9, 16, 25, 36],
              [16, 25, 36, 49]], float)

b = np.array([30, 54, 86, 126], float)

x = factorizacion_LU(A.copy(), b)  # Copiar A para no modificar el original
print("La solución del sistema es:", x)
