# Escreva um programa que converta uma temperatura digitada em °C, e converta em °F

cel  = float(input('Temperatura em °C: '))

far = (cel * 9)/5 + 32

print('{}°C = {}°F'.format(cel, far))