"""
Faça um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

maior_dado = 0
colocaçao = 1
vencedor = ''

ranking = []
jogadores = {'Jogador 1' : randint(1,6),
             'Jogador 2' : randint(1,6),
             'Jogador 3' : randint(1,6),
             'Jogador 4' : randint(1,6)}

for i in jogadores:
    print(f'{i} tirou {jogadores[i]}')
    sleep(1)
    if jogadores[i] > maior_dado:
        maior_dado = jogadores[i]
        vencedor = i
print(f'O jogador {vencedor} é o vencedor. Após tirar {maior_dado} no dado')

sleep(1.5)

print('RANKING')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for j, d in ranking:
    print(f'{colocaçao}º lugar: {j} com {d}')
    colocaçao += 1
