"""
Faça um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
Quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares.
"""
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite um último número: ')))

print(f'Você digitou os números {n}')

print(f'Você digite o número 9 {n.count(9)} vez(es)')

if 3 in n:
    print(f'Você digitou o número 3 na {n.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado nenhuma vez')

print('Os números pares digitados foram ', end='')
for i in n:
    if i % 2 == 0:
        print(f'{i} ', end=' ')
