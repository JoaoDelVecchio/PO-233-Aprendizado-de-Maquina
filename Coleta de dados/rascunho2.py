import pandas as pd
import csv
import io
import re

def __main__():
    input_string = """
        Income Statement

        2009 Y
        2010 Y
        2011 Y
        2012 Y
        2013 Y
        2014 Y
        2015 Y
        2016 Y
        2017 Y
        2018 Y
        2019 Y
        2020 Y
        2021 Y
        2022 Y
        2023 Y
        TTM
        2023 Q1
        2023 Q2
        2023 Q3
        2023 Q4
        Sales & Services Revenue
        21,599
        29,361
        30,594
        24,643
        30,782
        32,469
        33,263
        32,711
        35,852
        37,714
        39,045
        45,828
        56,414
        50,210
        50,667
        premium
        premium
        premium
        premium
        premium
    """
    """# Use StringIO para criar um objeto de arquivo a partir da string
    input_file = io.StringIO(input_string)
    # Use a biblioteca csv para ler o arquivo
    reader = csv.reader(input_file)
    print(input_string)
    # Ignore as primeiras 23 linhas
    for _ in range(23):
        next(reader)"""


    with open('arquivo.txt', 'r') as file:
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
        for line in file:
            # Incrementa o contador de linha
            line_count += 1
            # Ignora as primeiras 24 linhas
            if line_count <= 23:
                continue

            elif 23 < line_count <= 43:
                line = line.strip()
                line = line.replace(',', '')
                if line == "premium" or line == "-":
                    processed_lines1.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines1.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines1.append(line)

            elif 44 < line_count <= 64:
                line = line.strip()
                line = line.replace(',', '')
                if line == "premium" or line == "-":
                    processed_lines2.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines2.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines2.append(line)
            
            elif 65 < line_count <= 85:
                line = line.strip()
                line = line.replace(',', '')
                if line == "premium" or line == "-":
                    processed_lines3.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines3.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines3.append(line)

            elif 86 < line_count <= 106:
                line = line.strip()
                line = line.replace(',', '')
                if line == "premium" or line == "-":
                    processed_lines4.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines4.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines4.append(line)
            
    # print(processed_lines)




    data = {
        "Year": ["2009 Y", "2010 Y", "2011 Y", "2012 Y", "2013 Y", "2014 Y", "2015 Y", "2016 Y", "2017 Y", "2018 Y", "2019 Y", "2020 Y", "2021 Y", "2022 Y", "2023 Y", "TTM", "2023 Q1", "2023 Q2", "2023 Q3", "2023 Q4"],
        "Sales & Services Revenue": processed_lines1,
        "Cost of Revenue": processed_lines2,
        "Gross Profit": processed_lines3,
        "Selling, General & Admin": processed_lines4
    }

    #print(data)
    df = pd.DataFrame(data)
    
    df = df[~df.apply(lambda row: row.astype(str).str.contains('premium').any(), axis=1)]

    df.to_csv('df.csv', index=False)

    print(df)

__main__()




"""
"Cost of Revenue":
        "Gross Profit":
        "Selling, General & Admin":
        "Research & Development":
        "Operating Income (Loss)":
        "Non-Operating (Income) Loss":
        "Pretax Income":
        "Income (Loss) from Cont Ops":
        "Basic Weighted Avg Shares":
        "Basic EPS, GAAP":
        "Diluted Weighted Avg Shares":
        "Diluted EPS, GAAP":
        "EBITDA":
        "EBITDA Margin (%)":
        "EBITA":
        "EBIT":
        "Gross Margin (%)":
        "Operating Margin (%)":
        "Profit Margin (%)": 
        "Sales per Employee": 
        "Depreciation Expense": 
"""