#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:41:23 2023

@author: diogo
"""
import pandas as pd

# Dataframe = tabela no python

# Craindo um dataframe vazio:
# dataframe = pd.DataFrame()

# Criando um dataframe a partir de um dicionário:
venda = {
        'data': ['15/02/2021', '16/02/2021'],
        'valor': [500, 300],
        'produto': ['feijão', 'arroz'],
        'qtde': [50, 70],
        }
tabela_vendas = pd.DataFrame(venda)
print(tabela_vendas)

# Importando um dataframe de uma base de dados:
vendas_df = pd.read_excel("Vendas.xlsx")

# Métodos de visualização da tabela
#print(vendas_df)
#print(vendas_df.head())
#print(vendas_df.shape)
#print(vendas_df.describe())

