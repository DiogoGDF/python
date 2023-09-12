'''
Faça um programa que leia o comprimento do 
cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.
'''
from math import sqrt, hypot

# sol 1
print('Solução 1:')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = sqrt(co * co + ca * ca)
print('A hipotenusa vai medir {:.2f}\n'.format(h))

# sol 2
print('Solução 2:')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))