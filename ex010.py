# Crie um programa que leia o quanto dinheiro uma pessoa quer converter de reais para dolares, e o converta.
from forex_python.converter import CurrencyRates

c = CurrencyRates()

rs = float(input('R$ para conversão: '))
usd = c.convert('BRL', 'USD', rs)

print('{} = {} USD'.format(rs, usd))