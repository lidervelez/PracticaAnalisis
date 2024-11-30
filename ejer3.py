# Definir la función
def f(x):
    return x**(1/3) - 2  # Equivalente a nthroot(x, 3) en Octave

# Intervalo inicial [a, b]
a = 0
b = 10000

# Tolerancia
tol = 0.0001

# Inicialización de la iteración
iteraciones = 0

while (b - a) / 2 > tol:
    iteraciones += 1
    
    # Calcular el punto medio
    c = (a + b) / 2
    
    # Evaluar la función en el punto medio
    fc = f(c)
    
    # Comprobar si c es una raíz o si se ha alcanzado la tolerancia
    if fc == 0 or (b - a) / 2 < tol:
        break
    
    # Decidir qué subintervalo tomar
    if f(a) * fc > 0:
        a = c
    else:
        b = c

# Mostrar resultados
print(f"La raíz aproximada es: {c:.5f}")
print(f"Número de iteraciones: {iteraciones}")
