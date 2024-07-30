# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número: '))

print('Você digitou:', n)
print('O antecessor de {} é {}'.format(n, n - 1))
print('O sucessor de {} é {}'.format(n, (n + 1)))