"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'amarelo':'\033[1;33m'}

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

print('Calculando...')
sleep(2)

print(f'A área da parede é {cores["amarelo"]}{lar*alt:.2f}{cores["limpa"]}. E será necessário usar {cores["amarelo"]}{(lar*alt)/2:.1f}{cores["limpa"]} lata(s) de tinta')
