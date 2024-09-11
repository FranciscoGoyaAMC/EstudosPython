"""
Refaça o exercício 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
"""
from time import sleep

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

print('Calculando...')
sleep(3)

if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('Essas retas não formam um triângulo.')
elif (r1 == r2) and (r2 == r3):
    print('Essas retas formam um triângulo equilátero.')
elif(r1 == r2) or (r1 == r3) or (r2 == r3):
    print('Essas retas formam um triângulo isósceles.')
else:
    print('Essas retas formam um triângulo escaleno.')
