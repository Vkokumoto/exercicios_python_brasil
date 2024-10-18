# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a = 80000
pop_b = 200000
anos = 0

while True:
    anos +=1
    pop_a = pop_a + (pop_a * 0.03)
    pop_b = pop_b + (pop_b * 0.015)

    if pop_a >= pop_b:
        print(f'Demorou {anos} anos para que a população A ultrapasse ou iguale a população B')
        print(f'População A: {pop_a:.0f}')
        print(f'População B: {pop_b:.0f}')
        break
