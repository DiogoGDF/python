'''
Crie um programa que leia um número real qualquer pelo teclado e
mostre na tela a sua porção inteira.
ex: 6.127 -> 6
'''

# Maneira 1 - importando módulo
from math import floor
n1 = float(input('Digite um número com vírgula: '))
print('Sua parte inteira é {}'.format(floor(n1)))

# Maneira 2 - usando int
n2 = float(input('Digite outro número com vírgula: '))
print('Sua parte inteira é {}'.format(int(n2)))