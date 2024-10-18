# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
qte = 5

for i in range (5):
    num = float(input(f'Digite o {i + 1}° número: '))
    soma += num

media = soma / qte

print(f'Soma: {soma}')
print(f'Média: {media}')
