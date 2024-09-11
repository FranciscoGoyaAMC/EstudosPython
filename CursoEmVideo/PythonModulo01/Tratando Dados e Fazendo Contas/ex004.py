"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'reverso':'\033[7m'}

val = input('Digite algo: ')

print('Analisando...')
sleep(2)

print(f'Só tem espaços? {cores["reverso"]}{val.isspace()}{cores["limpa"]}')
print(f'É um número? {cores["reverso"]}{val.isnumeric()}{cores["limpa"]}')
print(f'É alfabético? {cores["reverso"]}{val.isalpha()}{cores["limpa"]}')
print(f'É alfanumérico? {cores["reverso"]}{val.isalnum()}{cores["limpa"]}')
print(f'Está somente em maiúscula? {cores["reverso"]}{val.isupper()}{cores["limpa"]}')
print(f'Está somente em minúscula? {cores["reverso"]}{val.islower()}{cores["limpa"]}')
print(f'Está capitalizada? {cores["reverso"]}{val.istitle()}{cores["limpa"]}')
