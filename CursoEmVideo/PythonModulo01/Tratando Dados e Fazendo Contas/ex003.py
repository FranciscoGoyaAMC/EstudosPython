"""
Faça um programa que leia dois números e mostre a soma entre eles.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}

n1 = int(input('Digite um valor: '))
n2 = int(input('Digte outro valor: '))

print('Calculando...')
sleep(2)

s = n1 + n2

print(f'A soma entre {cores["amarelo"]}{n1}{cores["limpa"]} e {cores["amarelo"]}{n2}{cores["limpa"]} é {cores["vermelho"]}{s}{cores["limpa"]}')
