"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
from time import sleep

while True:
    print('Digite o número que você gostaria de saber a tabuada')
    print('Para sair digite um valor um valor negativo')
    n = int(input('Digite um número: '))
    if n < 0:
        break
    else:
        print('Calculando...')
        sleep(2)
        c = 1
        for i in range(n, (n * 11), n):
            print(f'{c} x {n} = {i}')
            c +=1
    sleep(1)
print('Obrigado!')
