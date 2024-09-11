"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

i = int(input('Quantos jogos você gostaria de simular? '))
for j in range(0,i):
    print('---------------------')
    cont = 0
    jogos = []
    while True:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    print(f'Jogo {j+1}: {jogos}')
    sleep(1)
print('------Boa Sorte------')
