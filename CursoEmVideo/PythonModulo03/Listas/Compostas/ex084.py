"""
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. Depois diga:
Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas.
Uma listagem com as pessoas mais leves.
"""
dados = []
pessoas = []
maior_peso = menor_peso = 0
while True:
    resposta = "a"
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = dados[1]
        menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar cadastrando pessoas? [S/N] ')).strip().upper()[0]
    if resposta == "N":
        break
print(f'Você cadastrou {len(pessoas)} pessoa(s)')
print(f"O maior peso foi {maior_peso} kg's da(s) pessoa(s)", end='')
for i in pessoas:
    if i[1] == maior_peso:
        print(f'[{i[0]}]', end='')
print()
print(f"O menor peso foi {menor_peso} kg's da(s) pessoa(s) ", end='')
for i in pessoas:
    if i[1] == menor_peso:
        print(f'[{i[0]}]', end='')
