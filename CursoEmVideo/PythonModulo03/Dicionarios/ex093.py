"""
Faça um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
"""
dados = {}
gols = []


dados['Nome'] = str(input('Nome do(a) jogador(a): '))
dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
for i in range(0, dados['Partidas']):
    gol = int(input(f'Quantos gols na partida {i+1}: '))
    gols.append(gol)
dados['Gols'] = gols[:]
dados['Total de gols'] = sum(gols)
print(f'Atleta: {dados["Nome"]}')
for i in range(0, dados['Partidas']):
    print(f'Na partida {i+1}, {dados["Nome"]} fez {gols[i]} gol(s)')
dados['Média de gols'] = dados['Total de gols'] / dados['Partidas']
print(f'Totalizando {dados["Total de gols"]} gols em uma média de {dados["Média de gols"]:.1f} por partida')
