"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
maior_peso = 0
menor_peso = 0

for i in range(1,6):
    peso = float(input(f'Digite o {i}º peso: '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi {maior_peso} e o menor foi {menor_peso}.')
