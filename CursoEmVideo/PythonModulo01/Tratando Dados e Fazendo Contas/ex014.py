"""
Faça um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'verde':'\033[32m'}

temp = float(input('Digite a temperatura em ºC: '))
far = (temp * 1.8)+32

print('Calculando...')
sleep(2)

print(f"{cores["amarelo"]}{temp:.1f}{cores["limpa"]}ºC equivale a {cores["verde"]}{far:.1f}{cores["limpa"]}ºF.")
