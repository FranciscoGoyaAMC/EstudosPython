"""
Faça um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
"""
from time import sleep

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}

while True:
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite outro número inteiro: '))
    resposta = 'não'

    print('Analisando...')
    sleep(2)

    if (num1 > num2):
        print(f'{cores['azul']}{num1}{cores['limpa']}, primeiro valor digitado, é maior que {cores['vermelho']}{num2}{cores['limpa']}, segundo valor digitado')
    elif (num2 > num1):
        print(f'{cores['azul']}{num2}{cores['limpa']}, segundo valor digitado, é maior que {cores['vermelho']}{num1}{cores['limpa']}, primeiro valor digitado')
    elif (num1 == num2):
        print('Os números são iguais')

    sleep(1)
    
    resposta = str(input('Digite sim caso deseje sair do programa: ')).strip().lower()
    if (resposta == 'sim'):
        break
