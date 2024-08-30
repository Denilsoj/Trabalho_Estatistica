import pandas as pd

# df = pd.read_excel('/home/denilso-oliveira/Documents/Estatistica/table_estatistica.xlsx',)
tb = pd.read_csv('/home/denilso-oliveira/Documents/Estatistica/result_inmet.CSV', encoding='utf-8')


tb_colums_temp = tb[['TEMPERATURA DO AR - BULBO SECO', 
                'TEMPERATURA DO PONTO DE ORVALHO (C)', 
                'TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C)', 
                'TEMPERATURA MINIMA NA HORA ANT. (AUT) (C)', 
                'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (C)', 
                'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (C)']]


tb_media_columns_temp = tb_colums_temp.mean()
tb_mediana_columns_temp = tb_colums_temp.median()
tb_moda_columns_temp = tb_colums_temp.mode().iloc[0]


print('Media das Temperaturas')
print(tb_media_columns_temp)
print('\n')
print('Mediana das temperaturas')
print(tb_mediana_columns_temp)
print('\n')
print('Moda das temperaturas')
print(tb_moda_columns_temp)