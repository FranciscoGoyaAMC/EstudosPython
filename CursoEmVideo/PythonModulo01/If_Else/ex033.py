"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
from time import sleep

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um segundo número inteiro: '))
n3 = int(input('Digite um terceiro número inteiro: '))

print('Analisando...')
sleep(3)

if (n1 > n2 and n2 > n3):
    print(f'O maior número digitado foi {n1}. E o menor foi {n3}.')
elif (n1 > n2 and n2 < n3 and n1 > n3):
    print(f'O maior número digitado foi {n1}. E o menor foi {n2}.')
elif (n2 > n1 and n1 > n3):
    print(f'O maior número digitado foi {n2}. E o menor foi {n3}.')
elif (n2 > n1 and n1 < n3 and n2 > n3):
    print(f'O maior número digitado foi {n2}. E o menor foi {n1}.')
elif (n3 > n1 and n1 > n2):
    print(f'O maior número digitado foi {n3}. E o menor foi {n2}.')
elif (n3 > n1 and n1 < n2 and n2 < n3):
    print(f'O maior número digitado foi {n3}. E o menor foi {n1}.')
