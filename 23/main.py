import pandas as pd

df = pd.read_csv('vendas.csv')

print("=============Quantidade média vendida de cada produto ============\r\n",
      df.groupby('Produto')['Quantidade'].mean())

print("=============Quantidade vendida em cada loja ============\r\n",
      df.groupby('Loja')['Quantidade'].sum())

print("============= Preço médio de cada produto ============\r\n",
      df.groupby('Produto')['PreçoUnitário'].mean())

print("============= Preço médio de cada produto por loja ============\r\n",
      df.groupby(['Produto', 'Loja'])['PreçoUnitário'].mean())
