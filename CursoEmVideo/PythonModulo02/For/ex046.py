"""
Faça um programa que mostre na tela uma contagem regressiva para um estouro, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
import emoji

explosao = emoji.emojize(':collision:')

print('\033[1;31mCUIDADO\033[m')
sleep(1)

for i in range(10,-1,-1):
    print(i)
    sleep(1)

print(f'\033[1m{explosao}KABOOM{explosao}\033[m')
