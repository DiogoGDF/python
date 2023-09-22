'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo" 
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
if (cidade[:5].lower == 'santo'):
    print('Ela começa com Santo!')
else:
    print('Ela não começa com Santo :(')