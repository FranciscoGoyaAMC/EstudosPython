"""
Faça um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
total_idade = 0
homem_mais_velho = ""
idade_homem_velho = 0
menos_vinte = 0

for i in range(1,5):
    nome = str(input(f'Digite o nome da {i}ª pessoa: ')).strip().upper()
    sexo = input(f'Digite M se o sexo da {i}ª pessoa for Masculino e F se for feminino: ').strip().upper()[0]
    while (sexo != "M") and (sexo != "F"):
        print('Opção inválida')
        sexo = input(f'Digite M se o sexo da {i}ª pessoa for Masculino e F se for feminino: ').strip().upper()[0]
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    total_idade += idade
    media_idade = total_idade / 4
    if sexo == "M":
        if idade > idade_homem_velho:
            idade_homem_velho = idade
            homem_mais_velho = nome
    if sexo == "F":
        if idade < 20:
            menos_vinte += 1
print(f'A média de idade do grupo é {media_idade:.0f}')
print(f'{homem_mais_velho} é o homem mais velho e sua idade é {idade_homem_velho}')
print(f'{menos_vinte} mulher(es) tem menos de 20 anos.')
