"""
Faça um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""
cores = {'limpa':'\033[m',
         'azul':'\033[34m'}

nome = str(input('Digite seu nome completo: '))

print(f'Seu nome tem Silva? {cores["azul"]}{"silva" in nome.lower()}{cores["limpa"]}')
