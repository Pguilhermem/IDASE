import pandas as pd

# Importa os dados do arquivo do Excel para um dicionário de dataframes
tipos = ['records', 'index', 'columns', 'split', 'values']

for tipo in tipos:
    df = pd.read_json(f"{tipo}.json", orient=tipo)
    print(f"====================={tipo}=======================")
    print(df)


df = pd.read_json('dados.json', convert_dates=False)
df.iloc[:, 1:4] = df.iloc[:, 1:4].interpolate("linear")
df.to_json('dadostratados.json', orient='records')
