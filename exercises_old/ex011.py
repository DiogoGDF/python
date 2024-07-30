# Faça um programa que leia a largura e altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
print('A área da parede é de {}m²'.format(altura))

litros = area / 2
print('Você precisa de {:.2f} litros de tinta para pintar essa parede'.format(litros))