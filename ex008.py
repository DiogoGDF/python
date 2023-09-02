# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input("Escreva uma distância em metros: "))

print("{}m corresponde a:".format(n))
print("{}km".format(n/1000))
print("{}hm".format(n/100))
print("{}dam".format(n/10))
print("{}dm".format(n*10))
print("{}cm".format(n*100))
print("{}mm".format(n*1000))