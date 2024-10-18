# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

dinheiro = float(input('Digite quanto você ganha por hora: '))
horas = float(input('Digite quantas horas você trabalha por mês: '))

salario = horas * dinheiro

print(f'Você trabalhou {horas} horas esse mês e ganhou um salário de R${salario}')
