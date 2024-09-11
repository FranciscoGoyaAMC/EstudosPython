"""
Faça um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
s = 0
n = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
decimo = n + (10 - 1) * r
print('Os 10 primeiros termos da razão são: ')

for i in range(n, (decimo + r), r):
    print('{i}'.format(i), end = ' > ')
print('Fim')
