"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol de 2017, na ordem de colocação. Depois mostre:
Os 5 primeiros times.
Os últimos 4 colocados.
Times em ordem alfabética.
Em que posição está o time da Chapecoense.
"""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama',
         'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 10)
print(f'Colocação final dos times no Brasileirão 2017: {times}')
print('-=' * 10)
print(f'Os primeiros colocados do Brasileirão 2017 foram: {times[0:5]}')
print('-=' * 10)
print(f'Os últimos colocados do Brasileirão 2017 foram: {times[16:]}')
print('-=' * 10)
print(f'Times do Brasileirão 2017 em ordem alfabética: {sorted(times)}')
print('-=' * 10)
