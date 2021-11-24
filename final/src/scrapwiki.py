from os import link
from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = 'https://pt.wikipedia.org/wiki/Participa%C3%A7%C3%B5es_dos_clubes_no_Campeonato_Brasileiro_de_Futebol'

name = 'wikitable sortable'

response = requests.get(wiki_url)

soup = BeautifulSoup(response.text, 'html.parser')

#tabela dos clubes
teams_table = soup.find('table',{'class':name})



################################################
# Obtendo os links para referência no DBPedia: #
################################################

links=[]
#cria lista com todos os links da tabela
for a in teams_table.find_all('a', href=True):
    if a.text:
        links.append(a['href'])

#Um dos links da tabela de clubes estava faltando:
links.insert(772, "/wiki/Ficheiro:Duque_de_Caxias(MA)")


#Arquivo com os Links sem tratamento nenhum
dict = {'Reference': links}
df2 = pd.DataFrame(dict)
df2.to_csv('links_v0.csv', index=False)


# O arquivo veio com algumas linhas de comentários indesejáveis
links = [x for x in links if x[0] != "#"]
dict = {'Reference': links}
df3 = pd.DataFrame(dict)
df3.to_csv('links_v1.csv', index=False)

concepts = []
#limpa a lista deixando apenas a parte que interessa dos links e apenas dos clubes
for i in range(4, len(links), 2):
    #links[i] = links[i][6: ]
    concepts.append(links[i][6:])      #retira os 6 primeiros char da lista "links"


#Exportando a lista dos concepts em um csv
dict = {'Reference': concepts}
df1 = pd.DataFrame(dict)
df1.to_csv('dbconcepts.csv', index=False)




############################################
# Obtendo a tabela dos clubes da Wikipédia #
############################################

df = pd.read_html(str(teams_table))         #read_html retorna uma lista

df = df[0]      #converte em um dataframe

df.to_csv('clubes_raw.csv')

