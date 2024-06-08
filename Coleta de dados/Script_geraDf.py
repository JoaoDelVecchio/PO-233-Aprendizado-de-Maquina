import pandas as pd
import csv
import io
import re

def __main__():

    with open('entrada.txt', 'r') as file:
        line_count = 0
        processed_lines = []
        processed_lines1 = []
        processed_lines2 = []
        processed_lines3 = []
        processed_lines4 = []
        processed_lines5 = []
        processed_lines6 = []
        processed_lines7 = []
        processed_lines8 = []
        processed_lines9 = []
        processed_lines10 = []
        processed_lines11 = []
        processed_lines12 = []
        processed_lines13 = []
        processed_lines14 = []
        processed_lines15 = []
        processed_lines16 = []
        processed_lines17 = []
        processed_lines18 = []
        processed_lines19 = []
        processed_lines20 = []
        processed_lines21 = []
        processed_lines22 = []
        processed_lines23 = []

        for line in file:
            # Incrementa o contador de linha
            line_count += 1
            # Ignora as primeiras 18 linhas
            if line_count <= 18:
                continue

            # para as próximas 40 linhas (da 24 até a 43 inclusive) ele vai transformar
            # os dados em uma linha da minha tabela, removendo a ','; transformando a linha em um inteiro;
            # caso contrario a linha vai como string
            # logo, locais sem valor são considerados como ' - - '
            # LEMBRE DE CADA VEZ QUE COPIAR ESSE PASSO MUDAR O NOMDE DE processed_linesX
            elif 19 < line_count <= 33:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines1.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines1.append(float(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines1.append(line)

            # agora basta repetir o processo em 20 e 20 linhas;

            elif 35 < line_count <= 49:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines2.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines2.append(float(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines2.append(line)
            
            elif 51 < line_count <= 65:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines3.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines3.append(float(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines3.append(line)

            elif 67 < line_count <= 81:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines4.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines4.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines4.append(line)

            elif 83 < line_count <= 97:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines5.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines5.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines5.append(line)
            
            elif 99 < line_count <= 113:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines6.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines6.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines6.append(line)
            
            elif 115 < line_count <= 129:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines7.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines7.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines7.append(line)
            
            elif 131 < line_count <= 145:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines8.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines8.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines8.append(line)

            elif 147 < line_count <= 161:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines9.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines9.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines9.append(line)
                        
            elif 163 < line_count <= 177:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines10.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines10.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines10.append(line)
            
            elif 179 < line_count <= 193:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines11.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines11.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines11.append(line)
                        
            elif 195 < line_count <= 209:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines12.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines12.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines12.append(line)
                        
            elif 211 < line_count <= 225:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines13.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines13.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines13.append(line)
                        
            elif 227 < line_count <= 241:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines14.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines14.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines14.append(line)
                        
            elif 243 < line_count <= 257:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines15.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines15.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines15.append(line)
                        
            elif 259 < line_count <= 273:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines16.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines16.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines16.append(line)
                        
            elif 275 < line_count <= 289:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines17.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines17.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines17.append(line)
                        
            elif 291 < line_count <= 305:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines18.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines18.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines18.append(line)
                        
            elif 307 < line_count <= 321:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines19.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines19.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines19.append(line)
                        
            elif 323 < line_count <= 337:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines20.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines20.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines20.append(line)
                        
            elif 339 < line_count <= 353:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines21.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines21.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines21.append(line)

                  
            elif 355 < line_count <= 369:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines22.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines22.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines22.append(line)
                        
            elif 371 < line_count <= 385:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines23.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines23.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines23.append(line)

            

    data = {
        "Year": ["2010 Y", "2011 Y", "2012 Y", "2013 Y", "2014 Y", "2015 Y", "2016 Y", "2017 Y", "2018 Y", "2019 Y", "2020 Y", "2021 Y", "2022 Y",
                  "2023 Y"],
        "Sales & Services Revenue": processed_lines1,
        "Cost of Revenue": processed_lines2,
        "Gross Profit": processed_lines3,
        "Selling, General & Admin": processed_lines4,
        "Research & Development": processed_lines5,
        "Operating Income (Loss)": processed_lines6,
        "Non-Operating (Income) Loss": processed_lines7,
        "Pretax Income": processed_lines8,
        "Income (Loss) from Cont Ops": processed_lines9,
        "Basic Weighted Avg Shares": processed_lines10,
        "Basic EPS, GAAP": processed_lines11,
        "Diluted Weighted Avg Shares": processed_lines12,
        "Diluted EPS, GAAP": processed_lines13,
        "EBITDA": processed_lines14,
        "EBITDA Margin (%)": processed_lines15,
        "EBITA": processed_lines16,
        "EBIT": processed_lines17,
        "Gross Margin (%)": processed_lines18,
        "Operating Margin (%)": processed_lines19,
        "Profit Margin (%)": processed_lines20,
        "Sales per Employee": processed_lines21,
        "Dividend per Share": processed_lines22,
        "Depreciation Expense": processed_lines23
    }
    print(data)
    # transformar a tabela anterior em um dataframe por meio da biblioteca pandas
    df = pd.DataFrame(data)
    # eliminando todas as linhas que possuem um elemento escrito "Premium"
    df = df[~df.apply(lambda row: row.astype(str).str.contains('premium').any(), axis=1)]
    # Transformar esse dataFrame em um .csv
    df.to_csv('DATA_.csv', index=False)


    print(df)

__main__()




