import numpy as np

# Lendo o arquivo CSV de temperaturas
temperaturas = np.genfromtxt(
    'temperaturas.csv', delimiter=',', skip_header=1, usecols=range(1, 13))

print(temperaturas)

# Indexação para obter os dados de temperaturas de uma cidade específica
cidade1 = temperaturas[0, :]

print(f"Temperaturas da cidade 1: {cidade1}")

print(f"Temperaturas da cidade 1 no primeiro semestre: {cidade1[0:6]}")

# Calculando a média de temperaturas em cada cidade
media_cidade = np.mean(temperaturas, axis=1)

# Encontrando as cidades com as temperaturas mais altas e mais baixas
cidade_mais_quente = np.argmax(media_cidade)
cidade_mais_fria = np.argmin(media_cidade)

# Comparando as temperaturas em duas cidades diferentes (linhas 2 e 5)
comparacao = temperaturas[1, :] - temperaturas[4, :]

# Imprimindo os resultados
print("Média de temperaturas em cada cidade:")
print(media_cidade)
print("Cidade mais quente:", cidade_mais_quente)
print("Cidade mais fria:", cidade_mais_fria)
print("Comparação de temperaturas entre duas cidades:")
print(comparacao)
