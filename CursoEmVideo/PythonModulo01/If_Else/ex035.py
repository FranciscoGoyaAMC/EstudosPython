"""
Faça um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
from time import sleep

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

print('Calculando...')
sleep(3)

if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('Essas retas não formam um triângulo.')
else:
    print('Essas retas formam um triângulo.')
