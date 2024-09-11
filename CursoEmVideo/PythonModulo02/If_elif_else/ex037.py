"""
Faça um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 
"""
from time import sleep

print('\033[1;34m-=\033[m' * 9)
print('\033[30mCONVERSOR DE BASES\033[m')
print('\033[1;34m-=\033[m' * 9)

sleep(2)

cores = {'limpa':'\033[m',
        'vermelho':'\033[31m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'ciano':'\033[36m'}

while True:
    n = int(input('Digite um número inteiro: '))
    conversor = 0
    resposta = 'não'

    while (conversor < 1) or (conversor > 3):
        sleep(1)
        print('Digite 1 para converter para base binária')
        print('Digite 2 para converter para base octal')
        print('Digite 3 para converter para base hexadecimal')
        conversor = int(input('Para qual base gostaria de converter? '))

        if conversor == 1:
            print('Calculando...')
            sleep(2)
            print(f'O valor {cores["vermelho"]}{n}{cores["limpa"]} em base binária fica {cores["roxo"]}{bin(n)[2:]}{cores["limpa"]}')
        elif conversor == 2:
            print('Calculando...')
            sleep(2)
            print(f'O valor {cores["vermelho"]}{n}{cores["limpa"]} em base octal fica {cores["ciano"]}{oct(n)[2:]}{cores["limpa"]}')
        else:
            print('Calculando...')
            sleep(2)
            print(f'O valor {cores["vermelho"]}{n}{cores["limpa"]} em base hexadecimal fica {cores["azul"]}{hex(n)[2:]}{cores["limpa"]}')

    resposta = str(input('Digite sim caso deseje sair do programa: ')).strip().lower()

    if resposta == 'sim':
        break
