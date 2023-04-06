import pandas as pd

xpaths = ['/root/row',
          '/root/row[1]',
          '/root/row[cidade="Rio de Janeiro"]',
          '/root/row[idade >= 25]']

for x in xpaths:
    df = pd.read_xml('dadospessoas.xml', xpath=x)
    print("=============================")
    print(df)

df = pd.read_xml('dados.xml')
df.set_index('timestamp')
df = df.interpolate('linear')
df.to_xml('dadostratados.xml', index=False)
