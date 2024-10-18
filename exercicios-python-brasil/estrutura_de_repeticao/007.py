# 7. Faça um programa que leia 5 números e informe o maior número.

num = []

for i in range (5):
    numero = int(input(f'Digite o {i + 1}° número: '))
    num.append(numero)

maior_num = max(num)

print(f'O maior número é: {maior_num}')
