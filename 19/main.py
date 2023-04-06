from dadosclimaticos import DadosClimaticos
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(filename='erros.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.ERROR)

api_key = os.getenv('API_KEY')
lat = -21.7642
lon = -43.3496

updater = DadosClimaticos(api_key, lat, lon)

updater.update_data()
