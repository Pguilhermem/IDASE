import pandas as pd

df = pd.read_csv('parametros_coleta_imagens.csv')

print("============== Estatísticas Descritivas do DataFrame ===============\r\n", df.describe())

print("============== Matriz de Correlação ===============\r\n", df.corr())

mean = df['Qualidade da Imagem'].mean()
std = df['Qualidade da Imagem'].std()

outliers = (df['Qualidade da Imagem'] > mean + 2 *
            std) | (df['Qualidade da Imagem'] < mean - 2*std)
n_outliers = outliers.sum()

print("============== Quantidade de amostras com valores fora da média +- desvio padrão ===============\r\n", n_outliers)
