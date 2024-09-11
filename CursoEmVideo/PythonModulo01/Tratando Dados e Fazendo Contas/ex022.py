"""
Faça um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'azul':'\033[4;34m'}

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando...')
sleep(3)

print(f'Seu nome: {cores["azul"]}{nome}{cores["limpa"]}')
print(f'Seu nome em maiúsculas: {cores["azul"]}{nome.upper()}{cores["limpa"]}')
print(f'Seu nome em minúsculas: {cores["azul"]}{nome.lower()}{cores["limpa"]}')
print(f'Seu nome ao total tem {cores["azul"]}{len(nome) - nome.count(' ')}{cores["limpa"]} letras')
print(f'Seu primeiro nome é {cores["azul"]}{nome.split()[0]}{cores["limpa"]} e ao total ele tem {cores["azul"]}{len(nome.split()[0])}{cores["limpa"]} letras')
