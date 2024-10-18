# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

for i in range (5):
    num = int(input(f'Digite o {i + 1}° número: '))
    lista.append(num)

print('\nOs números digitados foram:\n')

for i in lista:
    print(i)
    