"""
Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1

while c <= 10:
    print(n, end=' > ')
    n = n + r
    c += 1
print('Fim')
