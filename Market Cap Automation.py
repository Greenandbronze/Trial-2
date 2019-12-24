# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as bs
import pandas as pd
import xlrd as xl

#Opens Excel Workbook with Ticker Symbol List
Workbook=xl.open_workbook('Ticker_List.xlsx')
Worksheet= Workbook.sheet_by_index(0)

#Find Number of Rows in the Sheet
Total_Rows=Worksheet.nrows
print(Total_Rows)

#Loop through Total Rows
def loop_through_excel (Start_Row, Total_Rows):
    for row_cursor in range (Start_Row,Total_Rows):
        Ticker_Symbol= Worksheet.cell(row_cursor,0).value
        print (Ticker_Symbol)
    return 
#Loop Variables
Start_Row= 1

#Call Ticker Loop
Ticker_Found= loop_through_excel(Start_Row, Total_Rows)

#Creates Panda with Ticker Symbols and Names from an Excel Spreadsheet.
Ticker_List= 'Ticker_List.xlsx'
Tickers= pd.read_excel(Ticker_List,
                       header=0,
                       index_col=False,
                       keep_default_na=True)

#Searches, Parses, and then locates Market Cap from Yahoo Finance.
html = uo('https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL')
# html = uo('https://finance.yahoo.com/quote/'+ Ticker_Symbol + '/key-statistics?p=' + Ticker_Symbol + "'")
read= bs(html.read(),'html.parser')
MarketCap= read.find('td', {'class':'Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)'})

print(MarketCap.get_text())
#Prints Top 5 Dataframe results and Market Cap from Yahoo Finance.
print(Tickers.head())
