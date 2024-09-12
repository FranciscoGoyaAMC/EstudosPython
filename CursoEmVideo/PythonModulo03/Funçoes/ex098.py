"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep

def escreva(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))

def contador(inicio, fim, passo):
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1
    escreva(f'Contando de {inicio} até {fim} andando de {passo} em {passo}')
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c}', end=' ', flush=True)
            c += passo
            sleep(0.5)
    else:
        c = inicio
        while c >= fim:
            print(f'{c}', end=' ', flush=True)
            c -= passo
            sleep(0.5)
    print('Fim')


contador(1,10,1)
contador(10,0,2)
escreva('Agora é a sua vez!')

inicio = int(input('A partir de que número devo contar? '))
fim = int(input('Até que número devo contar? '))
passo = int(input('De quantos em quantos números devo contar? '))

contador(inicio, fim, passo)
