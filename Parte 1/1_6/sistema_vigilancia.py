import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    filename='system_log.txt'
)


def gerador_lotes(dados, tamanho_lote):
    """
    Geração de lotes de dados para processamentos parciais
    :param dados: lista de dicionários contendo os dados
    : tamanho_lote: tamanho dos lotes gerados
    """
    for i in range(0, len(dados), tamanho_lote):
        lote = dados[i:i+tamanho_lote]
        yield lote


def detectar_padroes(lotes):
    """
    Buscar de padrões suspeitos nos lotes
    :param lotes: lotes a serem processados
    """
    for lote in lotes:
        padroes_suspeitos = filter(
            lambda dado: dado["temperatura"] > 23 and dado["movimento"], lote)
        for padrao in padroes_suspeitos:
            yield padrao


def imprimir_dados(padroes_suspeitos):
    """
    Gravação de resultados
    :param padrões suspeitos
    """
    for padrao_suspeito in padroes_suspeitos:
        logging.warning(f"Padrao suspeito detectado: {padrao_suspeito}")


def medir_tempo_de_execucao(func):
    """
    Decorador para medição de tempo
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(
            f"Tempo gasto para executar o programa: {end_time - start_time:.6f} segundos")
        return result
    return wrapper
