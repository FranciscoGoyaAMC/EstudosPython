"""
Faça um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre as informações dos cadastrados
"""
dados = {}
pessoas = []
total_mulheres = 0
total_homens = 0
maiores_de_idade = 0
menores_de_idade = 0
total_idade = 0
acima_media = 0
abaixo_media = 0
dentro_media = 0

while True:
    dados.clear()
    resposta = 'a'
    dados['Nome'] = str(input('Nome: ')).strip().upper()
    dados['Idade'] = int(input('Idade: '))
    while dados['Idade'] <= 0:
        print('Idade inválida')
        dados['Idade'] = int(input('Idade: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas.append(dados.copy())
    while resposta not in 'SN':
        resposta = str(input('Deseja seguir cadastrando pessoas? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
for i in range (len(pessoas)):
    total_idade += pessoas[i]['Idade']
    if pessoas[i]['Sexo'] == 'F':
        total_mulheres += 1
    elif pessoas[i]['Sexo'] == 'M':
        total_homens += 1
    if pessoas[i]['Idade'] >= 18:
        maiores_de_idade += 1
    elif pessoas[i]['Idade'] < 18:
        menores_de_idade += 1
media_idade = total_idade / len(pessoas)
for i in range (len(pessoas)):
    if pessoas[i]['Idade'] > media_idade:
        acima_media +=1
    elif pessoas[i]['Idade'] < media_idade:
        abaixo_media += 1
    elif pessoas[i]['Idade'] == media_idade:
        dentro_media += 1
print('--------\nDADOS DE CADASTRO\n--------')
print(f'Você cadastrou um total de {len(pessoas)} pessoa(s)')
print(f'Sendo um total de {total_mulheres} mulher(es) e {total_homens} homem(ns)')
print(f'A média de idade é {media_idade:.1f} anos')
print(f'Sendo {maiores_de_idade} maior(es) de idade e {menores_de_idade} menor(es) de idade')
print(f'Das {len(pessoas)} pessoa(s) cadastras {acima_media} está(ão) acima da média de idade')
print(f'{dentro_media} está(ão) dentro da média de idade')
print(f'{abaixo_media} está(ão) abaixo da média de idade')
print('--------\nPESSOAS CADASTRADAS\n--------')
for i in range (len(pessoas)):
    print(f'Nome: {pessoas[i]["Nome"]}\nIdade: {pessoas[i]["Idade"]}\nSexo: {pessoas[i]["Sexo"]}\n--------\n')
print('MULHERES CADASTRADAS\n--------')
for i in range(len(pessoas)):
    if pessoas[i]['Sexo'] == 'F':
        print(f'Nome: {pessoas[i]["Nome"]} | Idade: {pessoas[i]["Idade"]}')
print('--------\nHOMENS CADASTRADOS\n--------')
for i in range(len(pessoas)):
    if pessoas[i]['Sexo'] == 'M':
        print(f'Nome: {pessoas[i]["Nome"]} | Idade: {pessoas[i]["Idade"]}')
print('--------\nMAIORES DE IDADE CADASTRADOS\n--------')
for i in range(len(pessoas)):
    if pessoas[i]['Idade'] >= 18:
        print(f'Nome: {pessoas[i]["Nome"]} | Idade: {pessoas[i]["Idade"]} | Sexo: {pessoas[i]["Sexo"]}')
print('--------\nMENORES DE IDADE CADASTRADOS\n--------')
for i in range(len(pessoas)):
    if pessoas[i]['Idade'] < 18:
        print(f'Nome: {pessoas[i]["Nome"]} | Idade: {pessoas[i]["Idade"]} | Sexo: {pessoas[i]["Sexo"]}')
print('--------\nACIMA DA MEDIA DE IDADE CADASTRADOS\n--------')
for i in range(len(pessoas)):
    if pessoas[i]['Idade'] > media_idade:
        print(f'Nome: {pessoas[i]["Nome"]} | Idade: {pessoas[i]["Idade"]} | Sexo: {pessoas[i]["Sexo"]}')
print('--------\nABAIXO DA MEDIA DE IDADE CADASTRADOS\n--------')
for i in range(len(pessoas)):
    if pessoas[i]['Idade'] < media_idade:
        print(f'Nome: {pessoas[i]["Nome"]} | Idade: {pessoas[i]["Idade"]} | Sexo: {pessoas[i]["Sexo"]}')
print('--------\nDENTRO DA MEDIA DE IDADE CADASTRADOS\n--------')
for i in range(len(pessoas)):
    if pessoas[i]['Idade'] == media_idade:
        print(f'Nome: {pessoas[i]["Nome"]} | Idade: {pessoas[i]["Idade"]} | Sexo: {pessoas[i]["Sexo"]}')
