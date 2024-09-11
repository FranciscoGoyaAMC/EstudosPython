"""
Faça um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
boletim = []
dados = []
while True:
    resposta = "a"
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1] + dados[2]) / 2)
    boletim.append(dados[:])
    dados.clear()
    while resposta not in 'SN':
        resposta = str(input('Deseja seguir cadastrando? [S/N] ')).strip().upper()[0]
    if resposta == "N":
        break
print("-"*10)
print(f"{'No':<4}{'NOME':<10}{'MÉDIA':>8}")
for i in range (len(boletim)):
    print(f'{i:<4}{boletim[i][0]:<10}{boletim[i][3]:>8.1f}')
print("-"*10)
while True:
    seletor = int(input('Digite o número do aluno que gostaria de ver as notas ou digite 999 para sair: '))
    while (seletor > (len(boletim)) or seletor < 0) and seletor != 999:
        print("-"*10)
        print('Aluno não encontrado')
        seletor = int(input('Digite o número do aluno que gostaria de ver as notas ou digite 999 para sair: '))
    if seletor == 999:
        break
    print("-"*10)
    print(f'Aluno: {boletim[seletor][0]} | Nota 1: {boletim[seletor][1]} | Nota 2: {boletim[seletor][2]}')
    print('-'*10)
print('Programa finalizado')
