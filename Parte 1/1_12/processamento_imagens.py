import os
import multiprocessing
import cv2

class ProcessamentoImagens:
    """
    Classe responsável por processar imagens em paralelo usando múltiplos processos.

    Atributos:
    ----------
    diretorio_saida : str
        Caminho para o diretório onde as imagens processadas serão salvas.
    diretorio_entrada : str
        Caminho para o diretório onde as imagens a serem processadas estão localizadas.
    num_processos : int
        Número de processos que serão criados para processar as imagens.
    arquivos : list
        Lista de arquivos encontrados no diretório de entrada.
    fila : multiprocessing.Queue
        Fila que armazena os lotes de arquivos a serem processados.
    infos : dict
        Dicionário que armazena informações sobre o processamento, como o número de imagens processadas e erros ocorridos.
    """
    def __init__(self, diretorio_entrada:str, diretorio_saida:str, num_processos:int=4) -> None:
        """
        Inicializa a classe ProcessamentoImagens.

        :param diretorio_entrada: Caminho para o diretório onde as imagens a serem processadas estão localizadas.
        :param diretorio_saida: Caminho para o diretório onde as imagens processadas serão salvas.
        :param num_processos: Número de processos que serão criados para processar as imagens. (padrão: 4)
        """
        self.diretorio_saida = diretorio_saida
        self.diretorio_entrada = diretorio_entrada
        self.arquivos = [f for f in os.listdir(self.diretorio_entrada)]
        self.num_processos = num_processos
        self.fila = multiprocessing.Queue()
        self.infos = {"num_imgs":len(self.arquivos),"erros":[]}

    def processa_imagem(self, path_img:str) -> None:
        """
        Realiza a detecção de faces em uma imagem usando um classificador pré-treinado e salva a imagem com as faces detectadas no diretório de saída.

        :param path_img: Caminho para a imagem a ser processada.
        """
        try:
            imagem = cv2.imread(os.path.join(self.diretorio_entrada, path_img))
            classificador = cv2.CascadeClassifier("multiprocessing_env\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

            cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            faces = classificador.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imwrite(f"{self.diretorio_saida}/{path_img}",imagem)

        except Exception as e:
            self.infos["erros"].append({path_img:e.args})

    def processa_lote(self, fila:multiprocessing.Queue) -> None:
        """
        Processa um lote de imagens da fila.

        :param fila: Fila que armazena os lotes de arquivos a serem processados.
        """
        lote = fila.get()
        for img in lote:
            self.processa_imagem(img)

    def inicia_processamento(self):
        """
        Inicia o processamento das imagens em paralelo usando múltiplos processos.

        :return: Dicionário que armazena informações sobre o processamento, como o número de imagens processadas e erros ocorridos.
        """
        tamanho_lote = int(len(self.arquivos) / self.num_processos) + 1
        for i in range(0, len(self.arquivos), tamanho_lote):
            self.fila.put(self.arquivos[i:i+tamanho_lote])
        
        processos = []
        for i in range(self.num_processos):
            p = multiprocessing.Process(target=self.processa_lote, args=(self.fila,))
            p.start()
            processos.append(p)

        for p in processos:
            p.join()

        return self.infos