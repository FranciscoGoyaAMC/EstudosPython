"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""
from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando...')
sleep(2)

divisao = nome.split()

print(f'Seu primeiro nome é {divisao[0]}')
print(f'Seu último nome é {divisao[len(divisao) - 1]}')
