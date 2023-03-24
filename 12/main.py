from processamento_imagens import ProcessamentoImagens
import time
if __name__ == '__main__':
    inicial = time.perf_counter()
    diretorio_entrada = "faces"
    diretorio_saida = "imagens_processadas"
    num_processos = 2
    processador = ProcessamentoImagens(diretorio_entrada,diretorio_saida, num_processos)
    infos = processador.inicia_processamento()
    if infos["erros"]:
        print("O processamento das seguintes imagens retornaram erros:")
        for e in infos["erros"]:
            print(e)
    else:
        print(f"Processamento de {infos['num_imgs']} imagens concluído com sucesso em {time.perf_counter()-inicial:.2f} segundos!")