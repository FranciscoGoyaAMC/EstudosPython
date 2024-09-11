"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m'}

numero = int(input('Digite um valor de 0 a 9999: '))

print('Analisando...')
sleep(2)

if (numero > 9999 or numero < 0):
    print('Número não está dentro do alcance solicitado. Tente novamente.')
else:
    print(f'Unidade: {cores["vermelho"]}{numero // 1 % 10}{cores["limpa"]}')
    print(f'Dezena: {cores["vermelho"]}{numero // 10 % 10}{cores["limpa"]}')
    print(f'Centena: {cores["vermelho"]}{numero // 100 % 10}{cores["limpa"]}')
    print(f'Milhar: {cores["vermelho"]}{numero // 1000 % 10}{cores["limpa"]}')
