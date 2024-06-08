import pandas as pd
import csv
import io
import re

def __main__():

    data = {
    "Year": ["2010 Y", "2011 Y", "2012 Y", "2013 Y", "2014 Y", "2015 Y", "2016 Y", "2017 Y", "2018 Y", "2019 Y", "2020 Y", "2021 Y", "2022 Y", "2023 Y"],
    "Sales & Services Revenue": [], "Cost of Revenue": [], "Gross Profit": [], "Selling, General & Admin": [], "Research & Development": [], "Operating Income (Loss)": [],
    "Non-Operating (Income) Loss": [], "Pretax Income": [], "Income (Loss) from Cont Ops": [], "Basic Weighted Avg Shares": [], "Basic EPS, GAAP": [], "Diluted Weighted Avg Shares": [],
    "Diluted EPS, GAAP": [], "EBITDA": [], "EBITDA Margin (%)": [], "EBITA": [], "EBIT": [], "Gross Margin (%)": [], "Operating Margin (%)": [], "Profit Margin (%)": [], 
    "Sales per Employee": [], "Dividend per Share": [], "Depreciation Expense": [], "Cash, Cash Equivalents & STI": [], "Cash & Cash Equivalents": [], "Accounts & Notes Receiv": [],
    "Inventories": [], "Other ST Assets": [], "Total Current Assets": [], "Property, Plant & Equip, Net": [], "Property, Plant & Equip": [], "LT Investments & Receivables": [],
    "Other LT Assets": [], "Total Noncurrent Assets": [], "Total Assets": [], "Payables & Accruals": [], "ST Debt": [], "Other ST Liabilities": [], "Total Current Liabilities": [],
    "LT Debt": [], "Other LT Liabilities": [], "Total Noncurrent Liabilities": [], "Total Liabilities": [], "Share Capital & APIC": [], "Common Stock": [], "Retained Earnings": [],
    "Other Equity": [], "Equity Before Minority Interest": [], "Total Equity": [], "Total Liabilities & Equity": [], "Shares Outstanding": [], "Net Debt": [], "Net Debt to Equity": [],
    "Tangible Common Equity Ratio": [], "Current Ratio": [], "Cash Conversion Cycle": [], "Number of Employees": [], "Net Income": [], "Depreciation & Amortization": [], 
    "Non-Cash Items": [], "Stock-Based Compensation": [], "Chg in Non-Cash Work Cap": [], "Cash from Operating Activities": [], "Acq of Fixed & Intang": [], 
    "Net Change in LT Investment": [], "Cash from Investing Activities": [], "Dividends Paid": [], "Cash From Debt": [], "Cash (Repurchase) of Equity": [], 
    "Cash from Financing Activities": [], "Net Changes in Cash": [], "Capital Expenditures": [], "EBITDA": [], "EBITDA Margin (%)": [], "Free Cash Flow": [], 
    "Price/Free Cash Flow": [], "Cash Flow to Net Income": []
    }

    def process_line(line, processed_lines):
        line = line.strip().replace('%', '').replace('.', '').replace(',', '.')
        if line == "premium" or line == "-":
            processed_lines.append(line)
        else:
            try:
                processed_lines.append(int(line))
            except ValueError:
                processed_lines.append(line)

    with open('entrada.txt', 'r') as file:
        lines = file.readlines()

    processed_lines = {
        range(0, 14): data["Sales & Services Revenue"],
        range(16, 30): data["Cost of Revenue"],
        range(32, 46): data["Gross Profit"],
        range(48, 62): data["Selling, General & Admin"],
        range(64, 78): data["Research & Development"],
        range(80, 94): data["Operating Income (Loss)"],
        range(96, 110): data["Non-Operating (Income) Loss"],
        range(112, 126): data["Pretax Income"],
        range(128, 142): data["Income (Loss) from Cont Ops"],
        range(144, 158): data["Basic Weighted Avg Shares"],
        range(160, 174): data["Basic EPS, GAAP"],
        range(176, 190): data["Diluted Weighted Avg Shares"],
        range(192, 206): data["Diluted EPS, GAAP"],
        range(208, 222): data["EBITDA"],
        range(224, 238): data["EBITDA Margin (%)"],
        range(240, 254): data["EBITA"],
        range(256, 270): data["EBIT"],
        range(272, 286): data["Gross Margin (%)"],
        range(288, 302): data["Operating Margin (%)"],
        range(304, 318): data["Profit Margin (%)"],
        range(320, 334): data["Sales per Employee"],
        range(336, 350): data["Dividend per Share"],
        range(352, 366): data["Depreciation Expense"],
        range(368, 382): data["Cash, Cash Equivalents & STI"],
        range(384, 398): data["Cash & Cash Equivalents"],
        range(400, 414): data["Accounts & Notes Receiv"],
        range(416, 430): data["Inventories"],
        range(432, 446): data["Other ST Assets"],
        range(448, 462): data["Total Current Assets"],
        range(464, 478): data["Property, Plant & Equip, Net"],
        range(480, 494): data["Property, Plant & Equip"],
        range(496, 510): data["LT Investments & Receivables"],
        range(512, 526): data["Other LT Assets"],
        range(528, 542): data["Total Noncurrent Assets"],
        range(544, 558): data["Total Assets"],
        range(560, 574): data["Payables & Accruals"],
        range(576, 590): data["ST Debt"],
        range(592, 606): data["Other ST Liabilities"],
        range(608, 622): data["Total Current Liabilities"],
        range(624, 638): data["LT Debt"],
        range(640, 654): data["Other LT Liabilities"],
        range(656, 670): data["Total Noncurrent Liabilities"],
        range(672, 686): data["Total Liabilities"],
        range(688, 702): data["Share Capital & APIC"],
        range(704, 718): data["Common Stock"],
        range(720, 734): data["Retained Earnings"],
        range(736, 750): data["Other Equity"],
        range(752, 766): data["Equity Before Minority Interest"],
        range(768, 782): data["Total Equity"],
        range(784, 798): data["Total Liabilities & Equity"],
        range(800, 814): data["Shares Outstanding"],
        range(816, 830): data["Net Debt"],
        range(832, 846): data["Net Debt to Equity"],
        range(848, 862): data["Tangible Common Equity Ratio"],
        range(864, 878): data["Current Ratio"],
        range(880, 894): data["Cash Conversion Cycle"],
        range(896, 910): data["Number of Employees"],
        range(912, 926): data["Net Income"],
        range(928, 942): data["Depreciation & Amortization"],
        range(944, 958): data["Non-Cash Items"],
        range(960, 974): data["Stock-Based Compensation"],
        range(976, 990): data["Chg in Non-Cash Work Cap"],
        range(992, 1006): data["Cash from Operating Activities"],
        range(1008, 1022): data["Acq of Fixed & Intang"],
        range(1024, 1038): data["Net Change in LT Investment"],
        range(1040, 1054): data["Cash from Investing Activities"],
        range(1056, 1070): data["Dividends Paid"],
        range(1072, 1086): data["Cash From Debt"],
        range(1088, 1102): data["Cash (Repurchase) of Equity"],
        range(1104, 1118): data["Cash from Financing Activities"],
        range(1120, 1134): data["Net Changes in Cash"],
        range(1136, 1150): data["Capital Expenditures"],
        range(1152, 1166): data["EBITDA"],
        range(1168, 1182): data["EBITDA Margin (%)"],
        range(1184, 1198): data["Free Cash Flow"],
        range(1200, 1214): data["Price/Free Cash Flow"],
        range(1216, 1230): data["Cash Flow to Net Income"]
    }

    for line_count, line in enumerate(lines, start=1):
        for line_range, processed_lines_list in processed_lines.items():
            if line_count in line_range:
                process_line(line, processed_lines_list)
                break

    # Now the `data` dictionary is filled with the processed data.

    print(data)
    # transformar a tabela anterior em um dataframe por meio da biblioteca pandas
    df = pd.DataFrame(data)
    # eliminando todas as linhas que possuem um elemento escrito "Premium"
    df = df[~df.apply(lambda row: row.astype(str).str.contains('premium').any(), axis=1)]
    # Transformar esse dataFrame em um .csv
    df.to_csv('DATA_ABT.csv', index=False)


    print(df)

__main__()
