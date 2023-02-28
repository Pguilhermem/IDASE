import os
import multiprocessing
import cv2

class ProcessamentoImagens:
    def __init__(self, diretorio_entrada, diretorio_saida, num_processos=4):
        self.diretorio_saida = diretorio_saida
        self.diretorio_entrada = diretorio_entrada
         # Lista os arquivos do diretório de entrada
        self.arquivos = [f for f in os.listdir(self.diretorio_entrada)]

        self.num_processos = num_processos
        #Cria a fila
        self.fila = multiprocessing.Queue()
        self.infos = {"num_imgs":len(self.arquivos),"erros":[]}

    def processa_imagem(self, path_img): #Realiza a detecção de faces com um classificador pré-treinado
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

    def processa_lote(self, fila):
        lote = fila.get()
        for img in lote:
            self.processa_imagem(img)

    def inicia_processamento(self):
        # Divide a lista de arquivos em lotes e coloca na fila
        tamanho_lote = int(len(self.arquivos) / self.num_processos) + 1
        for i in range(0, len(self.arquivos), tamanho_lote):
            self.fila.put(self.arquivos[i:i+tamanho_lote])
        
        # Inicia os processos
        processos = []
        for i in range(self.num_processos):
            p = multiprocessing.Process(target=self.processa_lote, args=(self.fila,))
            p.start()
            processos.append(p)

        # Finaliza os processos
        for p in processos:
            p.join()

        # Retorna o arquivo com informações do processamento
        return self.infos