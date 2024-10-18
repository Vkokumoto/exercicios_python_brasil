# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input('Digite a área a ser pintada: '))

quantidade_tinta = area / 6

# Opção 1
quantidade_lata = -(-quantidade_tinta // 18)
preco_lata = quantidade_lata * 80

# Opção 2
quantidade_galao = -(-quantidade_tinta // 3.6)
preco_galao = quantidade_galao * 25

# Opção 3
lata_mistura = quantidade_tinta // 18
restante = quantidade_tinta - (lata_mistura * 18)
galao_mistura = -(-restante // 3.6)
preco_mistura = (lata_mistura * 80) + (galao_mistura * 25)

print(f'Apenas latas de 18L: {quantidade_lata} latas, Preço: R$ {preco_lata:.2f}')
print(f'Apenas galões de 3.6L: {quantidade_galao} galões, Preço: R$ {preco_galao:.2f}')
print(f'Mistura: {quantidade_lata} latas e {quantidade_galao} galões, Preço: R$ {preco_mistura:.2f}')

