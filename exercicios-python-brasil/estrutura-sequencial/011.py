# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print(f'O produto do dobro de {num1} com a metade de {num2} é {a}')
print(f'A soma do triplo de {num1} com {num3} é {b}')
print(f'{num3} elevado ao cubo é {c}')
