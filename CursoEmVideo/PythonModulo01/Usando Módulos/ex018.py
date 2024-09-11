"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import cos, sin, tan, radians
from time import sleep

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}

ang = float(input('Digite o ângulo desejado: '))

print('Calculando...')
sleep(2)

print(f'ÂNGULO {cores["azul"]}{ang}{cores["limpa"]} \n\n Seno: {cores["verde"]}{sin(radians(ang)):.2f}{cores["limpa"]} \n Cosseno {cores["amarelo"]}{cos(radians(ang)):.2f}{cores["limpa"]} \n Tangente {cores["vermelho"]}{tan(radians(ang)):.2f}{cores["limpa"]}')
