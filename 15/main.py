import pandas as pd

# Define os parâmetros da função read_csv
params = {
    'filepath_or_buffer': 'dados.csv',
    'sep': ',',
    'names': ['datahora', 'temp', 'umid', 'press'],
    'index_col': 'datahora',
    'usecols': ['datahora', 'temp', 'umid', 'press'],
    'skiprows': [0, 1],
    'dtype': {'temp': 'float32', 'umid': 'float32'},
    'parse_dates': ['datahora']
}

# Importa os dados do arquivo CSV para um DataFrame
df = pd.read_csv(**params)
print(df)
df.to_clipboard()
# Tratar os valores NaN
df_interpolado = df.interpolate(method='linear')

# Exportar arquivo tratado
df_interpolado.to_csv('df_interpolado.csv', index=True,
                      date_format='%d/%m/%Y %H:%M:%S')
