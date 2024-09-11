"""
Faça um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
from time import sleep

cores = {'limpa':'\033[m',
      'azul':'\033[1;34m',
      'verde':'\033[1;32m',
      'amarelo':'\033[1;33m',
      'vermelho':'\033[1;31m'}

n = int(input('Digite um número: '))

print('Analisando...')
sleep(2)

print(f'O número digitado é {cores["azul"]}{n}{cores["limpa"]}. Seu dobro é {cores["verde"]}{n*2}{cores["limpa"]}. Seu triplo é {cores["amarelo"]}{n*3}{cores["limpa"]}. Sua raiz quadrada é {cores["vermelho"]}{n**(1/2):.2f}{cores["limpa"]}.')
