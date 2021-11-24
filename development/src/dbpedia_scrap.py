import io
from os import stat
import requests
import json
import pandas as pd
import csv

from requests.models import Response



#Lendo o arquivo csv e salvando em uma lista
teams= []
with open('dbconcepts.csv', newline='') as f:
    reader = csv.reader(f)
    teams = list(reader)
teams = [item[0] for item in teams]

#remove o nome da coluna
del teams[0]


#Listas para construção do nosso DataFrame
fullnames = []
nicknames = []
formations = []
fundations = []
status = []


#Laço percorrendo todos os recursos da DBPedia e obtendo as infos desejadas
#for team in teams:
for i in range(0, len(teams)):
    flag = True
    url_template = "http://dbpedia.org/data/{concept}.{format}"

    concept = teams[i]
    format = "jsod"

    concept = concept.replace(" ", "_")

    url = url_template.replace("{concept}", concept).replace("{format}", format)

    data = requests.get(url)
    #Tratamento de erros para JSON inválidos
    try:
        resp_content = data.json()
    except ValueError:
        resp_content = data.content
        flag = False

    
    #JSON inválido, preenche a posição nas listas
    if (flag == False):
        fullnames.append("-")
        nicknames.append("-")
        formations.append("-")
        fundations.append("-")
        status.append("SyxtaxError")
        continue
    
    js = resp_content


    #Se o vetor de resultados possui pelo menos 1 elemento
    if(js["d"]["__count"] != '0'):
        status.append("Found")
        # Flag para verificar se recurso possui nome completo do clube
        if("http://dbpedia.org/property/fullname" in js["d"]["results"][0]):
            fullname = js["d"]["results"][0]["http://dbpedia.org/property/fullname"]
        else:
            fullname = "-"
        fullnames.append(fullname)

        #Flag para apelido
        if("http://dbpedia.org/property/nickname" in js["d"]["results"][0]):
            nickname = js["d"]["results"][0]["http://dbpedia.org/property/nickname"]
        else:
            nickname = "-"
        nicknames.append(nickname)

        #Flag para Formação
        if("http://dbpedia.org/ontology/formationDate" in js["d"]["results"][0]):
            formation = js["d"]["results"][0]["http://dbpedia.org/ontology/formationDate"]
        else:
            formation = "-"
        formations.append(formation)

        #Flag para Fundação
        if("http://dbpedia.org/property/founded" in js["d"]["results"][0]):
            founded = js["d"]["results"][0]["http://dbpedia.org/property/founded"]
        else:
            founded = "-"
        fundations.append(founded)


    else:
        #Não tem recurso na DBPedia, preenche como linha vazia
        status.append("NotFound")
        fullnames.append("-")
        nicknames.append("-")
        formations.append("-")
        fundations.append("-")
    
#Criando DataFrame e Exportando em um csv
dict = {'Fullname': fullnames, 'Nickname': nicknames, 'formationDate': formations, 
            'fundation': fundations, 'status': status}
df = pd.DataFrame(dict)
df.to_csv('dbpedia_scrap.csv', index=False)