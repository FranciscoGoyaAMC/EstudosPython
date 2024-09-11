"""
Faça um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""
from time import sleep

cidade = str(input('Digite a cidade em que você nasceu: '))

print('Analisando...')
sleep(2)

divisao = cidade.lower().strip().split()

if(divisao[0] == 'santo' or divisao[0] == 'santa' or divisao[0] == 'são' or divisao[0] == 'sao'):
    print('Você nasceu em uma cidade com nome de santo')
else:
    print('Você não nasceu em uma cidade com nome de santo')
