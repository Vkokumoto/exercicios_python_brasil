# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite sua altura: '))

peso_ideal = (72.7 * altura) - 58

print(f'O peso ideal de uma pessoa com {altura}m de altura é {peso_ideal:.1f}kg')
