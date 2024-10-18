# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

dinheiro = float(input('Digite quanto você ganha por hora: '))
horas = float(input('Digite quantas horas você trabalha por mês: '))

salario_bruto = horas * dinheiro

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Salário bruto: R${salario_bruto:.2f}')
print(f'IR (11%): R${ir:.2f}')
print(f'INSS (8%): R${inss:.2f}')
print(f'Sindicato (5%): R${sindicato:.2f}')
print(f'Salário líquido: R${salario_liquido:.2f}')