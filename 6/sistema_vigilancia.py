import logging
from time import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    filename='system_log.txt'
)


def medir_tempo_execucao(func):
    """
    Decorador para medir tempo de execução
    """
    def wrapper(*args, **kwargs):
        tempo_inicial = time()
        result = func(*args, **kwargs)
        tempo_exec = time() - tempo_inicial
        logging.info(
            f"Tempo gasto para a execucao do programa: {tempo_exec:.7f} segundos.")
        return result
    return wrapper


def gerador_lotes(dados, tamanho_lote):
    """
    Geração de lotes dados para processamentos parciais
    : param dados: lista de dicionários contando os dados
    : tamanho_lote: tamanho dos lotes gerados
    """
    for i in range(0, len(dados), tamanho_lote):
        lote = dados[i:i+tamanho_lote]
        yield lote


def detectar_padroes_suspeitos(lotes):
    """
    Busca de padrões suspeitos nos lotes
    :param lotes: iterador para os lotes de dados a serem processados
    """
    for lote in lotes:
        padroes_suspeitos = filter(
            lambda dado: dado["temperatura"] > 23 and dado["movimento"], lote)
        for padrao in padroes_suspeitos:
            yield padrao


def registrar_eventos(padroes_suspeitos):
    """
    Registro de eventos
    : param padroes_suspeitos: iterador para os padrões suspeitos
    """
    for padrao in padroes_suspeitos:
        logging.warning(f"Padrao suspeito detectado: {padrao}")


@medir_tempo_execucao
def sistema_vigilancia(dados):
    """
    Função que encapsula todas as funcionalidades do sistema de vigilância
    :param dados: lista de dicionários com os dados de entrada do sistema
    """
    lotes = gerador_lotes(dados, 2)
    padroes_suspeito = detectar_padroes_suspeitos(lotes)
    registrar_eventos(padroes_suspeito)
