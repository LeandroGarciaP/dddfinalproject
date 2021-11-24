from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time
from urllib.request import urlopen as uReq
from selenium import webdriver

urls = ['https://www.ogol.com.br/edition_matches.php?id=2491',
        'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=2',
       'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=3',
       'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=4',
       'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=5',
       'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=6',
       'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=7',
       'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=8',
       'https://www.ogol.com.br/edition_matches.php?id_edicao=2491&fase_in&equipa=0&estado=&filtro=&op=calendario&page=9']

dataframes = []
for url in urls:
    browser = webdriver.Chrome('C:\chromedriver.exe')
    browser.get(url)
    time.sleep(3)
    browser.refresh()
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')
    time.sleep(5)
    browser.close()
    gdp = soup.find_all("table", attrs={"class": "zztable stats"})
    table1 = gdp[0]
    body = table1.find_all("tr")
    head = body[0]
    body_rows = body[1:]
    headings = []
    for item in head.find_all("th"): # loop through all th elements
        # convert the th elements to text and strip "\n"
        item = (item.text).rstrip("\n")
        # append the clean column name to headings
        headings.append(item)

    all_rows = [] # will be a list for list for all rows
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            # row_item.text removes the tags from the entries
            # the following regex is to remove \xa0 and \n and comma from row_item.text
            # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
            #append aa to row - note one row entry is being appended
            row.append(aa)
        # append one row to all_rows
        all_rows.append(row)
    
    dataframes.append(pd.DataFrame(all_rows, columns=headings).drop(0, axis=0))
    
df = pd.concat(dataframes)

df.to_csv('CopaBrasil1975.csv')