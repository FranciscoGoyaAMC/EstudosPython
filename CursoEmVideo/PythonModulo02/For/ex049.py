"""
Refaça o exercício 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
"""
from time import sleep

while True:
    print('\033[1;34m-=\033[m' * 15)
    print('\033[1;30mTABUADA AUTOMÁTICA\033[m')
    print('\033[1;34m-=\033[m' * 15)

    sleep(1)
    
    resposta = "S"
    c = 1
    n = int(input('Digite o número que você gostaria de saber a tabuada: '))

    print('Calculando...')
    sleep(2)

    for i in range(n , (n*11), n):
        print(f'{n} x {c} = {i}')
        c += 1
        sleep(0.3)

    resposta = str(input('Gostaria de calcular mais algum número? ')).strip().upper()[:0]
    if resposta == "N":
        break
