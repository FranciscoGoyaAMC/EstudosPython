"""
Faça um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m'}

nota1 = float(input('Digite o valor da nota 1: '))
nota2 = float(input('Digite o valor da nota 2: '))
media = (nota1+nota2)/2

print('Calculando...')
sleep(2)

print(f'A média das notas {cores["amarelo"]}{nota1:.2f}{cores["vermelho"]} e {cores["amarelo"]}{nota2:.2f}{cores["limpa"]} é {cores["vermelho"]}{media:.2f}{cores["limpa"]}.')
