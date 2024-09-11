"""
Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
from time import sleep

limite = 80
velocidade = int(input('Qual a velocidade do carro? '))

print('Analisando...')
sleep(2)

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print(f'Você o limite de velocidade é {limite}. Você foi multado.')
    print(f'Você deverá pagar {multa} reais.')
else:
    print('Você está dentro do limite de velocidade.')
