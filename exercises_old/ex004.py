# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
inpt = input('Digite algo: ')
print('{} é {}'.format(inpt, type(inpt)))
print('Numérico: {}'.format(inpt.isnumeric()))
print('Alfabético: {}'.format(inpt.isalpha()))
print('Alfanumérico: {}'.format(inpt.isalnum())) 
print('Está em maiuscolas: {}'.format(inpt.isupper()))
print('Está em minuscolas: {}'.format(inpt.islower()))
print('Está capitalizada: {}'.format(inpt.istitle()))