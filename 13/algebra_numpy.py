import numpy as np

# Criando uma matriz
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Transpondo uma matriz
matriz_transposta = matriz.transpose()  # ou matriz.T

# Multiplicando matrizes
matriz_multiplicada = np.dot(matriz, matriz_transposta)

# Resolvendo um sistema de equações lineares
a = np.array([[2, 3], [4, 5]])
b = np.array([8, 13])
x = np.linalg.solve(a, b)

matriz2 = np.array([[1, 20, 3], [4, 5, 6], [72, 8, 9]])
# Calculando autovalores e autovetores
autovalores, autovetores = np.linalg.eig(matriz2)

# Cálculo do determinante
det = np.linalg.det(matriz2)

# Cálculo da inversa
matriz2_inv = np.linalg.inv(matriz2)

# Imprimindo os resultados
print("Matriz:")
print(matriz)
print("Matriz transposta:")
print(matriz_transposta)
print("Matriz multiplicada:")
print(matriz_multiplicada)
print("Solução do sistema de equações lineares:")
print(x)

print("Matriz 2")
print(matriz2)
print("Autovalores da matriz 2:")
print(autovalores)
print("Autovetores da matriz 2:")
print(autovetores)
print("Determinante da matriz 2:")
print(det)
print("Inversa da matriz 2:")
print(matriz2_inv)
