import random
# Definindo uma função geradora que retorna amostras em tempo real
def gerador_amostras():
    while True:
        # Simulando uma variação aleatória na grandeza monitorada
        sample = random.gauss(50, 10)
        yield sample

# Definindo uma rotina de validação que determina se uma amostra é válida
def validador_amostras(sample):
    # Determinando se a amostra está dentro de um intervalo de tolerância
    if abs(sample - 50) <= 10:
        return True
    else:
        return False

# Criando um objeto gerador a partir da função
sample_values = gerador_amostras()

# Usando um loop for para gerar 10 amostras e avaliar a qualidade de cada amostra
for i in range(10):
    # Obtendo a próxima amostra do gerador
    sample = next(sample_values)
    # Avaliando a qualidade da amostra usando a rotina de validação
    if validador_amostras(sample):
        print(f"Amostra {i+1}: {sample:.2f} - Válida")
    else:
        print(f"Amostra {i+1}: {sample:.2f} - Inválida")