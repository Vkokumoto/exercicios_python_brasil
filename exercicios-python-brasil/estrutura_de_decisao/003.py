# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite o seu sexo: ').upper()

if sexo == 'F':
    print('Sexo feminino')
elif sexo == 'M':
    print('Sexo masculino')
else:
    print('Sexo inválido')
