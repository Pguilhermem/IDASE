import pandas as pd

# Define os parâmetros da função read_csv
params = {
    'filepath_or_buffer': 'dados.csv',
    'sep': ',',
    'header': 0,
    'names': ['datahora', 'temp', 'umid', 'press'],
    'index_col': 'datahora',
    'usecols': ['datahora', 'temp', 'umid', 'press'],
    'skiprows': [0, 1, 2],
    'dtype': {'temp': 'float32', 'umid': 'float32'}
}

# Importa os dados do arquivo CSV para um DataFrame
df = pd.read_csv(**params)

# Trata os dados NaN
df_interpolado = df.interpolate(method='linear')

# Exporta os dados do dataframe para um arquivo csv
df_interpolado.to_csv('df_interpolado.csv', index=True)
