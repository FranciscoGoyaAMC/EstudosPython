"""
Faça um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
from time import sleep

numero = int(input('Digite um número inteiro: '))

print('Analisando...')
sleep(2)

if numero % 2 == 0:
    print('O número digitado é par.')
else:
    print('O número digitado é ímpar.')
