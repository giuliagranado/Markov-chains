# ⛴️ Modelagem do Tempo de Espera dos Navios no Porto de Santos

Este repositório reúne materiais e códigos relacionados ao projeto de **Iniciação Científica (PIBICT)** desenvolvido na FATEC Rubens Lara, que tem como objetivo **Modelar o Tempo de espera dos Navios para Atracação no Porto de Santos utilizando Cadeias de Markov e Teoria de Filas**. Versão em inglês - [here](https://github.com/giuliagranado/Markov-chains/edit/main/README_english.md)

---

## 📌 Objetivo
Construir um modelo estocástico capaz de representar o processo de atracação dos navios, estimando:
- Probabilidades de transição entre estados (chegada, espera, atracação e saída).
- Tempo médio de espera dos navios.
- Gargalos operacionais no fluxo portuário.

---

## 🛠️ Metodologia
1. **Revisão bibliográfica** sobre logística portuária, Cadeias de Markov e Teoria de Filas.  
2. **Coleta de dados** oficiais da ANTAQ e da Autoridade Portuária de Santos.  
3. **Construção da matriz de transição** e definição dos estados do sistema.  
4. **Implementação em Python** utilizando:
   - NumPy
   - Pandas
   - Matplotlib  
5. **Simulações computacionais** para validar o modelo e analisar cenários.  

---

## 📊 Resultados Esperados
- Modelo computacional replicável em Python.  
- Estimativas do tempo médio de espera e taxa de ocupação dos berços.  
- Visualizações gráficas para análise de desempenho.  
- Contribuição acadêmica com artigos e apresentações em eventos científicos.  

---

## 📂 Estrutura do Repositório
- `data/` → Conjunto de dados 
- `analise exploratoria` → graficos da analise  
- `src/` → Scripts Python para modelagem e cálculos  (futuramente)
- `docs/` → Documentos relacionados ao projeto.  

---

## 🚀 Status
🔹 Projeto em fase inicial de desenvolvimento.  
🔹 Próximos passos: finalizar analise exploratoria e construção da matriz de transição.  

---

## 👩‍💻 Autoria
- **Aluno(a):** Giulia Dias Granado de Marques  
- **Orientador:** Prof. Dr. João Paulo Ferreira de Mello  
- **Instituição:** FATEC Rubens Lara – CEETEPS  

---

## 📖 Referências
- ANTAQ – Estatísticos Aquaviários (2024)  
- Ferreira (2025) – Estudo básico das Cadeias de Markov  
- Rodrigues (2020) – Introdução à Teoria das Filas  
