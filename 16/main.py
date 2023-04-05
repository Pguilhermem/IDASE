import pandas as pd
import datetime as dt
# Define os parâmetros da função read_csv
params = {
    'io': 'dados.xlsx',
    'sheet_name': ["Dados2022", "Dados2023"],
    'header': 0,
    'names': ['datahora', 'temp', 'umid', 'press'],
    'usecols': ['datahora', 'temp', 'umid', 'press'],
    'dtype': {'temp': 'float32', 'umid': 'float32'},
    'parse_dates': ['datahora']
}

# Importa os dados do arquivo do Excel para um dicionário de dataframes
dfs = pd.read_excel(**params)

# Exportar o arquivo do excel tratado
with pd.ExcelWriter('dados_tratados.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
    for sheetname, df in dfs.items():
        df['datahora'] = df['datahora'].apply(
            lambda x: dt.datetime.strftime(x, '%d/%m/%Y %H:%M:%S'))
        df = df.interpolate(method='linear')  # Tratar os valores NaN
        df.to_excel(writer, sheet_name=sheetname)
