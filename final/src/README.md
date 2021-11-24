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

> Nesse Modelo, extraímos a tabela bruta com os dados dos Clubes do site da Wikipédia utilizando `webscrapping`, bem como obtemos os links para todas as páginas da Wiki que referenciam esses clubes, com o intuito de utilizar esses links para acessar o recurso de todos os clubes na DBPedia e através do modelo estruturado recuperar informações individuais dos clubes como Nome Completo, Apelido e Data de Fundação.

> Ao final da execução, teremos o arquivo `clubes_raw.csv` contendo os dados da tabela bruta, dois arquivos `links_v0.csv` e `links_v1.csv` (contidos dentro de '/data/raw') sendo o primeiro sem nenhum tratamento e o segundo com a adição de um link faltante no site e remoção de comentários que integravam a tabela. Por fim, o arquivo `dbconcepts.csv` ('/data/external') é criado com as referências a serem utilizadas para busca dos recursos posteriormente na DBPedia.

# Modelo de Consultas à DBPedia (dbpediascrap.py)

> Nesse modelo, utilizamos os 521 `concepts` extraídos da tabela da Wikipédia no modelo _scrapWiki_ para realizar consultas individuais à DBPedia, a fim de recuperar informações complementares a respeito de todos os clubes da tabela.

> Aqui, as 521 consultas buscavam encontrar, para cada clube, seu `Nome Completo`, `Apelido` e `Data de Fundação`, sendo a maioria das consultas bem sucedidas. Dois problemas foram encontrados durante o procedimento de extração de dados:
> * Página da DBPedia com arquivo JSON corrompido: "SyntaxError: JSON.parse"
> * Página do recurso encontrada mas incorreta ou sem as informações
> 
> Nesses casos, o modelo apenas continua a consulta preenchendo as informações do respectivo clube com "-"

> Ao final da execução, um arquivo csv `'dbpedia_scrap.csv'`('/data/interm/') é gerado com os dados recuperados, ele será unido junto ao `clubes_raw.csv`.

***

## Arquivos Utilizados para tratamento de Dados:
* `clubes_join.py`: Unificação dos arquivos csv contendo informações dos clubes que disputaram os campeonatos cobertos pelo banco.
* `trat_brasileirao.py`: tratamento dos dados obtidos no github para os campeonatos de 2000-2021.

# Tratamento Clubes (clubes_join.py)
Aqui, o objetivo é unificar as duas tabelas com informações dos clubes extraídas da Wikipédia e da DBPedia, para isso, foi utilizada a biblioteca pandas para criação e concatenação dos dataframes, além das alterações no nome e ordenaçao das colunas.

# Tratamento Partidas (trat_brasileirao.py)
Essa rotina trata os arquivos obtivos através do dataset público do github utilizado como fonte, aqui o tratamento ocorreu da seguinte forma:

**Expansão das Colunas do DataFrame:** O dataframe original encontra-se apenas uma coluna e todos os dados de uma partida concentrados em uma única célula, o objetivo passa a ser expandir esse conteúdo de forma a facilitar sua manipulação e visualização.

**Deleção das Células Antigas:** Uma vez expandido, a informação em formato menos otimizado pode ser removida.

**Deleção de Informação Redundante:** Colunas com informações redundantes que podem ser obtidas através de queries, como `Estado`, `Clube Vencedor` foram removidas a fim de otimizar a utilização de espaço dos dados.

**Renomeação de Colunas:** Para seguir o padrão do restante do banco de dados, as colunas foram renomeadas.

***
# Instalação
Para a utilização das rotinas disponibilizadas aqui, basta realizar a importação (ou instalação) de suas respectivas bibliotecas
~~~
pip install <biblioteca>
~~~
