import pandas as pd
import numpy as np

# 1. Carregar os dados da Etapa 02
print("1/3 Carregando arquivos da Etapa 2...")
df_resumo = pd.read_csv('02_resumo_semanal.csv', sep=';', decimal=',', encoding='utf-8-sig')
df_detalhado = pd.read_csv('02_dados_detalhados.csv', sep=';', decimal=',', encoding='utf-8-sig')

# 2. Definir os limites corretos dos intervalos de dias e os rótulos dos 6 estados (s0 a s5)
# s0: [0.0, 2.5) | s1: [2.5, 3.0) | s2: [3.0, 3.5) | s3: [3.5, 4.0) | s4: [4.0, 4.5) | s5: [4.5, inf)
limites = [0.0, 2.5, 3.0, 3.5, 4.0, 4.5, np.inf]
rotulos = ['s0', 's1', 's2', 's3', 's4', 's5']

# 3. Categorizar a média semanal nos estados de Markov
print("2/3 Categorizando as medias semanais nos estados de Markov...")
df_resumo['estado'] = pd.cut(
    df_resumo['media_tempo_espera'], 
    bins=limites, 
    labels=rotulos, 
    right=False
)

# Mapear o estado também na tabela detalhada
df_detalhado['estado'] = pd.cut(
    df_detalhado['media_por_semana'], 
    bins=limites, 
    labels=rotulos, 
    right=False
)

# 4. Exportar os novos arquivos da Etapa 03
print("3/3 Salvando 03_resumo_com_estados.csv e 03_dados_detalhados_com_estados.csv...")
df_resumo.to_csv('03_resumo_com_estados.csv', sep=';', decimal=',', index=False, encoding='utf-8-sig')
df_detalhado.to_csv('03_dados_com_estados.csv', sep=';', decimal=',', index=False, encoding='utf-8-sig')

# 5. Exibir o resumo da distribuição dos estados no terminal
print("\n Etapa 3 Concluida com sucesso!")
print("Arquivos gerados: '03_resumo_com_estados.csv' e '03_dados_com_estados.csv'")
print("\n--- Frequencia de Semanas por Estado de Congestionamento ---")
print(df_resumo['estado'].value_counts().sort_index())