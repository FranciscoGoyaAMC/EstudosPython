"""
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'amarelo':'\033[33m'}

frase = str(input('Digite uma frase: ')).strip().lower()

print('Analisando...')
sleep(2)

print(f'A letra \033[4;31mA\033[m aparece {cores["amarelo"]}{frase.count("a")}{cores["limpa"]} vezes nessa frase.')
print(f'A \033[4;31mprimeira letra A\033[m apareceu na posição {cores["amarelo"]}{frase.find("a")+1}{cores["limpa"]}')
print(f'A \033[4;31múltima letra A\033[m apareceu na posição {cores["amarelo"]}{frase.rfind("a")+1}{cores["limpa"]}')
