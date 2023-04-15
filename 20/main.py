import pandas as pd

df1 = pd.DataFrame({'coluna_comum': ['A', 'B', 'C'], 'valor1': [1, 2, 3]})
df2 = pd.DataFrame({'coluna_comum': ['B', 'C', 'D'], 'valor2': [4, 5, 6]})

df_merged_left = pd.merge(df1, df2, on='coluna_comum', how='left')
print("============Merge Left=============\r\n", df_merged_left)
df_merged_right = pd.merge(df1, df2, on='coluna_comum', how='right')
print("============Merge Right=============\r\n", df_merged_right)
df_merged_inner = pd.merge(df1, df2, on='coluna_comum', how='inner')
print("============Merge Inner=============\r\n", df_merged_inner)
df_merged_outer = pd.merge(df1, df2, on='coluna_comum', how='outer')
print("============Merge Outer=============\r\n", df_merged_outer)
