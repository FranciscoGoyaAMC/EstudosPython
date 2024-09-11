"""
Faça um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
menor_numero = numeros[0]
maior_numero = numeros[0]

for c in range(0,5):
    if maior_numero < numeros[c]:
        maior_numero = numeros[c]
    if menor_numero > numeros[c]:
        menor_numero = numeros[c]

print(f'Os números sorteados são {numeros}')
print(f'O maior número sorteado foi {maior_numero}')
print(f'O menor número sorteado foi {menor_numero}')
