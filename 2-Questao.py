import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_excel('/home/denilso-oliveira/Documents/Estatistica/table_estatistica.xlsx',)
df = pd.read_csv('/home/denilso-oliveira/Documents/Estatistica/result_inmet.CSV', encoding='utf-8')


df['Data'] = pd.to_datetime(df['Data'], format='%Y/%m/%d')


df_precip = df.groupby('Data')['PRECIPITACAO TOTAL'].sum()

plt.figure(figsize=(12, 6))
plt.plot(df_precip.index, df_precip.values, marker='', linestyle='-', color='r')
plt.title('Série Histórica de Precipitação em Maceió')
plt.xlabel('Data')
plt.ylabel('Precipitação Total (mm)')
plt.grid(True)
plt.show()


# Para apresentar a série histórica de precipitação em Maceió, eu escolhi o  o gráfico de linha, 
# pois ele é eficaz para mostrar como a precipitação varia ao longo do tempo, permitindo observar tendências 
# e padrões sazonais.