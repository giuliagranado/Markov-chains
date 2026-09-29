# REMOVENDO OUTLIERS 

import pandas as pd 
import numpy as np

# 1. definir o limite fixo estabelecido pelo estudo
limite_outlier = 17.41

# carregar os dados 
df = pd.read_csv('00_Dados_Modelados.csv', sep=';', decimal=',', encoding='latin1') 

# 2. verificar a quant. total de registros antes do filtro
total_inicial = len(df) 
print(f"Total de atracacoes cadastradas: {total_inicial}")

# 3. sendo a coluna do tempo de espera 'Duracao_dias'
df_limpo = df[df['Duracao_dias'] <= limite_outlier].copy()

# calcular quantos registros foram removidos 
total_filtrado = len(df_limpo) 
removidos = total_inicial - total_filtrado

print(f"Atracacoes mantidas: {total_filtrado}") 
print(f"Outliers removidos (< 17.41 dias): {removidos} ({removidos/total_inicial*100:.2f}%)")

#df_limpo.to_excel('Dados_semOutliers', index=False)
df_limpo.to_csv('02_Dados_semOutliers.csv', sep=';', decimal=',', index=False, encoding='utf-8-sig')
