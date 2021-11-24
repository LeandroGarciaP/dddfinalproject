# Instruções do Arquivos Source

## Bibliotecas
* import BeautifulSoup
* import Requests
* import csv
* import json


## Arquivos Utilizados para extração de Dados:
* `scrapwiki.py`: Extração da tabela de Clubes
* `dbpediascrap.py`:  Consulta à DBPedia para todos os 521 clubes da tabela
* `Modelo Web Scraping`: Extração das partidas


# Modelo de extração da tabela de Clubes de Futebol na Wikipédia (scrapwiki.py)

**Fonte:** [Participação dos Clubes no Campeonato Brasileiro de Futebol](https://pt.wikipedia.org/wiki/Participa%C3%A7%C3%B5es_dos_clubes_no_Campeonato_Brasileiro_de_Futebol)

> Nesse Modelo, extraímos a tabela bruta com os dados dos Clubes do site da Wikipédia utilizando webscrapping, bem como obtemos os links para todas as páginas da Wiki que referenciam esses clubes, com o intuito de utilizar esses links para acessar o recurso de todos os clubes na DBPedia e através do modelo estruturado recuperar informações individuais dos clubes como Nome Completo, Apelido e Data de Fundação


