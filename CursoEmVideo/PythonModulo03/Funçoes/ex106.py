"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
from time import sleep

cores = {'limpa':'\033[m',
         'ciano':'\033[;36m'}

def titulo(msg):
    print(f'{cores["ciano"]}-'*len(msg))
    print(msg)
    print(f'-'*len(msg))
    print(cores["limpa"])
    sleep(1)


def ajuda(txt):
    titulo(f'Acessando manual do comando {txt}')
    sleep(1)
    help(txt)
    sleep(1)


while True:
    titulo('AJUDANTE VIRTUAL')
    ajd = str(input('Digite a biblioteca ou função da qual gostaria de ter informações, ou digite fim para sair: '))
    if ajd.strip().lower() == 'fim':
        break
    else:
        ajuda(ajd)
titulo('Obrigado! Espero ter ajudado')