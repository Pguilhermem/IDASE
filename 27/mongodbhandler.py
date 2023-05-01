from datetime import datetime
import pymongo
import pytz


class MongoDBHandler:
    def __init__(self, database_url):
        self.client = pymongo.MongoClient(database_url)
        self.db = self.client["database"]
        self.collection = self.db["data"]

    def insert_data(self, data):
        self.collection.insert_many(data)

    def search_data(self, inicio, fim):
        local_tz = pytz.timezone('America/Sao_Paulo')
        utc_tz = pytz.timezone('UTC')
        inicio_local = local_tz.localize(
            datetime.strptime(inicio, '%d/%m/%Y %H:%M:%S'))
        fim_local = local_tz.localize(datetime.strptime(fim, '%d/%m/%Y %H:%M:%S'))
        inicio_utc = inicio_local.astimezone(utc_tz)
        fim_utc = fim_local.astimezone(utc_tz)
        query = {"ts": {"$gte": inicio_utc, "$lte": fim_utc}}
        result = self.collection.find(query)
        for doc in result:
            ts_utc = utc_tz.localize(doc['ts'])
            ts_local = ts_utc.astimezone(local_tz)
            hora_local = ts_local.strftime('%d/%m/%Y %H:%M:%S.%f')
            print(
                f"_id: {doc['_id']}| Timestamp:{hora_local} | Temperatura: {doc['temperatura']}")

    def update_data(self, filtro, novo_valor):
        self.collection.update_one(filtro, novo_valor)

    def delete_data(self, query):
        self.collection.delete_one(query)
