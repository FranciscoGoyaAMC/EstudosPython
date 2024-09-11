"""
Faça um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'azul':'\033[34m'}

cidade = str(input('Digite em que cidade você nasceu: ')).strip()

print('Analisando...')
sleep(2)

print(f'Sua cidade começa com Santo: {cores['azul']}{cidade[:5].lower() == "santo"}{cores['limpa']}')
