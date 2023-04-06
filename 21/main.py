import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
# aplicar uma função para calcular o quadrado de cada elemento
s_quadrado = s.map(lambda x: x ** 2)
print("==========map()=============\r\n", s_quadrado)

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]})
# aplicar uma função para calcular a soma de cada linha
df_soma_linhas = df.apply(lambda x: x.sum(), axis=1)
print("==========apply()=============\r\n", df_soma_linhas)

# aplicar uma função para calcular o quadrado de cada elemento do DataFrame
df_quadrado = df.applymap(lambda x: x ** 2)
print("==========applymap()=============\r\n", df_quadrado)
