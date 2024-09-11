"""
Faça um programa em que o computador “pense” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

print('Irei pensar em um número de 0 a 5 e você terá de adivinhar.')
n = randint(0,5)
sleep(3)
print('Pronto!')

numero = int(input('Em qual número eu estou pensando? '))
sleep(1)

if n == numero:
    print(f'Parabens, o número era {n}! Você acertou!')
else:
    print(f'Sinto muito, o número era {n}. Você errou.')
