"""
Faça um programa que faça o computador jogar Jokenpô com você
"""
from time import sleep
from random import choice

while True:
    print('\033[1;34m-=\033[m' * 11)
    print('\033[1;30mPEDRA PAPEL OU TESOURA\033[m')
    print('\033[1;34m-=\033[m' * 11)

    resposta = "S"
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    escolhido = choice(opcoes)
    jogador = str(input('Pedra, papel ou tesoura? ')).strip().upper()

    while (jogador != 'PEDRA') and (jogador != 'PAPEL') and (jogador != 'TESOURA'):
        print('')
        print('OPÇÃO INVÁLIDA')
        jogador = str(input('Pedra, papel ou tesoura? ')).strip().upper()
    
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)

    if (jogador == escolhido):
        print(f'Deu empate. Eu escolhi {escolhido} também.')
    elif (jogador == 'PEDRA') and (escolhido == 'PAPEL'):
        print(f'Você perdeu... eu escolhi {escolhido}.')
    elif (jogador == 'TESOURA') and (escolhido == 'PEDRA'):
        print(f'Você perdeu... eu escolhi {escolhido}.')
    elif (jogador == 'PAPEL') and (escolhido == 'TESOURA'):
        print(f'Você perdeu... eu escolhi {escolhido}.')
    else:
        print(f'Parabéns! Você ganhou, eu escolhi {escolhido}.')
    
    print('')
    resposta = str(input('Isso foi divertido! Você quer jogar de novo?[S/N] ')).strip().upper()[:0]
    if resposta == "N":
        print('')
        print('Obrigado pelo jogo! Até a próxima.')
        break
