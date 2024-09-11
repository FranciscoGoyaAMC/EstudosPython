"""
Faça um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from datetime import date

dados = {}
dados['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - ano_nascimento
dados['Carteira de trabalho'] = int(input('Carteira de trabalho: [0] caso não tenha '))
if dados['Carteira de trabalho'] == 0:
    dados['Carteira de trabalho'] = 'Não possui'
    for n, d in dados.items():
        print(f'{n}: {d}')
else:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Ano de aposentadoria'] = dados['Ano de contratação'] + 45
    dados['Idade de aposentadoria'] = dados['Ano de aposentadoria'] - ano_nascimento
    for n,d in dados.items():
        print(f'{n}: {d}')
