"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot
from time import sleep

cores = {'limpa':'\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m'}

cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))

print('Calculando...')
sleep(2)

print(f'Com o cateto oposto sendo {cores["verde"]}{cat_op}{cores["limpa"]} e cateto adjacente sendo {cores["amarelo"]}{cat_adj}{cores["limpa"]}, a hipotenusa será {cores["vermelho"]}{hypot(cat_op,cat_adj):.2f}{cores["limpa"]}')
