# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Digite a área a ser pintada: '))

quantidade_tinta = area / 3

quantidade_lata = -(-quantidade_tinta // 18) 

preco = quantidade_lata * 80

print(f'Serão necessárias {quantidade_lata:.1f} latas de tinta')
print(f'O preço total será de R${preco:.2f}')