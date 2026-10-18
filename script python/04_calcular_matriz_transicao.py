import pandas as pd

# 1. carrega os dados categorizados da Etapa 03
print("1/4 Carregando 03_resumo_com_estados.csv...")
df_resumo = pd.read_csv('03_resumo_com_estados.csv', sep=';', decimal=',', encoding='utf-8-sig')

# garante a ordenação cronológica pelo número da semana
df_resumo = df_resumo.sort_values(by='numero_semana').reset_index(drop=True)

# 2. usa 'estado' como o estado atual (t) e cria 'estado_proximo' para a semana t+1
df_resumo['estado_proximo'] = df_resumo['estado'].shift(-1)

# remove a última linha (a última semana não possui prox p comparar)
df_transicoes = df_resumo.dropna(subset=['estado_proximo']).copy() #descarta a última linha

# lista com todos os rótulos (garante a matriz 6x6 completa)
rotulos = ['s0', 's1', 's2', 's3', 's4', 's5']

# 3. gerar a Matriz de Frequência Absoluta (contagem de mudanças de estado)
print("2/4 Calculando matriz de frequencia de transicao...")
matriz_frequencia = pd.crosstab( #cria tabela 6x6, e conta quantas vzs houve cada uma das transições 
    df_transicoes['estado'],
    df_transicoes['estado_proximo']
).reindex(index=rotulos, columns=rotulos, fill_value=0) #preenche com zero se ñ houver ocorrencia

# 4. calcula a Matriz de Probabilidades de Transição P 
print("3/4 Calculando a Matriz de Probabilidades P...")
matriz_probabilidade = matriz_frequencia.div(
    matriz_frequencia.sum(axis=1), axis=0
).fillna(0).round(4)

# 5. Exportar os dois arquivos CSV
print("4/4 Exportando arquivos CSV...")
matriz_frequencia.to_csv('04_matriz_frequencia.csv', sep=';', decimal=',', encoding='utf-8-sig')
matriz_probabilidade.to_csv('04_matriz_probabilidade_P.csv', sep=';', decimal=',', encoding='utf-8-sig')
df_transicoes.to_csv('04_tabela_transicoes.csv', sep=';', decimal=',', index=False, encoding='utf-8-sig')

print("\nEtapa 4 Concluida com sucesso!")
print("Arquivos gerados: '04_matriz_frequencia.csv',  '04_matriz_probabilidade_P.csv e 04_tabela_transicoes.csv'\n")

print("--- MATRIZ DE PROBABILIDADES DE TRANSICAO (P) ---")
print(matriz_probabilidade)