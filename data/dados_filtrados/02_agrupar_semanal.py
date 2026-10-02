import pandas as pd 
# a funçao groupby().transform('mean') será peça chave p o grupo de 7 dias e mapear a média de tempo de espera em cada linha

# 1. Carregar os dados filtrados da Etapa 01 
df = pd.read_csv('01_Dados_semOutliers.csv', sep=';', decimal=',', encoding='utf-8-sig')
df['Data da Chegada'] = pd.to_datetime(df['Data da Chegada'], dayfirst=True)  # converter p formato datetime
df = df.sort_values(by='Data da Chegada').reset_index(drop=True) 

# 2. Fixar a primeira data em 01/01/2024
primeira_data = pd.to_datetime('01/01/2024', dayfirst=True) 

# 3. Criar a Coluna R ('numero_semana') 
df['numero_semana'] = ((df['Data da Chegada'] - primeira_data).dt.days // 7) + 1

# 4. Criar a Coluna 'media_por_semana'-> Média semanal repetida em cada registro (tab. principal)
df['media_por_semana'] = df.groupby('numero_semana')['Duracao_dias'].transform('mean').round(2) 

# 5. Criar a Tabela Resumida (1 linha por semana) 
print("Gerando tabela resumo semanal...") 
df_resumo = df.groupby('numero_semana').agg(
     data_inicio=('Data da Chegada', 'min'), 
     data_fim=('Data da Chegada', 'max'), 
     qtd_navios=('Duracao_dias', 'count'), 
     media_tempo_espera=('Duracao_dias', 'mean') 
).reset_index()

# Arredondar a média e formatar as datas da aba resumida 
df_resumo['media_tempo_espera'] = df_resumo['media_tempo_espera'].round(2)
df_resumo['data_inicio'] = df_resumo['data_inicio'].dt.strftime('%d/%m/%Y') 
df_resumo['data_fim'] = df_resumo['data_fim'].dt.strftime('%d/%m/%Y')

# 6. Salvar os dois arquivos CSV formatados para o Excel
# detalhado 
df.to_csv('02_Dados_detalhados.csv', sep=';', decimal=',', index=False, encoding='utf-8-sig') 
# resumo semanal 
df_resumo.to_csv('02_resumo_semanal.csv', sep=';', decimal=',', index=False, encoding='utf-8-sig')

# 7. Exibir resumo no terminal 
print("\n Etapa 2 Concluida com sucesso!")
print(f"Total de semanas processadas: {len(df_resumo)} semanas.") 
print("\n--- Primeiras 5 Semanas (Visao Resumida) ---") 
print(df_resumo.head())