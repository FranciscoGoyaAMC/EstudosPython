"""
Faça um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
numeros = []
pares = []
impares = []
while True:
    resposta = "a"
    numeros.append(int(input('Digite um número: ')))
    while resposta not in "SN":
        resposta = str(input('Deseja inserir mais números? [S/N] ')).strip().upper()[0]
    if resposta == "N":
        break
for i in range (len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
print(f'Você digitou os númers {numeros}')
print(f'Os valores pares são {pares}')
print(f'Os valores ímpares são {impares}')
