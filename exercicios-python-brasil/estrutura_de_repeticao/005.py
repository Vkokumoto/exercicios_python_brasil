# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    pop_a = int(input('Digite o valor da população A: '))
    pop_b = int(input('Digite o valor da população B: '))
    cresc_a = float(input('Digite a taxa de crescimento anual da população A: '))
    cresc_b = float(input('Digite a taxa de crescimento anual da população B: '))
    anos = 0

    while True:
        anos +=1
        pop_a = pop_a + (pop_a * (cresc_a / 100))
        pop_b = pop_b + (pop_b * (cresc_b / 100))

        if pop_a >= pop_b:
            print(f'Demorou {anos} anos para que a população A ultrapasse ou iguale a população B')
            print(f'População A: {pop_a:.0f}')
            print(f'População B: {pop_b:.0f}')
            break
    
    continuar = input('Deseja continuar [S/N]? ').lower()
    if continuar == 's':
        continue
    elif continuar == 'n':
        print('Finalizando o programa')
        break
