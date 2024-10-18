# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Digite o tamanho do arquivo (em MB): '))
velocidade = float(input('Digite a velocidade da sua internet (em Mbps): '))

tempo_segundo = (tamanho * 8) / velocidade
tempo_minuto = tempo_segundo / 60

print(f'Um arquivo de {tamanho}MB levará aproximadamente {tempo_minuto:.2f} minutos para ser baixado')