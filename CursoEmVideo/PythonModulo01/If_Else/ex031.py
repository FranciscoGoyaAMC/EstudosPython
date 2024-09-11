"""
Faça um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
from time import sleep

distancia = int(input("Qual a distancia viajada em km's? "))

print('Analisando...')
sleep(3)

if distancia > 200:
    print(f'O valor da passagem é {distancia * 0.45}')
else:
    print(f'O valor da passagem é {distancia * 0.5}')
