from sistema_vigilancia import medir_tempo_de_execucao, gerador_lotes, detectar_padroes, imprimir_dados


# Aplicando o decorador para medir o tempo de execução do programa
@medir_tempo_de_execucao
def sistema_vigilancia(dados_sensores):
    # Carregando dados de sensores de um banco de dados
    dados = dados_sensores

    # Criação de lotes
    lotes = gerador_lotes(dados, 2)

    # Detecção de padrões suspeitos
    padroes_suspeitos = detectar_padroes(lotes)

    # Gravação dos dados de saída
    imprimir_dados(padroes_suspeitos)


# Dados de sensores de exemplo
dados_sensores = [
    {"id": 1, "temperatura": 22.3, "movimento": True},
    {"id": 2, "temperatura": 25.6, "movimento": False},
    {"id": 3, "temperatura": 20.1, "movimento": True},
    {"id": 4, "temperatura": 21.8, "movimento": False},
    {"id": 5, "temperatura": 24.5, "movimento": True},
    {"id": 6, "temperatura": 23.7, "movimento": False},
    {"id": 7, "temperatura": 19.8, "movimento": True},
    {"id": 8, "temperatura": 20.9, "movimento": False},
    {"id": 9, "temperatura": 23.1, "movimento": True},
    {"id": 10, "temperatura": 24.8, "movimento": False},
]

sistema_vigilancia(dados_sensores)
