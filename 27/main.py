from datetime import datetime
import pymongo
import pytz
from bson.objectid import ObjectId

# Conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["database"]
collection = db["data"]

# Criação da coleção
# collection = db.create_collection("mycollection")

# Inserção de documentos na coleção
data = datetime.now()
doc1 = {"ts": data, "temperatura": 400.0,
        "pressao": 36450.0, "umidade": 33.0, "consumo": 62.0}
doc2 = {"ts": data, "temperatura": 401.0,
        "pressao": 35635.0, "umidade": 32.0, "consumo": 65.0}
doc3 = {"ts": data, "temperatura": 402.0,
        "pressao": 38965.0, "umidade": 31.0, "consumo": 78.0}
collection.insert_many([doc1, doc2, doc3])

# Busca de documentos com filtro de data e hora


def busca_dados(inicio, fim):
    local_tz = pytz.timezone('America/Sao_Paulo')
    utc_tz = pytz.timezone('UTC')
    inicio_local = local_tz.localize(
        datetime.strptime(inicio, '%d/%m/%Y %H:%M:%S'))
    fim_local = local_tz.localize(datetime.strptime(fim, '%d/%m/%Y %H:%M:%S'))
    inicio_utc = inicio_local.astimezone(utc_tz)
    fim_utc = fim_local.astimezone(utc_tz)
    query = {"ts": {"$gte": inicio_utc, "$lte": fim_utc}}
    result = collection.find(query)
    for doc in result:
        ts_utc = utc_tz.localize(doc['ts'])
        ts_local = ts_utc.astimezone(local_tz)
        hora_local = ts_local.strftime('%d/%m/%Y %H:%M:%S')
        print(
            f"_id: {doc['_id']}| Timestamp:{hora_local} | Temperatura: {doc['temperatura']}")


busca_dados("23/06/2022 10:22:45", "23/06/2022 10:25:53")

# Atualização de um documento
filtro = {"_id": ObjectId('6447402222f1417c592f0b5d')}
novo_valor = {"$set": {"temperatura": 129}}
print(collection.update_one(filtro, novo_valor))
busca_dados("23/06/2022 10:22:45", "23/06/2022 10:25:53")

# Remoção de um documento
query = {"ts": datetime.strptime("23/06/2022 13:22:52.947", "%d/%m/%Y %H:%M:%S.%f")}
collection.delete_one(query)
busca_dados("23/06/2022 10:22:45", "23/06/2022 10:25:53")