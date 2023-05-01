import os
from datetime import datetime
import csv
import dotenv
from dataconn import DBConn


dotenv.load_dotenv()

db = DBConn(os.getenv('POSTGRES_PASS'))
db.init_db()

# Abre o arquivo CSV com os dados dos sensores
with open('data_sensores.csv', 'r',encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # Percorre as linhas do arquivo CSV
    for row in reader:
        # Insere a medição no banco de dados
        db.insert_sensor([row])

# Abre o arquivo CSV com os dados das medições
with open('data_medicoes.csv', 'r',encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # Percorre as linhas do arquivo CSV
    for row in reader:
        # Converte a string da data e hora em um objeto datetime
        row['ts'] = datetime.strptime(row['ts'], '%Y-%m-%d %H:%M:%S')
        # Insere a medição no banco de dados
        db.insert_medicao([row])

# Obtém os 10 maiores valores do Termômetro
res = db.select_data(
    'SELECT * FROM medicoes WHERE sensor_id=1 ORDER BY valor DESC LIMIT 10')
for data in res:
    print(data)
