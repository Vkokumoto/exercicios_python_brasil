# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite mais um número: '))

if num1 > num2 and num1 > num3:
    print(f'Maior: {num1}')
elif num2 > num1 and num2 > num3:
    print(f'Maior: {num2}')
else:
    print(f'Maior: {num3}')

if num1 < num2 and num1 < num3:
    print(f'Menor: {num1}')
elif num2 < num1 and num2 < num3:
    print(f'Menor: {num2}')
else:
    print(f'Menor: {num3}')