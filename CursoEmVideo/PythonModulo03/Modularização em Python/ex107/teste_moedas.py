"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
from ex107 import moedas

num = float(input('Digite quanto você tem disponível: '))
var1 = int(input('Digite quantos por cento quer aumentar: '))
var2 = int(input('Digite quantos por cento quer diminuir: '))
print(f'Aumentar: {moedas.aumentar(num,var1)}')
print(f'Diminuir: {moedas.diminuir(num,var2)}')
print(f'Dobro: {moedas.dobro(num)}')
print(f'Metade: {moedas.metade(num)}')
print(help(moedas))
