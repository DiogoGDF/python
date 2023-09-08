# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o seu salário atual? R$'))
aumento = int(input('Quantos % será aumentado o salário? '))

aumento = aumento / 100
aumento = salario * aumento
sal_final = salario + aumento

print('Salário final: R${}'.format(sal_final))