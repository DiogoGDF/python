'''
Um professor quer sortear um dos seus quatro alunos para apagar
o quadro. Faça um programa que ajude ele, lendo o nome deles e 
escrevendo o nome do escolhido
'''
import random

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
escolha = random.choice(alunos)

print('O aluno escolhido foi {}'.format(escolha))