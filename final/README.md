# Projeto `Campeonato Brasileiro Consolidado - Primeira Divisão`

# Equipe `Dupla de Dois` - `DDD`
* `Gustavo Mantellatto Elias` - `169366`
* `Leandro Garcia` - `178258`

## Resumo do Projeto
O Campeonato Brasileiro de Futebol é a principal competição de futebol entre clubes no país. O torneio que é hoje realizado anualmente e disputado por 20 times em um sistema de pontos corridos enfrentou diversos obstáculos para sua realização e passou por vários formatos até se tornar o que é hoje. Desde sua primeira edição em 1959, quando recebeu o nome de Taça Brasil, o torneio foi sendo disputado anualmente e incorporando mudanças ao longo do caminho, sendo a última delas em 2003, quando adotou o modelo vigente. Os nomes oficiais do Campeonato Brasileiro ao longo do tempo foram:

- Taça Brasil (1959 - 1968)
- Torneio Roberto Gomes Pedrosa (1967)
- Taça de Prata (1968 - 1970)
- Campeonato Nacional de Clubes (1971 - 1974)
- Copa Brasil (1984)
- Taça de Ouro (1985)
- Copa Brasil (1986 - 1988)
- Campeonato Brasileiro Série A (1989 - 1999; 2001 - Presente)
- Copa João Havelange (2000)
- Campeonato Brasileiro Série A (2001 - Presente)


Foi apenas em 20 de dezembro de 2010, quando a CBF por meio de nota unificou os títulos conquistados nos torneios listados acima, que todos eles passaram a ser contabilizados na contagem de campeonatos brasileiros dos clubes. Porém, pouco esforço foi feito por parte da CBF para agregar e disponibilizar os dados dos campeonatos históricos de forma consistente, de fato, não se consegue encontrar os dados sobre partidas realizadas nos campeonatos que foram unificados no site oficial da Confederação Brasileira de Futebol.
Pensando nisso, o objetivo desse projeto é consolidar e tratar os registros de partidas ocorridas nos Campeonatos Brasileiros oficiais desde 1959 em um só dataset, unindo informações presentes em repositórios sobre o sistema mais atual, com os dados de partidas encontrados em sites a serem extraídos a partir da técnica de Web Scraping. 


## Slides da Apresentação
> Coloque aqui o link para o PDF da apresentação final

## Modelo Conceitual

> ![Conceitual](assets/conceitual.png)

## Modelos Lógicos

### Relacional
~~~
CLUBE(_Clube_, Nome Completo, Cidade, UF, Fundação, Serie A, R_a, Serie B, P_b, R_b, Serie C, P_c, R_c, Serie D, P_d)
PARTIDA(_Data_, _Mandante_, Horario, Visitante, Placar_mandante, Placar_visitante)
  Mandante chave estrangeira -> Clube,
  Visitante chave estrangeira -> Clube
Campeonato(_Nome_, _Ano_, Inicio, Fim)
~~~

> Para o modelo de grafos de propriedades, utilize este
> [modelo de base](https://docs.google.com/presentation/d/10RN7bDKUka_Ro2_41WyEE76Wxm4AioiJOrsh6BRY3Kk/edit?usp=sharing) para construir o seu.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image`):
>
> ![Modelo Lógico de Grafos](images/modelo-logico-grafos.png)

> Para o modelo de grafos de conhecimento, utilize a abordagem
> (recurso, propriedade, valor) para apresentar seu grafo exemplo.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image).
>
> Você pode usar um grafo ilustrando as classes, como este:
> ![Modelo Lógico de Grafos de Conhecimento](images/grafo-conhecimento-classes.png)
>
> Além de outro com exemplo de instâncias, como este:
> ![Modelo Lógico de Grafos](images/grafo-conhecimento-exemplo.png)

> Para modelos hierárquicos (XML e JSON), utilize um formato
> conforme o abaixo:

> ![Modelo Lógico Hierárquico](images/modelo-logico-hierarquico.png)

## Dataset Publicado
> Elencar os arquivos/bases preliminares dos datasets serão publicados.

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<título do arquivo/base>` | `<link para arquivo/base>` | `<breve descrição do arquivo/base>`

> Os arquivos finais do dataset publicado devem ser colocados na pasta `data`, em subpasta `processed`. Outros arquivos serão colocados em subpastas conforme seu papel (externo, interim, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos que não estejam disponíveis online e sejam acessados pelo notebook. Relacionais (usualmente CSV), XML, JSON e CSV ou triplas para grafos.
> Este é o conjunto mínimo de informações que deve constar na disponibilização do Dataset, mas a equipe pode enriquecer esta seção.

## Bases de Dados
> Elencar as bases de dados fonte utilizadas no projeto.

título da base | link | breve descrição
----- | ----- | -----
`Ogol` | [www.ogol.com.br](https://www.ogol.com.br/) | `Um site com infomações de competições de futebol nacional e internacional. Mais importante, com o histórico de todos os torneios nacionais desde 1959. A técnica utilizada para extração de dados será o web scrapping com auxílio de bibliotecas do python.`
`Brasileirão Dataset` | [github.com/adaoduque/Brasileirao_Dataset](https://github.com/adaoduque/Brasileirao_Dataset) | `Dataset aberto independente com as partidas do campeonato brasileiro no período de pontos corridos. Os dados precisam passar por tratamento para se adequar ao modelo proposto pelo grupo, que acredita ser mais adequado pois simplifica as tabelas ao mesmo tempo que acomoda mais informações.`
`Wikipedia` | [wikipedia.com](www.wikipedia.com) | `Informações dos clubes e suas participações nos torneios nacionais serão extraídas aqui utilizando web scrapping e bibliotecas do python.`

## Detalhamento do Projeto
> A inspiração para o desenvolvimento do projeto se deu justamente pelo fato da ausência de dados estruturados dos campeonatos alvo, sendo assim, sua construção teve como base a extração de dados de páginas não estruturadas. Para isso, o grupo utilizou da técnica de `Web scrapping` para recuperar as informações desejadas dos sites utilizados como fonte. 

### Método de Extração da Tabela de Clubes da Wikipédia (scrapwiki.py)
> Através Wikipédia, obtemos uma tabela com todos os clubes que disputaram um campeonato nacional pelo menos uma vez desde 1959, bem como a quantidade de vezes que a disputaram e suas respectivas promoções / rebaixamentos à outras divisões.
~~~python
wiki_url = 'https://pt.wikipedia.org/wiki/Participa%C3%A7%C3%B5es_dos_clubes_no_Campeonato_Brasileiro_de_Futebol'

name = 'wikitable sortable'

response = requests.get(wiki_url)

soup = BeautifulSoup(response.text, 'html.parser')

#tabela dos clubes
teams_table = soup.find('table',{'class':name})
~~~


> Também extraímos da Wikipédia as referências aos clubes para serem usadas posteriormente como consultas à uma fonte estruturada como a DBPedia, essas consultas resultaram na coleta de informações complementares que auxiliaram a construir nossa tabela de Clubes.

~~~python
#cria lista com todos os links da tabela
for a in teams_table.find_all('a', href=True):
    if a.text:
        links.append(a['href'])
~~~
~~~python
#limpa a lista deixando apenas a parte que interessa dos links e apenas dos clubes
for i in range(4, len(links), 2):
    concepts.append(links[i][6:])      #retira os 6 primeiros char da lista "links"
~~~
> De posse dos links, exportamos para um arquivo csv que posteriormente será usado para realizar as consultas à DBPedia.

~~~python
dict = {'Reference': concepts}
df1 = pd.DataFrame(dict)
df1.to_csv('dbconcepts.csv', index=False)
~~~
> Ao final da execução, teremos o arquivo `clubes_raw.csv` contendo os dados da tabela bruta, dois arquivos `links_v0.csv` e `links_v1.csv` (contidos dentro de '/data/raw') sendo o primeiro sem nenhum tratamento e o segundo com a adição de um link faltante no site e remoção de comentários que integravam a tabela. Por fim, o arquivo `dbconcepts.csv` ('/data/external') é criado com as referências a serem utilizadas para busca dos recursos posteriormente na DBPedia.

<br>

### Método de Consulta à DBPedia (dbpediascrap.py)
> Nesse modelo, utilizamos os 521 `concepts` extraídos da tabela da Wikipédia no modelo _scrapWiki_ para realizar consultas individuais à DBPedia, a fim de recuperar informações complementares a respeito de todos os clubes da tabela.

> Aqui, as 521 consultas buscavam encontrar, para cada clube, seu `Nome Completo`, `Apelido` e `Data de Fundação`, sendo a maioria das consultas bem sucedidas. Dois problemas foram encontrados durante o procedimento de extração de dados:
> * Página da DBPedia com arquivo JSON corrompido: "SyntaxError: JSON.parse"
> * Página do recurso encontrada mas incorreta ou sem as informações
> 
> Nesses casos, o modelo apenas continua a consulta preenchendo as informações do respectivo clube com "-"

~~~python
#Laço percorrendo todos os recursos da DBPedia e obtendo as infos desejadas
for i in range(0, len(teams)):
    flag = True
    url_template = "http://dbpedia.org/data/{concept}.{format}"
    concept = teams[i]
    format = "jsod"
    concept = concept.replace(" ", "_")
    url = url_template.replace("{concept}", concept).replace("{format}", format)
    data = requests.get(url)
~~~


> Ao final da execução, um arquivo csv `'dbpedia_scrap.csv'`('/data/interm/') é gerado com os dados recuperados, ele será unido junto ao `clubes_raw.csv`.

<br>

### Método de Extração das Partidas (Modelo Web Scraping.py)
> É aqui que se concentra a maior quantidade de dados extraída, a tabela html da fonte de extração de dados era consideravelmente mais complexa do que a encontrada na Wikipédia, além disso, o site também possuia um mecanismo para realizar bloqueios quando muitos acessos seguidos eram realizados.

~~~python
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
~~~


### Arquivos Utilizados para tratamento de Dados:
* `clubes_join.py`: Unificação dos arquivos csv contendo informações dos clubes que disputaram os campeonatos cobertos pelo banco.
* `trat_brasileirao.py`: tratamento dos dados obtidos no github para os campeonatos de 2000-2021.

#### Tratamento Clubes (clubes_join.py)
Aqui, o objetivo é unificar as duas tabelas com informações dos clubes extraídas da Wikipédia e da DBPedia, para isso, foi utilizada a biblioteca pandas para criação e concatenação dos dataframes, além das alterações no nome e ordenaçao das colunas.

#### Tratamento Partidas (trat_brasileirao.py)
Essa rotina trata os arquivos obtivos através do dataset público do github utilizado como fonte, aqui o tratamento ocorreu da seguinte forma:

**Expansão das Colunas do DataFrame:** O dataframe original encontra-se apenas uma coluna e todos os dados de uma partida concentrados em uma única célula, o objetivo passa a ser expandir esse conteúdo de forma a facilitar sua manipulação e visualização.

~~~python
df_brasileirao[['ID', 'Rodada', 'Data', 'Horário', 'Dia', 'Mandante', 'Visitante', 
    'Vencedor', 'Arena', 'Mandante Placar', 'Visitante Placar', 'Estado Mandante', 
        'Estado Visitante', 'Estado Vencedor']] = df_brasileirao['ID;Rodada;Data;Horário;Dia;Mandante;Visitante;Vencedor;Arena;Mandante Placar;Visitante Placar;Estado Mandante;Estado Visitante;Estado Vencedor'].str.split(';', expand=True)
~~~


**Deleção das Células Antigas:** Uma vez expandido, a informação em formato menos otimizado pode ser removida.

**Deleção de Informação Redundante:** Colunas com informações redundantes que podem ser obtidas através de queries, como `Estado`, `Clube Vencedor` foram removidas a fim de otimizar a utilização de espaço dos dados.

**Renomeação de Colunas:** Para seguir o padrão do restante do banco de dados, as colunas foram renomeadas.



> Aqui devem ser apresentadas as operações de construção do dataset:
* extração de dados de fontes não estruturadas como, por exemplo, páginas Web
* agregação de dados fragmentados obtidos a partir de API
* integração de dados de múltiplas fontes
* tratamento de dados
* transformação de dados para facilitar análise e pesquisa

> Se for notebook, ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src` (por exemplo, arquivos do Orange ou Cytoscape). Se as operações envolverem queries executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Evolução do Projeto
> Relatório de evolução, descrevendo as evoluções na modelagem do projeto, dificuldades enfrentadas, mudanças de rumo, melhorias e lições aprendidas. Referências aos diagramas, modelos e recortes de mudanças são bem-vindos.
> Podem ser apresentados destaques na evolução dos modelos conceitual e lógico. O modelo inicial e intermediários (quando relevantes) e explicação de refinamentos, mudanças ou evolução do projeto que fundamentaram as decisões.
> Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

> Liste aqui as perguntas de pesquisa/análise e respectivas análises. Nem todas as perguntas precisam de queries que as implementam. É possível haver perguntas em que a solução é apenas descrita para demonstrar o potencial da base. Abaixo são ilustradas três perguntas, mas pode ser um número maior a critério da equipe.
>
### Perguntas/Análise com Resposta Implementada

> As respostas às perguntas podem devem ser ilustradas da forma mais rica possível com tabelas resultantes, grafos ou gráficos que apresentam os resultados. Os resultados podem ser analisados e comentados. Veja um exemplo de figura ilustrando uma comunidade detectada no Cytoscape:

> ![Comunidade no Cytoscape](images/cytoscape-comunidade.png)

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

### Perguntas/Análise Propostas mas Não Implementadas

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

> Coloque um link para o arquivo do notebook que executa o conjunto de queries. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.
