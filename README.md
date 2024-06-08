# PO-233-Aprendizado-de-Maquina
Projeto de aprendizado de máquina

**Bibliotecas  que serão usadas:**
1. numpy as np para linear Algebra
2. datetime as dt para datas
3. yfinance as yf para conseguir os dados financeiros
4. pandas as pd para processamento de dados
5. matplotlib.pyplot as plt
6. seaborn as sns
7. plotly.express as px
8. plotly.graph_objects as go

**To Do**
1. (FEITO) Conseguir um Site ou uma biblioteca do python que me forneça os dados de Financials, Balance Sheet e CashFlow dos últimos 15 anos de cada uma das empresas listadas no S&P500
2. (FEITO) Criar uma Script que, dado um arquivo Txt contendo as informações de cada empresa retiradas por meio de um Crtl C do site do Roic AI, me gere uma tabela chamada Data_XXX em que cada linha dessa tabela seja um ano da empresa, e cada coluna seja o valor do aumento percentual de um determinado indicador daquele ano para o anterior.
3. Dada as tabelas Data Geradas no passo atual, começar primeiro com 10 tabelas e, então, agrupar em cada uma destas a ultima coluna necessária, a qual seria o retorno percentual relativo dessa emrpesa com o índice do S&P500.
4.  Pensar melhor no modelo que iremos escolher antes de pular para a próxima tarefa.
5. Agrupar então cada um desses Dataframes completos em um final: Cada linha corresponde a uma empresa e um ano desta.


**Doing:**

1. Finalmente consegui criar um Script que gere uma tabela para cada empresa dos ultimos 15 anos dos 75 indicadores escolhidos, fiz isso para 10 empresas já


**Done:**
1. Não consegui os indices dos ultimos 15 anos, mas me veio uma ideia, se nosso modelo considerar cada conjunto EMPRESA+ANO como um elemento, mesmo tendo apenas 4 anos nós teríamos 505*5 elementos para considerar, o que já me garante uma base de dados um pouco mais eficiente
2. Não consegui encontrar em nenhuma biblioteca direta para python os dados de Financials, Cash Flow e Balance Income das empresas do S&P500 dos ultimos 15 anos, apenas dos ultimos 5
3. Encontrei um site que disponibiliza, mas o recurso de fazer o download das informações é pago: https://roic.ai/quote/MSFT:US/financials
3. Tentei inicialmente pegar empresa por empresa e mandar o GPT transformar o ctrl C da página em uma tabela em python, mas esse método se mostrou bastante lento, não prátivo e nem otimizado.
4. Estou criando um script em python que dado um ctrl C e ctrl V específico naquele site o python recebe isso como input, transforma em um dataframe e me gera os arquivos csv bonitinhos
5. Acho que uma coisa mais interessante a fazer é pegar a porcentagem de mudança de um ano para o outro
