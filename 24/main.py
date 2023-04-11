import pandas as pd
import matplotlib.pyplot as plt

# Criando um dicionário de dados
dados = {'Vendas': [35000, 45000, 12000, 18000],
         'Produtos': ['Produto A', 'Produto B', 'Produto C', 'Produto D']}

# Criando o DataFrame a partir do dicionário
df = pd.DataFrame(dados)

# Configurando o índice do DataFrame
df = df.set_index('Produtos')
print(df)
# Plotando um gráfico de pizza
df.plot.pie(y='Vendas', figsize=(5, 5), autopct='%1.1f%%')

# Exibindo o gráfico
plt.show()
