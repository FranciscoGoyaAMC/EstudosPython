"""
Faça um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
"""
n = int(input("Digite 999 para sair ou digite qualquer outro número para seguir: "))
soma = 0
digitados = 0
while n != 999:
    soma = soma + n
    n = int(input("Digite 999 para sair ou digite qualquer outro número para seguir: "))
    digitados += 1
print(f'Ao total você digitou {digitados} números e soma de todos eles é {soma}')
