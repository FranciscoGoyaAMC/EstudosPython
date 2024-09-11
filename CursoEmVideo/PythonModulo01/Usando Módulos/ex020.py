"""
 O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle
from time import sleep

cores = {'limpa':'\033[m',
         'azul':'\033[4;34m'}

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]

shuffle(lista)

print('Processando...')
sleep(2)

print(f'A ordem sorteada é {cores["azul"]}{lista}{cores["limpa"]}')
