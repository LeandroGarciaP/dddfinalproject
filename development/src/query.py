### importando bibliotecas
import pandas as pd
import warnings as wa



### ignorando warnings do tipo FutureWarning
wa.simplefilter( action='ignore', category= FutureWarning)
pd.options.mode.chained_assignment = None

periodo = "https://raw.githubusercontent.com/juvenalfonseca/python/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-periodo.csv"

df_partidas = pd.read_csv('Partidas - Campeonato Brasileiro (2000 - 2021).csv', delimiter=',')
df_periodo = pd.read_csv(periodo, delimiter=';')    #delimitador de acordo com o site

#manter tudo em letras minpusculas para padronizar
df_periodo.columns = df_periodo.columns.str.lower()
df_partidas.columns   = df_partidas.columns.str.lower()







### altera campos de datas de character para date
df_periodo['inicio' ] = pd.to_datetime(df_periodo['inicio'], format="%d/%m/%Y")
df_periodo['fim'    ] = pd.to_datetime(df_periodo['fim'   ], format="%d/%m/%Y")
df_partidas['data'     ] = pd.to_datetime(df_partidas['data'    ], format="%Y/%m/%d")   #data formato diff




### captalizar strings
#df_partidas['dia'      ] = df_partidas['dia'      ].str.title()
df_partidas['mandante' ] = df_partidas['mandante' ].str.title()
df_partidas['visitante'] = df_partidas['visitante'].str.title()
#df_partidas['vencedor' ] = df_partidas['vencedor' ].str.title()
#df_partidas['arena'    ] = df_partidas['arena'    ].apply(lambda x: x.title())

#print(df_partidas.head(5))
#print(df_periodo.head(5))


### junta os datasets e retorna apenas os registros corretos criados na junção
df_periodo['key'] = 1
df_partidas['key'] = 1
 
df = pd.merge(df_periodo, df_partidas, on ='key').drop("key", 1)
df = df.query('data >= inicio & data <= fim')



### gols por edição
gols_mandante = df[['torneio', 'mandante placar']].groupby('torneio').agg(lambda x: sum(x)).reset_index()
gols_mandante.rename(columns = {"mandante placar": "gols_mandante"}, inplace=True)
 
gols_visitante = df.groupby('torneio')['visitante placar'].sum().sort_values(ascending=False).reset_index()
gols_visitante.rename(columns = {"visitante placar": "gols_visitante"}, inplace=True)
 
gols_edicao = pd.merge(gols_mandante, gols_visitante, on="torneio")
gols_edicao['gols_total'] = gols_edicao['gols_mandante'] + gols_edicao['gols_visitante']
gols_edicao['gols_mandante_perc'  ] = (gols_edicao['gols_mandante' ]/gols_edicao['gols_total'])*100
gols_edicao['gols_visitantes_perc'] = (gols_edicao['gols_visitante']/gols_edicao['gols_total'])*100

#print(gols_edicao) - Funcionando


### gols por edição comparativo
df1 = gols_edicao[['torneio','gols_mandante' ]]
df2 = gols_edicao[['torneio','gols_visitante']]
df3 = gols_edicao[['torneio','gols_total'    ]]
 
df1.rename(columns = {'gols_mandante' : 'gols' }, inplace=True)
df2.rename(columns = {'gols_visitante': 'gols' }, inplace=True)
df3.rename(columns = {'gols_total'    : 'gols' }, inplace=True)
 
df1['tipo_gols'] = 'gols_mandante'
df2['tipo_gols'] = 'gols_visitante'
df3['tipo_gols'] = 'gols_total'
 
df4 = pd.concat([df1, df2, df3]).reset_index(drop=True)

#print(df4)


### top 10 clubes gols marcados
gols_mandante_time  = df.groupby('mandante' )['mandante placar' ].sum().sort_values(ascending=False).reset_index()
gols_mandante_time.rename(columns  = {"mandante" : "time", 'mandante placar' : 'gols marcados' }, inplace=True)
 
gols_visitante_time = df.groupby('visitante')['visitante placar'].sum().sort_values(ascending=False).reset_index()
gols_visitante_time.rename(columns = {"visitante": "time", 'visitante placar': 'gols marcados' }, inplace=True)
 
gols_time = pd.concat([gols_mandante_time, gols_visitante_time])
 
gols_marcados_time = gols_time.groupby('time')['gols marcados'].sum().sort_values(ascending=False).reset_index()
#print(gols_marcados_time.head(10))



### top 10 clubes gols sofridos
gols_mandante_time  = df.groupby('visitante')['mandante placar' ].sum().sort_values(ascending=False).reset_index()
gols_mandante_time.rename(columns  = {"visitante": "time", 'mandante placar' : 'gols sofridos' }, inplace=True)
 
gols_visitante_time = df.groupby('mandante' )['visitante placar'].sum().sort_values(ascending=False).reset_index()
gols_visitante_time.rename(columns = {"mandante" : "time", 'visitante placar': 'gols sofridos' }, inplace=True)
 
gols_time = pd.concat([gols_mandante_time, gols_visitante_time])
 
gols_sofridos_time = gols_time.groupby('time')['gols sofridos'].sum().sort_values(ascending=False).reset_index()
#print(gols_sofridos_time.head(10))


#######################################
### melhores ataques por edição
df['clube']                  = df['mandante']
gols_clubes_mandantes        = df.groupby(['torneio','clube'])['mandante placar'].sum().sort_values(ascending=False).reset_index()
gols_clubes_mandantes.rename(columns  = {"mandante placar" : "gols_mandante" }, inplace=True)
 
df['clube']                  = df['visitante']
gols_clubes_visitantes       = df.groupby(['torneio','clube'])['visitante placar'].sum().sort_values(ascending=False).reset_index()
gols_clubes_visitantes.rename(columns = {"visitante placar": "gols_visitante"}, inplace=True)
 
gols_clubes               = pd.merge(gols_clubes_mandantes, gols_clubes_visitantes,  on=["torneio","clube"])
gols_clubes['gols_total'] = gols_clubes['gols_mandante'] + gols_clubes['gols_visitante']
 
ataque_pior   = gols_clubes.groupby('torneio')['gols_total'].min().sort_values(ascending=False).reset_index()
ataque_melhor = gols_clubes.groupby('torneio')['gols_total'].max().sort_values(ascending=False).reset_index()
 
gols_torneio_ataque_melhor = pd.merge(gols_clubes, ataque_melhor, on=['torneio','gols_total'])[['torneio','clube','gols_total']]
gols_torneio_ataque_melhor.rename(columns = {"gols_total": "ataque_melhor"}, inplace=True)
 
gols_torneio_ataque_pior   = pd.merge(gols_clubes, ataque_pior  , on=['torneio','gols_total'])[['torneio','clube','gols_total']]
gols_torneio_ataque_pior.rename(columns   = {"gols_total": "ataque_pior"  }, inplace=True)
 
gols_ataques = pd.merge(gols_torneio_ataque_melhor, gols_torneio_ataque_pior, on="torneio", suffixes=("_melhor","_pior"))
#print(gols_ataques.sort_values(['torneio','clube_melhor']))


# pontuação
pontos_participantes               = df.groupby('torneio')['mandante'].nunique().sort_values(ascending=False).reset_index()
pontos_participantes['pontos_max'] = (pontos_participantes.mandante - 1)*2*3
 
pontos = df[['torneio', 'mandante', 'visitante', 'mandante placar', 'visitante placar']]
pontos['pontos_mandante' ] = pontos.apply(lambda x: 3 if x['mandante placar'] > x['visitante placar'] else (0 if x['mandante placar'] < x['visitante placar'] else 1), axis=1)
pontos['pontos_visitante'] = pontos.apply(lambda x: 3 if x['mandante placar'] < x['visitante placar'] else (0 if x['mandante placar'] > x['visitante placar'] else 1), axis=1)
 
pontos_mandantes = pontos.groupby(['torneio','mandante' ])['pontos_mandante' ].sum().sort_values(ascending=False).reset_index()
pontos_mandantes.rename(columns = {"mandante": "clube" }, inplace=True)

pontos_visitante = pontos.groupby(['torneio','visitante'])['pontos_visitante'].sum().sort_values(ascending=False).reset_index()
pontos_visitante.rename(columns = {"visitante": "clube"}, inplace=True)

pontos_total = pd.merge(pontos_mandantes, pontos_visitante, on=['torneio','clube'])
pontos_total['pontos_total'] = pontos_total.pontos_mandante + pontos_total.pontos_visitante


#maior pontuador das edições de pontos corridos
print(pontos_total[pontos_total['pontos_total'] == pontos_total['pontos_total'].max()])

#menor pontuador das edições de pontos corridos
print(pontos_total[pontos_total['pontos_total'] == pontos_total['pontos_total'].min()])
