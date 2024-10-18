# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range (4):
    nota = float(input(f'Digite a nota {i + 1}: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'As notas digitadas foram: {notas}')
print(f'Média: {media}')