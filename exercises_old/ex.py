import os
os.system('clear')

n = int(input('Digite um numero: '))

if n % 2 == 0:
    print('par')
else:
    print('impar')

print('\n')

idade = int(input('Digite sua idade: '))

if 0 <= idade <= 12:
    print('criança')
elif 13 <= idade <= 18:
    print('adolescente')
elif idade > 18:
    print('adulto')
else:
    print('idade inválida')

print('\n')

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

if x > 0 and y > 0:
    print('primeiro quadrante')
elif x < 0 and y > 0:
    print('segundo quadrante')
elif x < 0 and y < 0:
    print('terceiro quadrante')
elif x > 0 and y < 0:
    print('quarto quadrante')
else:
    print('eixo, ou origem')