# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

n = int(input('Digite um ângulo: '))

ang = math.radians(n)

sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))