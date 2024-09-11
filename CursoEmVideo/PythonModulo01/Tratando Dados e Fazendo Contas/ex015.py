"""
Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
from time import sleep

print('\033[34m-=\033[m' * 20)
print('\033[1mLOCADORA DE CARROS\033[m')
print('\033[34m-=\033[m' * 20)

cores = {'limpa':'\033[m',
         'azul':'\033[34m'}

dias = float(input('Digite quantos dias você ficou com o carro: '))
km = float(input('Quantos quilômetros você percorreu com o carro: '))
valor = (dias*60)+(km*0.15)

print('Calculando...')
sleep(2)

print(f'Você deve pagar {cores["azul"]}{(valor):.2f}{cores["limpa"]} reais.')
