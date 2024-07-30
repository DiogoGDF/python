'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

n = int(input('Digite um núemro: '))
print(n//1%10)
print(n//10%10)
print(n//100%10)
print(n//1000%10)