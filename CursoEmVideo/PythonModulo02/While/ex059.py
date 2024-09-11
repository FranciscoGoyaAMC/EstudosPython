"""
Faça um programa que leia dois valores e mostre um menu na tela para somar, multiplicar, ver maior número, alterar os números, sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso
"""
from time import sleep

opcao = 0
val1 = int(input('Digite o primeiro número: '))
val2 = int(input('Digite o segundo número: '))

while opcao != 5:
    print('Digite [1] para somar')
    print('Digite [2] para multiplicar')
    print('Digite [3] para analisar qual o maior')
    print('Digite [4] para alterar os números')
    print('Digite [5] para sair do programa')
    opcao = int(input('Digite sua opção: '))
    sleep(1)
    if opcao < 1 or opcao > 5:
        print('Opcão inválida')
    if opcao == 1:
        soma = val1 + val2
        print('Calculando...')
        sleep(2)
        print(f'A soma entre {val1} e {val2} é {soma}')
    if opcao == 2:
        mult = val1 * val2
        print('Calculando...')
        sleep(2)
        print(f'A multiplicação entre {val1} e {val2} é {mult}')
    if opcao == 3:
        print('Analisando...')
        sleep(2)
        if val1 > val2:
            print(f'O primeiro número digitado ({val1}) é maior que o segundo número digitado ({val2})')
        if val1 < val2:
            print(f'O segundo número digitado ({val2}) é maior que o primerio número digitado ({val1})')
        else:
            print('Os número são iguais')
    if opcao == 4:
        sleep(2)
        val1 = int(input('Digite o primeiro número: '))
        val2 = int(input('Digite o segundo número: '))
