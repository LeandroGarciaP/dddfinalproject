import io
from os import stat
import requests
import json
import pandas as pd
import csv
import numpy as np

from requests.models import Response


#Importa o Dataset original da fonte
df_brasileirao = pd.read_csv('campeonato-brasileiro-full.csv')


#O dataset veio com os valores divididos em apenas uma célula,
#Divide a informação do dataset em colunas para facilitar a manipulação:
df_brasileirao[['ID', 'Rodada', 'Data', 'Horário', 'Dia', 'Mandante', 'Visitante', 
    'Vencedor', 'Arena', 'Mandante Placar', 'Visitante Placar', 'Estado Mandante', 
        'Estado Visitante', 'Estado Vencedor']] = df_brasileirao['ID;Rodada;Data;Horário;Dia;Mandante;Visitante;Vencedor;Arena;Mandante Placar;Visitante Placar;Estado Mandante;Estado Visitante;Estado Vencedor'].str.split(';', expand=True)



#Apaga a célula antiga, deixando apenas os valores organizados
df_brasileirao = df_brasileirao.drop(['ID;Rodada;Data;Horário;Dia;Mandante;Visitante;Vencedor;Arena;Mandante Placar;Visitante Placar;Estado Mandante;Estado Visitante;Estado Vencedor'], axis=1)


#Exclui colunas com informação redundante
df_brasileirao = df_brasileirao.drop('ID', 1)
df_brasileirao = df_brasileirao.drop('Estado Mandante', 1)
df_brasileirao = df_brasileirao.drop('Estado Visitante', 1)
df_brasileirao = df_brasileirao.drop('Estado Vencedor', 1)
df_brasileirao = df_brasileirao.drop('Vencedor', 1)
df_brasileirao = df_brasileirao.drop('Dia', 1)
df_brasileirao = df_brasileirao.drop('Arena', 1)

#Renomeia a coluna para seguir o padrao do modelo conceitual
df_brasileirao = df_brasileirao.rename(columns={"Rodada":"Fase", "Mandante Placar":"Placar Mandante",
    "Visitante Placar": "Placar Visitante" })
    

#Exporta o arquivo padronizado
df_brasileirao.to_csv('Partidas - Campeonato Brasileiro (2000 - 2021).csv', sep=',', index=False)
