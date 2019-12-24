# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as bs

html = uo('https://finance.yahoo.com/quote/NEM?p=NEM&.tsrc=fin-srch')
read= bs(html.read(),'html.parser')
MarketCap= read.find('td', {'data-test':'MARKET_CAP-value'})


print(MarketCap.get_text())

print("Hello World")
