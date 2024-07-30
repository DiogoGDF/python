'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúscolas e mínuscolas
    - Quantas letras ao todo (sem contar os espaços)
    - Quantas letras tem o primeiro nome
'''

nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())

letras = nome.replace(' ', '')
print(len(letras))

print(nome.index(' '))