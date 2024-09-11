"""
Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
dados = {}
gols = []
jogadores = []

while True:
    resposta = 'a'
    dados.clear()
    dados['Nome'] = str(input('Nome do(a) jogador(a): ')).strip().upper()
    dados['Número do jogador'] = int(input('Número da camisa do(a) jogador(a): '))
    while dados['Número do jogador'] < 0:
        print('Número inválido')
        dados['Número do jogador'] = int(input('Número da camisa do(a) jogador(a): '))
    for i in range (len(jogadores)):
        while (jogadores[i]['Número do jogador'] == dados['Número do jogador']):
            print('Número inválido')
            dados['Número do jogador'] = int(input('Número da camisa do(a) jogador(a): '))
    dados['Partidas'] = int(input('Quantas partidas o jogador jogou? '))
    if dados['Partidas'] == 0:
        gol = 0
        gols.append(gol)
        dados['Média de gols'] = 0
    for i in range(0, dados['Partidas']):
        gol = int(input(f'Quantos gols {dados["Nome"]} fez na partida {i+1}: '))
        gols.append(gol)
    dados['Gols'] = gols[:]
    dados['Total de gols'] = sum(gols)
    gols.clear()
    if dados['Partidas'] != 0:
        dados['Média de gols'] = dados['Total de gols'] / dados['Partidas']
    jogadores.append(dados.copy())
    while resposta not in 'SN':
        resposta = str(input('Quer continuar cadastrando jogadores(as)? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-------\nDADOS JOGADORES\n-------')
print(f'{'COD':<4}{'NÚMERO':<8}{'NOME':<12}{'PARTIDAS':<16}{'GOLS':<20}{'MÉDIA':>4}')
for i in range(0, len(jogadores)):
    print(f'{i:<4}{jogadores[i]["Número do jogador"]:<8}{jogadores[i]["Nome"]:<12}{jogadores[i]["Partidas"]:<16}',
          f'{jogadores[i]["Total de gols"]:<20}{jogadores[i]["Média de gols"]:>4.1f}')
while True:
    print('-------')
    print('Digite o código do jogador que gostaria de ver as estátisticas')
    print('Digite 999 para sair do programa')
    seletor = int(input('Código: '))
    while (seletor > len(jogadores) or seletor < 0) and seletor != 999:
        print('-------')
        print('Código inválido')
        print('Digite o código do jogador que gostaria de ver as estátisticas')
        print('Digite 999 para sair do programa')
        seletor = int(input('Código: '))
    if seletor == 999:
        break
    print(f'-------\nDADOS {jogadores[seletor]["Nome"]}\n-------')
    print(f'Nome: {jogadores[seletor]["Nome"]} | Número: {jogadores[seletor]["Número do jogador"]} | Partidas: {jogadores[seletor]["Partidas"]}')
    for i in range(0,jogadores[seletor]['Partidas']):
        print(f'Partida {i+1} fez {jogadores[seletor]["Gols"][i]} gol(s)')
    print(f'Total de Gols: {jogadores[seletor]["Total de gols"]} | Média de Gols: {jogadores[seletor]["Média de gols"]}')
print('-------\nPROGRAMA FINALIZADO\n-------')
