import pandas as pd
import requests
import logging


class DadosClimaticos:
    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    def load_data_new_data(self) -> pd.DataFrame:
        response = requests.get(self.url)
        response.raise_for_status()
        return pd.DataFrame(pd.json_normalize(
            response.json()), columns=['dt', 'name', 'main.temp', 'wind.speed', 'main.pressure'])

    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df.rename(columns={'dt': 'timestamp', 'name': 'cidade', 'main.temp': 'temperatura',
                           'wind.speed': 'velocidade_do_vento', 'main.pressure': "pressao"}, inplace=True)
        df['temperatura'] = df['temperatura'].apply(
            lambda x: x-273.15)
        df['timestamp'] = pd.to_datetime(
            df['timestamp'], unit='s', utc=True).dt.tz_convert('America/Sao_Paulo').dt.tz_localize(None)
        return df

    def store_data(self, nd: pd.DataFrame) -> None:
        try:
            dados_historicos = pd.read_csv(
                'dados_climaticos.csv')
            dados_historicos['timestamp'] = pd.to_datetime(
                dados_historicos['timestamp'], format='%d/%m/%Y %H:%M:%S')
            nd = nd.reindex(
                columns=dados_historicos.columns, fill_value=None)
            dados_historicos.loc[len(
                dados_historicos)] = nd.values[0]
        except FileNotFoundError:
            dados_historicos = nd
        except Exception as _e:
            logging.exception(f"Erro ao armazenar os dados: {_e}")
        finally:
            dados_historicos = dados_historicos.drop_duplicates()
            dados_historicos.to_csv('dados_climaticos.csv',
                                    index=False, date_format='%d/%m/%Y %H:%M:%S', float_format='%.2f')

    def update_data(self):
        novo_df = self.load_data_new_data()
        transf_df = self.transform_data(novo_df)
        self.store_data(transf_df)
