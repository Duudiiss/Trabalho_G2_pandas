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
dfInfluencers.rename(columns= {'channel_info': 'Nome do Canal', 'influence_score': 'Pontuação', 'posts': 'Numero de Postagens', 
                              'followers': 'Numero de Seguidores', 'avg_likes': 'Média de Curtidas', 
                              '60_day_eng_rate': 'Taxa de Engajamento em 60 dias', 'new_post_avg_like': 'Média de Curtidas em Novas Postagens',
                              'total_likes': 'Total de Curtidas', 'country': 'País'}, inplace = True)

print(dfInfluencers)

print('\n==============================================')
print('Questão 2 - Substituição de valores\n')
#======================================================================
# Substituir os ‘m’ por 1000000 ex: 6m = 6.000.000
#======================================================================
print('/n------------------------------------------------------')
print('2-')

# Arrumar um jeito de converter essa coluna para numérico

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

# media = dfInfluencers['Média de Curtidas em Novas Postagens'].mean()
# print(media)
# dfInfluencers['Média de Curtidas em Novas Postagens'].fillna(media)

print('------------------------------------------------------')




print('\n==============================================')
print('Questão 4 -  Criar Categorias em função do valor de uma coluna\n')
#======================================================================
# a) Criar coluna ‘faixa total de likes’ que categoriza os influencers em 
# 3 faixas de acordo com a coluna ‘total likes’.
# b) Criar coluna ‘faixa de pontuação’ que categoriza os influencers de 
# acordo com a coluna ‘influencer score’.
#======================================================================
print('/n------------------------------------------------------')
print('4.a')
print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('4.b')
print('------------------------------------------------------')


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
# a) Mostrar valores minimo, maximo e médio da coluna Pontuação
# b) A partir da coluna ‘posts’ pensar em agrupar os influencers pela 
# quantidade de posts. Mostrar influencers que postam muitos posts.
# c) Agrupar influencers pelo país e pela coluna faixa de pontuação.
#======================================================================

print('------------------------------------------------------')
print('8.a')
print('------------------------------------------------------')
print(dfInfluencers['Numero de Postagens']].agg(['min','max', 'mean']))

print('\n------------------------------------------------------')
print('8.b')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('8.c')
print('------------------------------------------------------')



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
