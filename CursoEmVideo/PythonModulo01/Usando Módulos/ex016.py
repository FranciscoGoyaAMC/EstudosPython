"""
Faça um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
from math import trunc

cores= {'limpa':'\033[m',
        'vermelho':'\033[31m'}

num = float(input('Digite um número com ponto flutuante: '))

print(f'A parte inteira do valor {cores["vermelho"]}{num}{cores["limpa"]} é {cores["vermelho"]}{trunc(num)}{cores["limpa"]}')
