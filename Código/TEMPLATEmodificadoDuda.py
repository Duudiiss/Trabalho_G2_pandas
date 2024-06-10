# -*- coding: utf-8 -*-
############################################################################################
################################     Trabalho do G2   ######################################
#
# Giulia Orlandi - 2210383
# Felipe Calmon Lucas - 1713097
# Luisa Barragat Schneider - 2011398
# Maria Eduarda de Menezes Queiroz - 2320625
#
# Declaração de autoria: declaro que este documento foi produzido pelo grupo em sua totalidade,
#           sem consultas a outros alunos, professores ou qualquer outra pessoa.
############################################################################################


import pandas as pd
import matplotlib.pyplot as plt
import random 
print('\=================================')
print('\n Trabalhando com PANDAS \n')
print('\=================================')
'''
O arquivo excel `top_insta_influencers_data.xlsx` apresenta informações detalhadas sobre alguns dos 
principais influenciadores do Instagram. As colunas presentes no arquivo são:


channel_info: Nome de usuário do influenciador no Instagram. Este é o identificador principal do 
influenciador na plataforma.

Rank: A posição do influenciador em um ranking baseado na sua influência geral. Um menor número indica 
uma classificação mais alta.

influence_score: Uma pontuação que quantifica o nível de influência do usuário no Instagram. Esta pontuação 
pode ser baseada em vários fatores, como o número de seguidores, o engajamento, o alcance das postagens, etc.

Posts: O número total de postagens que o influenciador fez no Instagram. Pode incluir fotos, vídeos 
e outros tipos de conteúdo.

followers: O número de pessoas que seguem o influenciador no Instagram. Este número é um indicador 
importante da popularidade do influenciador.

avg_likes: A média de curtidas que cada postagem do influenciador recebe. Este valor é calculado dividindo
o total de curtidas pelo número de postagens.

60_day_eng_rate: A taxa de engajamento das postagens do influenciador nos últimos 60 dias. É geralmente 
expressa como uma porcentagem e pode ser calculada como o número total de interações (curtidas, comentários, etc.)
dividido pelo número de seguidores e multiplicado por 100.

new_post_avg_like: A média de curtidas que as postagens mais recentes do influenciador receberam. Isso
pode dar uma ideia de quão ativo e relevante o influenciador é no momento.

total_likes: O número total de curtidas que todas as postagens do influenciador receberam ao longo do 
tempo. Este é um indicador cumulativo de engajamento.

country: O país de origem ou residência do influenciador. Esta informação pode ser útil para identificar 
influenciadores em mercados específicos ou para campanhas direcionadas a uma audiência particular.

'''
"""TRANSFORMANDO EM ARQUIVO EXCEL"""
# dfConverter = pd.read_csv("Base_de_Dados\\top_insta_influencers_data.csv", header= 0, index_col= 1)
# dfConverter.to_excel("Base_de_Dados\\top_insta_influencers_data.xlsx")

print('\n==============================================')
print('Questão 1\n')
#======================================================================
# Transformando o tipo do arquivo e renomeando as colunas do inglês para português
#======================================================================
dfInfluencers = pd.read_excel("C:\\Users\\meduarda\\Downloads\\top_insta_influencers_data.xlsx", header= 0 , index_col= 1)
dfInfluencers.rename(columns= {'channel_info': 'Nome do Canal', 'influence_score': 'Pontuação', 
                               'posts': 'Numero de Postagens', 'followers': 'Numero de Seguidores', 
                               'avg_likes': 'Média de Curtidas', 'country': 'País', 
                              '60_day_eng_rate': 'Taxa de Engajamento em 60 dias (%)', 
                              'new_post_avg_like': 'Média de Curtidas em Novas Postagens',
                              'total_likes': 'Total de Curtidas'}, inplace = True)

print(dfInfluencers)

print('\n==============================================')
print('Questão 2 - Substituição de valores\n')
#======================================================================
# Substituir os valores que terminam em 'k', 'm', 'b', para numérico 
# ex: 6m = 6.000.000
#======================================================================
print('/n------------------------------------------------------')
print('2-')
colunas = ['Numero de Postagens', 'Total de Curtidas', 'Média de Curtidas em Novas Postagens', 
           'Numero de Seguidores', 'Média de Curtidas']
for col in colunas:
    dfInfluencers[col] = dfInfluencers[col].str.replace('.', '')

    dfInfluencers[col] = dfInfluencers[col].str.replace('k', '00')
    dfInfluencers[col] = dfInfluencers[col].str.replace('m', '00000')
    dfInfluencers[col] = dfInfluencers[col].str.replace('b', '00000000')
    dfInfluencers[col] = pd.to_numeric(dfInfluencers[col])
    
print(dfInfluencers)

print('------------------------------------------------------')


print('\n==============================================')
print('Questão 3 - Preencher valores auxentes: \n')
#======================================================================
# a) Preencher os valores ausentes da coluna 'País' por 'Não informado'
# b) Preencher os valores ausentes da coluna 'Média de Curtidas em Novas Postagens'
# pela média dessa coluna 
#======================================================================
print('/n------------------------------------------------------')
print('3.a')
dfInfluencers.País.fillna('Não informado', inplace=True)
print(dfInfluencers)

print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('3.b')

media = dfInfluencers['Média de Curtidas em Novas Postagens'].mean()
dfInfluencers['Média de Curtidas em Novas Postagens'].fillna(media, inplace=True)
print(dfInfluencers['Média de Curtidas em Novas Postagens'])

print('------------------------------------------------------')




print('\n==============================================')
print('Questão 4 -  Criar Categorias em função do valor de uma coluna\n')
#======================================================================
# a) Crie e exiba a coluna 'Crescimento/Engajamento' que categoriza os influencers
# em 3 faixas de acordo com a coluna ‘Taxa de Engajamento em 60 dias’.
#
# b) Criar coluna ‘Faixa de Pontuação’ que categoriza os influencers em 
# 'Baixa', 'Média', 'Alta', 'Muito Alta' de acordo com a coluna ‘Pontuação’
# e exiba os influencers com pontuaçãi 'Média'.
#======================================================================
print('/n------------------------------------------------------')
print('4.a')
print('------------------------------------------------------')
dfInfluencers['Crescimento/Engajamento'] = pd.cut(dfInfluencers['Total de Curtidas'], 
                                               bins=3,labels=['Baixo', 'Médio', 'Alto'])
print(dfInfluencers['Crescimento/Engajamento'])

print('/n------------------------------------------------------')
print('4.b')
print('------------------------------------------------------')
dfInfluencers['Faixa de Pontuação'] = pd.cut(dfInfluencers['Pontuação'], bins=[0,30,60,90,100],
                                             labels=['Baixa', 'Média', 'Alta', 'Muito Alta'])
print(dfInfluencers.loc[dfInfluencers['Faixa de Pontuação'] =='Média'])

print('\n==============================================')
print('Questão 5 - Filtros\n')
#======================================================================
# a) Filtrar Pontuação acima de 90
# b) Filtrar a base de dados com uma lista aleatória de index.
# c) Agora filtre o DataFrame usando a combinação dos itens anteriores.
#======================================================================
print('/n------------------------------------------------------')
print('5.a')
print('------------------------------------------------------')
# print(dfInfluencers['Pontuação'].isin(list(range(91,dfInfluencers['Pontuação'].values.max()+1)) ))
####?? duda ??###
print(dfInfluencers.loc[dfInfluencers['Pontuação']>90])

print('/n------------------------------------------------------')
print('5.b')
print('/n------------------------------------------------------')
numerosAleatorios = list(random.sample(range(1,201),30)) 
celebridades = ['Dwayne Johnson', 'Kylie Jenner', 'Cristiano Ronaldo', 'Ariana Grande', 'Selena Gomez',
                'Kim Kardashian', 'Lionel Messi', 'Beyoncé', 'Justin Bieber', 'Taylor Swift']
listaAleatóriaIndex = numerosAleatorios + celebridades 
colunas_index = dfInfluencers.index.isin(listaAleatóriaIndex)
print(colunas_index) 

print('/n------------------------------------------------------')
print('5.c')
print('------------------------------------------------------')
print(dfInfluencers.loc[(dfInfluencers['Pontuação'].isin(list(range(91,dfInfluencers['Pontuação'].values.max()+1)) )== True),(dfInfluencers.columns.isin(listaAleatóriaIndex)== True)])

print('\n==============================================')
print('Questão 6 - Tabelas de Frequência\n')
#======================================================================
# a) Tabela de Frequência dos países com inflenciadores de Pontuação acima de 90
# b) Tabela de Frequência Percentual do Engajamento Diário dos 20 Primeiros Influenciadores Estadunidenses
#======================================================================
print('\n------------------------------------------------------')
print('6.a')
print('------------------------------------------------------')
MaioresInfluenciadores = dfInfluencers.loc[dfInfluencers['Pontuação']>90]

TabelaFrequenciaSeguidores = pd.crosstab(index=MaioresInfluenciadores['Pontuação'], columns=dfInfluencers['País'])
print(TabelaFrequenciaSeguidores)

MaioresInfluenciadoresUsa = dfInfluencers[dfInfluencers['País'] == 'United States'].head(20)
# TabelaFrequenciaSeguidores = pd.crosstab(index=MaioresInfluenciadoresUsa['Nome do Canal'], columns='Frequência', values=MaioresInfluenciadoresUsa['Numero de Seguidores'], aggfunc='sum')
# print(TabelaFrequenciaSeguidores)

print('\n------------------------------------------------------')
print('6.b')
print('------------------------------------------------------')
def converte_str_em_porcentagem(valor_antigo):
    valor_novo = valor_antigo.replace('%', '')
    return float(valor_novo) 

MaioresInfluenciadoresUsa['Taxa de Engajamento em 60 dias (%)'] = MaioresInfluenciadoresUsa['Taxa de Engajamento em 60 dias (%)'].apply(converte_str_em_porcentagem) 
TabelaPorcentagemEngajamento = pd.crosstab(index=MaioresInfluenciadoresUsa['Nome do Canal'], columns='Percentual de Engajamento Diário', values=MaioresInfluenciadoresUsa['Taxa de Engajamento em 60 dias (%)'], aggfunc='mean')
print(TabelaPorcentagemEngajamento)


print('\n==============================================')
print('Questão 7 - Gráficos\n')
#======================================================================
# a) gráfico de coluna que mostre a distribuição de influenciadores por país 
# b) gráfico de pizza que mostre a distribuição dos influenciadores nos países do continente americano.
#======================================================================
print('\n------------------------------------------------------')
print('7.a')
print('------------------------------------------------------')
cores = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e',
    '#e6ab02', '#a6761d', '#666666', '#377eb8', '#ff7f00',
    '#4daf4a', '#984ea3', '#ff0000', '#ffff33', '#a65628'
]
dfInfluencers['País'].value_counts().plot.bar(title = 'Distribuição de influentes ao longo do globo', color = cores, figsize = (10,10))
plt.show()
print('\n------------------------------------------------------')
print('7.b')
print(dfInfluencers['País'].value_counts()) 
paises_americanos = [
    "United States", "Brazil", "Colombia", "Canada", "Mexico", 
    "Puerto Rico", "Anguilla", "British Virgin Islands", "Uruguay"
] 
dfInfluencers['País'].loc[dfInfluencers['País'].isin(paises_americanos)].value_counts().plot.pie(title = 'Distribuição de influentes no continente americano', figsize = (10,10), autopct = '%.1f') 
plt.show()
print('------------------------------------------------------')


print('\n==============================================')
print('Questão 8 - Medidas de Sumarização\n')
#======================================================================
# a) Mostrar valores minimo, maximo e médio da coluna 'Numero de Postagens'.
# b) A partir da coluna ‘País’ agrupar os influencers e mosrtrar o total de 
# curtidas dos influencers brasileiros.
# c) Agrupar influencers por 'País' e 'Faixa de Pontuação' e exibir o total 
# de curtida de brasileiros por Faixas de Pontuação.
#======================================================================

print('------------------------------------------------------')
print('8.a')
print('------------------------------------------------------')
print(dfInfluencers['Numero de Postagens'].agg(['min','max', 'mean']))

print('\n------------------------------------------------------')
print('8.b')
print('------------------------------------------------------')
dfAgrupado = dfInfluencers.groupby(by=dfInfluencers['País'])['Total de Curtidas'].sum()
print('Total de curtidas no Brasil:')
print(dfAgrupado.loc['Brazil'])

print('\n------------------------------------------------------')
print('8.c')
print('------------------------------------------------------')
dfgrupPaisPont = dfInfluencers.groupby(by=[dfInfluencers['País'], 
                                           dfInfluencers['Faixa de Pontuação']])['Total de Curtidas'].sum()
print(dfgrupPaisPont.loc['Brazil'])
print('\n==============================================')
print('Questão 9\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('------------------------------------------------------')
print('9.a')
print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('9.b')
print('------------------------------------------------------')

