"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from time import sleep
from random import randint

vitorias = 0

print('Eu irei pensar em um número de 0 a 10 e você também')
print('Você tem que adivinhar se a soma dos dois números será PAR ou ÍMPAR')
while True:
    computador = randint(0,10)
    usuario = int(input('Digite um número de 0 a 10: '))   
    while usuario < 0 or usuario > 10:
        sleep(0.5)
        print('Valor inválido')
        usuario = int(input('Digite um número de 0 a 10: '))   
    soma = computador + usuario
    print('Digite [P] para par ou [I] para ímpar')
    divisao = str(input('Você quer par ou ímpar: ')).strip().upper()[0]    
    while divisao != "P" and divisao != "I":
        sleep(0.5)
        print('Opção inválida')
        print('Digite [P] para par ou [I] para ímpares')
        divisao = str(input('Você quer par ou ímpar: ')).strip().upper()[0]    
    if divisao == "P" and soma % 2 == 0:
        print('Analisando...')
        sleep(1)
        print(f'Você ganhou! Você pensou em {usuario} e eu pensei em {computador}, logo a soma deu {soma} que é par!')
        print('Vamos seguir jogando')
        sleep(0.5)
        vitorias += 1   
    elif divisao == "I" and soma % 2 != 0:
        print('Analisando...')
        sleep(1)
        print(f'Você ganhou! Você pensou em {usuario} e eu pensei em {computador}, logo a soma deu {soma} que é ímpar!')
        print('Vamos seguir jogando')
        sleep(0.5)
        vitorias += 1   
    elif divisao == "P" and soma % 2 != 0:
        print('Analisando...')
        sleep(1)
        print(f'Você perdeu! Você pensou em {usuario} e eu pensei em {computador}, logo a soma deu {soma} que é ímpar')
        break   
    elif divisao == "I" and soma % 2 == 0:
        print('Analisando...')
        sleep(1)
        print(f'Você perdeu! Você pensou em {usuario} e eu pensei em {computador}, logo a soma deu {soma} que é par')
        break
sleep(2)
print('Isso foi divertido...')
print(f'Ao total você venceu {vitorias} vezes')
