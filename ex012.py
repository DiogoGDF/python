# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com x% de desconto

preco = float(input('Preço: R$'))
desconto = int(input('Desconto (%): '))

desconto = desconto / 100
desconto = preco * desconto
print('Novo preço: R${}'.format(preco - desconto))