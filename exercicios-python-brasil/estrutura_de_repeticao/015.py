# 15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input('Digite quantos termos da sequência de Fibonacci você deseja: '))

a, b = 0, 1

print(a)
print(b)

for _ in range (2, n):
    c = a + b
    print(c)
    a, b = b, c
    