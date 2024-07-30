# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

n = int(input('Digite um número: '))

print('O dobro de {} é {}'.format(n, n+n))
print('O triplo de {} é {}'.format(n, n*3))
print('A raiz quadrada de {} é {}'.format(n, math.sqrt(n)))