import pandas as pd
import yfinance as yf
import datetime as datetime

def __main__():

    with open('C:\\Users\\delve\\OneDrive\\Eu\\GitHub\\PO-233-Aprendizado-de-Maquina\\Coleta de dados\\Entradas\\entrada_ABT.txt', 'r') as file:
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
        processed_lines24 = []
        processed_lines25 = []
        processed_lines26 = []
        processed_lines27 = []
        processed_lines28 = []
        processed_lines29 = []
        processed_lines30 = []
        processed_lines31 = []
        processed_lines32 = []
        processed_lines33 = []
        processed_lines34 = []
        processed_lines35 = []
        processed_lines36 = []
        processed_lines37 = []
        processed_lines38 = []
        processed_lines39 = []
        processed_lines40 = []
        processed_lines41 = []
        processed_lines42 = []
        processed_lines43 = []
        processed_lines44 = []
        processed_lines45 = []
        processed_lines46 = []
        processed_lines47 = []
        processed_lines48 = []
        processed_lines49 = []
        processed_lines50 = []
        processed_lines51 = []
        processed_lines52 = []
        processed_lines53 = []
        processed_lines54 = []
        processed_lines55 = []
        processed_lines56 = []
        processed_lines57 = []
        processed_lines58 = []
        processed_lines59 = []
        processed_lines60 = []
        processed_lines61 = []
        processed_lines62 = []
        processed_lines63 = []
        processed_lines64 = []
        processed_lines65 = []
        processed_lines66 = []
        processed_lines67 = []
        processed_lines68 = []
        processed_lines69 = []
        processed_lines70 = []
        processed_lines71 = []
        processed_lines72 = []
        processed_lines73 = []
        processed_lines74 = []
        processed_lines75 = []
        processed_lines76 = []
        processed_lines77 = []
        processed_lines78 = []
        processed_lines79 = []

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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                line = line.replace('.', '')
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
                        
            elif 404 < line_count <= 418:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines24.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines24.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines24.append(line)
                        
            elif 420 < line_count <= 434:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines25.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines25.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines25.append(line)
                        
            elif 436 < line_count <= 450:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines26.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines26.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines26.append(line)
                        
            elif 452 < line_count <= 466:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines27.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines27.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines27.append(line)
                        
            elif 468 < line_count <= 482:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines28.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines28.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines28.append(line)
                        
            elif 484 < line_count <= 498:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines29.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines29.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines29.append(line)
                        
            elif 500 < line_count <= 514:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines30.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines30.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines30.append(line)
                        
            elif 516 < line_count <= 530:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines31.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines31.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines31.append(line)
                        
            elif 532 < line_count <= 546:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines32.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines32.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines32.append(line)
                        
            elif 548 < line_count <= 562:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines33.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines33.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines33.append(line)
                        
            elif 564 < line_count <= 578:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines34.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines34.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines34.append(line)
                        
            elif 580 < line_count <= 594:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines35.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines35.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines35.append(line)
                        
            elif 596 < line_count <=610:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines36.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines36.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines36.append(line)
                        
            elif 612 < line_count <= 626:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines37.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines37.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines37.append(line)
                        
            elif 628 < line_count <= 642:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines38.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines38.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines38.append(line)
                        
            elif 644 < line_count <= 658:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines39.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines39.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines39.append(line)
                        
            elif 660 < line_count <= 674:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines40.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines40.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines40.append(line)
                        
            elif 676 < line_count <= 690:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines41.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines41.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines41.append(line)
                        
            elif 692 < line_count <= 706:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines42.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines42.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines42.append(line)
                        
            elif 708 < line_count <= 722:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines43.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines43.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines43.append(line)
                        
            elif 724 < line_count <= 738:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines44.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines44.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines44.append(line)
                        
            elif 740 < line_count <= 754:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines45.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines45.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines45.append(line)
                        
            elif 756 < line_count <= 770:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines46.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines46.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines46.append(line)
                        
            elif 772 < line_count <= 786:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines47.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines47.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines47.append(line)
                        
            elif 788 < line_count <= 802:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines48.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines48.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines48.append(line)
                        
            elif 804 < line_count <= 818:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines49.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines49.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines49.append(line)
                        
            elif 820 < line_count <= 834:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines50.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines50.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines50.append(line)
                        
            elif 836 < line_count <= 850:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines51.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines51.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines51.append(line)
                        
            elif 852 < line_count <= 866:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines52.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines52.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines52.append(line)
                        
            elif 868 < line_count <= 882:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines53.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines53.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines53.append(line)
                        
            elif 884 < line_count <= 898:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines54.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines54.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines54.append(line)
                        
            elif 900 < line_count <= 914:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines55.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines55.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines55.append(line)
                        
            elif 916 < line_count <= 930:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines56.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines56.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines56.append(line)
                        
            elif 932 < line_count <= 946:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines57.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines57.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines57.append(line)
                     
            elif 965 < line_count <= 979:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines58.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines58.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines58.append(line)
                        
            elif 981 < line_count <= 995:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines59.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines59.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines59.append(line)
                        
            elif 997 < line_count <= 1011:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines60.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines60.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines60.append(line)
                        
            elif 1013 < line_count <= 1027:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines61.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines61.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines61.append(line)
                        
            elif 1029 < line_count <= 1043:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines62.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines62.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines62.append(line)

            elif 1045 < line_count <= 1059:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines63.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines63.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines63.append(line)
                        
            elif 1061 < line_count <= 1075:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines64.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines64.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines64.append(line)
                                    
            elif 1077 < line_count <= 1091:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines65.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines65.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines65.append(line)
                                                
            elif 1093 < line_count <= 1107:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines66.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines66.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines66.append(line)

            elif 1109 < line_count <= 1123:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines67.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines67.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines67.append(line)
            
            elif 1125 < line_count <= 1139:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines68.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines68.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines68.append(line)

            elif 1141 < line_count <= 1155:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines69.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines69.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines69.append(line)
            
            elif 1157 < line_count <= 1171:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines70.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines70.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines70.append(line)

            elif 1173 < line_count <= 1187:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines71.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines71.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines71.append(line)
            
            elif 1189 < line_count <= 1203:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines72.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines72.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines72.append(line)
            
            elif 1205 < line_count <= 1219:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines73.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines73.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines73.append(line)
            
            elif 1221 < line_count <= 1235:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines74.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines74.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines74.append(line)

            elif 1237< line_count <= 1251:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines75.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines75.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines75.append(line)
                        
            elif 1253< line_count <= 1267:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines76.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines76.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines76.append(line)
                        
            elif 1269< line_count <= 1283:
                line = line.strip()
                line = line.replace('%', '')
                line = line.replace('.', '')
                line = line.replace(',', '.')
                if line == "premium" or line == "-":
                    processed_lines77.append(line)
                else:
                    # Tenta converter a linha para um inteiro
                    try:
                        processed_lines77.append(int(line))
                    # Se a conversão falhar, adiciona a linha como uma string
                    except ValueError:
                        processed_lines77.append(line)
                                   

    data = {
        "Year": ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022",
                  "2023"],
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
        "Depreciation Expense": processed_lines23,
        "Cash, Cash Equivalents & STI": processed_lines24,
        "Cash & Cash Equivalents": processed_lines25,
        "Accounts & Notes Receiv": processed_lines26,
        "Inventories": processed_lines27,
        "Other ST Assets": processed_lines28,
        "Total Current Assets":processed_lines29,
        "Property, Plant & Equip, Net":processed_lines30,
        "Property, Plant & Equip": processed_lines31,
        "LT Investments & Receivables": processed_lines32,
        "Other LT Assets": processed_lines33,
        "Total Noncurrent Assets": processed_lines34,
        "Total Assets": processed_lines35,
        "Payables & Accruals":processed_lines36,
        "ST Debt": processed_lines37,
        "Other ST Liabilities": processed_lines38,
        "Total Current Liabilities": processed_lines39,
        "LT Debt": processed_lines40,
        "Other LT Liabilities": processed_lines41,
        "Total Noncurrent Liabilities": processed_lines42,
        "Total Liabilities": processed_lines43,
        "Share Capital & APIC": processed_lines44,
        "Common Stock": processed_lines45,
        "Retained Earnings": processed_lines46,
        "Other Equity": processed_lines47,
        "Equity Before Minority Interest": processed_lines48,
        "Total Equity":processed_lines49,
        "Total Liabilities & Equity": processed_lines50,
        "Shares Outstanding": processed_lines51,
        "Net Debt": processed_lines52,
        "Net Debt to Equity": processed_lines53,
        "Tangible Common Equity Ratio": processed_lines54,
        "Current Ratio": processed_lines55,
        "Cash Conversion Cycle": processed_lines56,
        "Number of Employees": processed_lines57,
        "Net Income": processed_lines58,
        "Depreciation & Amortization":processed_lines59,
        "Non-Cash Items": processed_lines60 ,
        "Stock-Based Compensation": processed_lines61,
        "Chg in Non-Cash Work Cap": processed_lines62,
        "Cash from Operating Activities": processed_lines63,
        "Acq of Fixed & Intang": processed_lines64,
        "Net Change in LT Investment":processed_lines65,
        "Cash from Investing Activities":processed_lines66,
        "Dividends Paid": processed_lines67,
        "Cash From Debt":processed_lines68,
        "Cash (Repurchase) of Equity":processed_lines69,
        "Cash from Financing Activities":processed_lines70,
        "Net Changes in Cash": processed_lines71,
        "Capital Expenditures":processed_lines72,
        "EBITDA":processed_lines73,
        "EBITDA Margin (%)":processed_lines74,
        "Free Cash Flow":processed_lines75,
        "Price/Free Cash Flow":processed_lines76,
        "Cash Flow to Net Income":processed_lines77,

    }
    
    # transformar a tabela anterior em um dataframe por meio da biblioteca pandas
    df = pd.DataFrame(data)

    # eliminando todas as linhas que possuem um elemento escrito "Premium"
    df = df[~df.apply(lambda row: row.astype(str).str.contains('premium').any(), axis=1)]
    df = df.rename(columns={'Year': 'Date'})

    # Baixando os dados de retorno anual do S&P500 dos ultimos 15 anos
    sp500 = yf.Ticker('^GSPC')
    start_date = "2008-01-01"
    end_date = "2024-01-01"
    sp500_hist = sp500.history(start=start_date, end=end_date).resample('YE').last()
    sp500_returns = sp500_hist['Close'].pct_change()

    # Definindo o ticker da empresa que iremos comparar
    ticker = 'ABT'
    company = yf.Ticker(ticker)
    company_hist = company.history(start=start_date, end=end_date).resample('YE').last()
    company_returns = company_hist['Close'].pct_change()

    # Calculando a performance relativa
    performance_relative = company_returns - sp500_returns
    df2 = pd.DataFrame(performance_relative)
    df2.index = df2.index.strftime('%Y')
    df2 = df2.iloc[2:]
    df2 = df2.rename(columns={'Close': 'Performance'})
    df2.to_csv('performance')
    
    # Combinando os dataframes
    df_combined = pd.merge(df, df2, on='Date', how='left')
    columns = [col for col in df_combined.columns if col != 'Performance'] + ['Performance']
    df_combined = df_combined[columns]

    # Salvando arquivo
    df_combined.to_csv('C:\\Users\\delve\\OneDrive\\Eu\\GitHub\\PO-233-Aprendizado-de-Maquina\\Coleta de dados\\Data\\Data_ABT.csv', index = True)

__main__()
