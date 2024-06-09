# -*- coding: utf-8 -*-

'''1. trabalhoGrupoXXX.docx com:
 SEUS DADOS: nome completo, matrícula, turma
 O Rótulo do seu Grupo e os nomes completos de todos os componentes do
GrupoXXX
 fonte dos dados (endereço completo de onde a base está)
 descrição da base de dados, isto é, o que representam as colunas
 Perguntas a serem respondidas – Todas devem ser numeradas
OBS1: as bases devem ser abertas, ou seja, não podem ser utilizadas bases fechadas, pagas ou
internas de empresas, que não permitam acesso para verificação da base.
OBS2:É terminantemente proibido se basear em provas ou trabalhos de períodos anteriores de
qualquer disciplina de manipulação de dados.


2. templateTrabalhoDoGrupoXXX.py com:
 SEUS DADOS: nome completo, matrícula, turma
 O Rótulo do seu Grupo e os nomes completos de todos os componentes do
GrupoXXX
 Para cada pergunta do docx
print("\n-----------------------------------------------------")
print("\n número e texto da questão: \n")
print("\n-----------------------------------------------------")


3. gabaritoTrabalhoGrupoXXX.py com:
 SEUS DADOS: nome completo, matrícula, turma
 O Rótulo do seu Grupo e os nomes completos de todos os componentes do
GrupoXXX
 Para cada pergunta do docx
print("\n-----------------------------------------------------")
print("\n número e texto da questão: \n")
print( sua resposta para a questão)
print("\n-----------------------------------------------------")


4. Arquivo excel com os dados (colocar o rótulo do grupo no início do nome do arquivo)
As perguntas formuladas por você devem ser elaboradas e, para serem respondidas, devem
fazer uso dos seguintes recursos do pandas vistos em aula (no mínimo):
ATENÇÃO : OS QUESITOS ABAIXO TÊM QUE OBRIGATORIAMENTE SER TODOS UTILIZADOS
PARA RESPONDER ÀS PERGUNTAS ELABORADAS, UMA OU MAIS VEZES, MAS NÃO PRECISAM
APARECER NA ORDEM EM QUE ESTÃO RELACIONADOS
'''
############################################################################################
################################     Trabalho do G2   ######################################
#
# Giulia Orlandi - 2210383
# 
# Luisa Barragat Schneider - 2011398
# Maria Eduarda de Menezes Queiroz - 2320625
#
#Declaração de autoria: declaro que este documento foi produzido pelo grupo em sua totalidade,
#           sem consultas a outros alunos, professores ou qualquer outra pessoa.
############################################################################################


import pandas as pd
import matplotlib.pyplot as plt

print('\=================================')
print('\n Trabalhando com PANDAS \n')
print('\=================================')
'''
explicação do arquivo.......
.
.
.
'''
"""TRANSFORMANDO EM ARQUIVO EXCEL"""
# dfConverter = pd.read_csv("Base_de_Dados\\top_insta_influencers_data.csv", header= 0, index_col= 1)
# dfConverter.to_excel("Base_de_Dados\\top_insta_influencers_data.xlsx")

print('\n==============================================')
print('Questão 1\n')
#======================================================================
# Transformando o tipo do arquivo e renomeando as colunas do inglês para português
#======================================================================
dfInfluencers = pd.read_excel("Base_de_Dados\\top_insta_influencers_data.xlsx", header= 0 , index_col= 1)
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
# a) Filtrar influencers com mais de 1% de taxa de engajamento em 60 dias.
# b) Filtrar Pontuação acima de 90
# c) Filtrar influencers com mais de 1k postagens e da faixa total de likes de [70, 80).
#======================================================================
print('/n------------------------------------------------------')
print('5.a')
print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('5.b')
print('/n------------------------------------------------------')


print('/n------------------------------------------------------')
print('5.c')
print('------------------------------------------------------')


print('\n==============================================')
print('Questão 6 - Tabelas de Frequência\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('\n------------------------------------------------------')
print('6.a')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('6.b')
print('------------------------------------------------------')


print('\n==============================================')
print('Questão 7 - Gráficos\n')
#======================================================================
# a) gráfico de pizza que mostra os países da América (aí vai ter que 
# selecionar quem é da américa)
# b) gráfico de coluna que mostre seguidores no Brasil
#======================================================================
print('\n------------------------------------------------------')
print('7.a')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('7.b')
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


print('/n------------------------------------------------------')
print('9.c')
print('------------------------------------------------------')
