import time

# Função lambda para converter os dados em um formato padrão
padronizar_dados = lambda dados: {"id": dados["id"], "temperatura": dados["temperatura"], "movimento": dados["movimento"]}

# Iterador para processar os dados em lotes e gerar dados de saída intermediários
def processar_dados(dados, tamanho_lote):
    for i in range(0, len(dados), tamanho_lote):
        lote = dados[i:i+tamanho_lote]
        saida = [padronizar_dados(dado) for dado in lote]
        yield saida

# Gerador para filtrar os dados intermediários e detectar padrões suspeitos
def detectar_padroes(dados):
    for lote in dados:
        padroes_suspeitos = filter(lambda dado: dado["temperatura"] > 23 and dado["movimento"], lote)
        for padrao in padroes_suspeitos:
            yield padrao

# Decorador para medir o tempo de execução do programa
def medir_tempo_de_execucao(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
        return result
    return wrapper

# Impressão do resultado na tela
def imprimir_dados(dados):
        for dado in dados:
            print(f"{dado}\n")

