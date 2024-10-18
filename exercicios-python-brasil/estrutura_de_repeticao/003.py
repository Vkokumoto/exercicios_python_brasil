# Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite seu nome: ')
while len(nome) < 4:
    nome = input('O nome deve ter pelo menos 4 caracteres, tente novamente: ')

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Valor inválido, tente novamente: '))

salario = float(input('Digite seu salário: '))
while salario < 0:
    salario = float(input('Valor inválido, tente novamente: '))

sexo = input('Digite seu sexo [M/F]: ').lower()
while sexo != 'f' and sexo != 'm':
    sexo = input('Valor inválido, tente novamente: ').lower()

estado_civil = input('Digite seu estado civil [S/C/V/D]: ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Valor inválido, tente novamente: ').lower()
