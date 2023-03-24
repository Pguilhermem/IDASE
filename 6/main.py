import json
from sistema_vigilancia import sistema_vigilancia

arquivo_dados = open('dados.json')
dados_sensores = json.load(arquivo_dados)
arquivo_dados.close()

sistema_vigilancia(dados_sensores)
