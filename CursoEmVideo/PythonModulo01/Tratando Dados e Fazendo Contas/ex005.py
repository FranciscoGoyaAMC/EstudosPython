"""
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'amarelo':'\033[1;33m',
         'verde':'\033[1;32m'}

n = int(input('Digite um valor: '))

print('Analisando...')
sleep(2)

print(f'O valor digitado foi {cores["amarelo"]}{n}{cores["limpa"]}. Antes dele vem {cores["verde"]}{n-1}{cores["limpa"]}, e após ele vem {cores["verde"]}{n+1}{cores["limpa"]}')
