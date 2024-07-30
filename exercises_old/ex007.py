# Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre sua média de acordo com as regras da Unisinos lembrando que GA vale 30% e o GB vale 70%

ga = float(input('Nota do GA: ')) * 0.3
gb = float(input('Nota do GB: ')) * 0.7
media = ga + gb

print('A média do aluno é {:.1f}'.format(media))