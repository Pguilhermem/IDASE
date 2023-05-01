"""
Arquivo exemplo do uso do módulo mongodbhandler
Autor: prof. Guilherme Márcio Soares
Instituição: UFJF
"""
from datetime import datetime
from bson.objectid import ObjectId
from mongodbhandler import MongoDBHandler


db_handler = MongoDBHandler("mongodb://localhost:27017/")

# Inserção de documentos na coleção
data = datetime.now()
doc1 = {"ts": data, "temperatura": 400.0,
        "pressao": 36450.0, "umidade": 33.0, "consumo": 62.0}
doc2 = {"ts": data, "temperatura": 401.0,
        "pressao": 35635.0, "umidade": 32.0, "consumo": 65.0}
doc3 = {"ts": data, "temperatura": 402.0,
        "pressao": 38965.0, "umidade": 31.0, "consumo": 78.0}
db_handler.insert_data([doc1, doc2, doc3])

# Busca de documentos com filtro de data e hora
db_handler.search_data("23/06/2022 10:22:45", "23/06/2022 10:25:53")

# Atualização de um documento
filtro = {"_id": ObjectId('6447402222f1417c592f0b5b')}
novo_valor = {"$set": {"temperatura": 129}}
db_handler.update_data(filtro, novo_valor)
db_handler.search_data("23/06/2022 10:22:45", "23/06/2022 10:25:53")

# Remoção de um documento
query = {"ts": datetime.strptime(
    "23/06/2022 13:22:50.903", "%d/%m/%Y %H:%M:%S.%f")}
db_handler.delete_data(query)
db_handler.search_data("23/06/2022 10:22:45", "23/06/2022 10:22:53")
