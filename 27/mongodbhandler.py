"""
Módulo mongodbhandler
Autor: prof. Guilherme Márcio Soares
Instituição: UFJF
"""
from datetime import datetime
import pymongo
import pytz


class MongoDBHandler:
    """
    Classe Mongo_DBHandler
    """

    def __init__(self, database_url):
        """
        Inicializa uma conexão com o banco de dados MongoDB.

        :param database_url: URL de conexão com o banco de dados.
        """
        self.client = pymongo.MongoClient(database_url)
        self._db = self.client["database"]
        self.collection = self._db["data"]

    def insert_data(self, data):
        """
        Insere dados na coleção 'data' do banco de dados.

        :param data: lista de dicionários com os valores a serem inseridos na coleção.
        """
        self.collection.insert_many(data)

    def search_data(self, inicio, fim):
        """
        Realiza uma busca na coleção 'data' do banco de dados.

        :param inicio: string contendo a data/hora de início da busca no formato 'dd/mm/yyyy HH:MM:SS'.
        :param fim: string contendo a data/hora de término da busca no formato 'dd/mm/yyyy HH:MM:SS'.
        """
        local_tz = pytz.timezone('America/Sao_Paulo')
        utc_tz = pytz.timezone('UTC')
        inicio_local = local_tz.localize(
            datetime.strptime(inicio, '%d/%m/%Y %H:%M:%S'))
        fim_local = local_tz.localize(
            datetime.strptime(fim, '%d/%m/%Y %H:%M:%S'))
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
        """
        Atualiza um registro na coleção 'data' do banco de dados.

        :param filtro: dicionário contendo o filtro para identificar o registro a ser atualizado.
        :param novo_valor: dicionário contendo os novos valores a serem atribuídos ao registro.
        """
        self.collection.update_one(filtro, novo_valor)

    def delete_data(self, query):
        """
        Remove um registro da coleção 'data' do banco de dados.

        :param query: dicionário contendo o filtro para identificar o registro a ser removido.
        """
        self.collection.delete_one(query)
