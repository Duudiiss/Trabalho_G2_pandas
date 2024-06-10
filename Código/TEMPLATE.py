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
# Renomeie as colunas do inglês para português
#======================================================================
dfInfluencers = pd.read_excel("top_insta_influencers_data.xlsx", header= 0 , index_col= 1)

dicRenomear = {'channel_info': 'Nome do Canal', 'influence_score': 'Pontuação', 
                               'posts': 'Numero de Postagens', 'followers': 'Numero de Seguidores', 
                               'avg_likes': 'Média de Curtidas', 'country': 'País', 
                              '60_day_eng_rate': 'Taxa de Engajamento em 60 dias (%)', 
                              'new_post_avg_like': 'Média de Curtidas em Novas Postagens',
                              'total_likes': 'Total de Curtidas'}

# print(dfInfluencers)

print('\n==============================================')
print('Questão 2 - Substituição de valores\n')
#======================================================================
# Substituir os valores que terminam em 'k', 'm', 'b', para numérico 
# ex: 6m = 6.000.000
#======================================================================
print('/n------------------------------------------------------')
print('2-')

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

print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('3.b')


print('------------------------------------------------------')




print('\n==============================================')
print('Questão 4 -  Criar Categorias em função do valor de uma coluna\n')
#======================================================================
# a) Crie e exiba a coluna 'Crescimento/Engajamento' que categoriza os influencers
# em 3 faixas de acordo com a coluna ‘Taxa de Engajamento em 60 dias’.
#
# b) Criar coluna ‘Faixa de Pontuação’ que categoriza os influencers em 
# 'Baixa', 'Média', 'Alta', 'Muito Alta' de acordo com a coluna ‘Pontuação’
# e exiba os influencers com pontuação 'Média'.
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
# a) Filtrar Pontuação acima de 90
# b) Filtrar os influencers com numeros no Nome do Canal 
# c) Filtrar os influencers com Curtidas maior que 1.000.000.000 e seguidores abaixo de 40.000.000.
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
# a) Tabela frequencia de influencers com baixo, médio e alto Crescimento/Engajamento.
# b) Tabela de frequencia de influencers por país.
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
# a) gráfico de barras que mostre a distribuição de influenciadores por país 
# b) gráfico de pizza que mostre a distribuição dos influenciadores nos países do continente americano.
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
# b) A partir da coluna ‘País’ agrupar os influencers e mostrar o total de 
# curtidas dos influencers brasileiros.
# c) Agrupar influencers por 'País' e 'Faixa de Pontuação' e exibir o total 
# de curtida de brasileiros por Faixas de Pontuação.
#======================================================================

print('------------------------------------------------------')
print('8.a')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('8.b')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('8.c')
print('------------------------------------------------------')

print('\n==============================================')
print('Questão 9\n')
#======================================================================
# c) Tabela de Frequência dos países com inflenciadores de Pontuação acima de 90
# d) Tabela de Frequência Percentual do Engajamento Diário dos 20 Primeiros 
# Influenciadores Estadunidenses.
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


print('/n------------------------------------------------------')
print('9.d')
print('------------------------------------------------------')
