import csv
from pymongo import MongoClient
import bson

# abrir o arquivo CSV e ler o conteúdo em uma variável de string
with open('meu_arquivo.csv', 'r') as f:
    conteudo_csv = f.read()

# obter o cabeçalho e o conteúdo do arquivo CSV
linhas = conteudo_csv.splitlines()
cabecalho = linhas[0]
conteudo = '\n'.join(linhas[1:])

# codificar a string em bytes
conteudo_bytes = conteudo.encode('utf-8')

# criar um novo documento MongoDB e inserir o BLOB e o cabeçalho
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
collection = db['minha_colecao']
doc = {'nome_arquivo': 'meu_arquivo.csv', 'cabecalho': cabecalho,
       'conteudo': bson.Binary(conteudo_bytes)}
collection.insert_one(doc)

# fechar a conexão com o MongoDB
client.close()
