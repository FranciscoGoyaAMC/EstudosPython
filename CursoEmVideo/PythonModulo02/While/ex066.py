"""
Faça um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
soma = 0
contador = 0

while True:
    n = int(input('Digite 999 para sair ou digite qualquer outro número para seguir: '))
    if n == 999:
        break
    else:
        soma += n
        contador += 1
print(f'Você digitou {contador} números e a soma de todos eles é {soma}')
