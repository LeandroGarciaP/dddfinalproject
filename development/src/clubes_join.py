import io
from os import stat
import requests
import json
import pandas as pd
import csv
import numpy as np

from requests.models import Response

#Rotina para concatenar os dois dataframes complementares com informações dos clubes

df_clubes = pd.read_csv('clubes_raw.csv')
df_infos = pd.read_csv('dbpedia_scrap.csv')



#Tratamento
df_clubes = df_clubes.rename(columns={"R":"R_a", "P":"P_b", "R.1":"R_b","P.1":"P_c", "R.2":"R_c",
            "P.2":"P_d",})

data = pd.concat((df_clubes, df_infos), axis=1)


#Alterando a ordem das colunas para melhor legibilidade
data = data[['Clube', 'Fullname', 'Nickname', 'Cidade', 'UF', 'formationDate', 'fundation',
    'Série A', 'R_a', 'Série B', 'P_b', 'R_b', 'Série C', 'P_c', 'R_c', 'Série D', 'P_d']]

data = data.rename(columns={"Fullname":"Nome Completo", "Nickname":"Apelido", 
    "formationDate":"Formacao","fundation":"Fundacao"})

data.to_csv('clubes_v0.csv', index=False)


