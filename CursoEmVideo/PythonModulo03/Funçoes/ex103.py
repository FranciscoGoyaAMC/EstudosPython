"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(n='default', g=0):
    return f'O jogador {n} fez {g} gols no campeonato'


nome = str(input('Informe o nome do jogador: '))
gols = str(input('Informe o número de gols feitos: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome,gols))
