# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. Os números impressos devem ter a mesma quantidade de digitos (em outras palavras, o = deve estar sempre na mesma posição)

n = int(input('Digite um núemro inteiro: '))

for i in range(1, 11):
    print('{} x {:02} = {:02}'.format(n, i, n*i))