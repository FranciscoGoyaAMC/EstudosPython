"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint

def sorteia(l):
    for i in range(0,5):
        l.append(randint(0,10))

def soma_par(n):
    soma = 0
    for i in range(0,len(n)):
        if n[i] % 2 == 0:
            soma += n[i]
    print(f'A soma dos valores pares da lista é {soma}')


numeros = []
sorteia(numeros)
print(f'Os valores sorteados são: {numeros}')
soma_par(numeros)
