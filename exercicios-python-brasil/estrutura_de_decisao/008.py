# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input('Preço 1: '))
prod2 = float(input('Preço 2: '))
prod3 = float(input('Preço 3: '))

if prod1 < prod2 and prod1 < prod3:
    print('O produto mais barato é o 1°')
elif prod2 < prod1 and prod2 < prod3:
    print('O produto mais barato é o 2°')
else:
    print('O produto mais barato é o 3°')