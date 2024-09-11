"""
Faça um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
quantas pessoas tem mais de 18 anos.
quantos homens foram cadastrados.
quantas mulheres tem menos de 20 anos. 
"""
mais_dezoito = 0
homens = 0
mulheres_menos_vinte = 0

while True:
    sexo = "A"
    idade = 0
    resposta = "A"
    nome = str(input('Insira o nome da pessoa: ')).strip().upper()
    while sexo not in 'FM':
        sexo = str(input('Insira o genêro da pessoa [F] para feminino e [M] para masculino: ')).strip().upper()[0]
    while idade <= 0:
        idade = int(input('Insira a idade da pessoa: '))
    if sexo == "M":
        homens += 1
    else:
        if idade < 20:
            mulheres_menos_vinte += 1
    if idade >= 18:
        mais_dezoito += 1
    while resposta not in 'SN':
        resposta = str(input('Deseja seguir cadastrando pessoas? Digite [S] para seguir e [N] para parar: ')).strip().upper()[0]
    if resposta == "N":
        break
print(f'Você cadastro {homens} pessoa(s) do sexo masculino')
print(f'Você cadasrou {mais_dezoito} pessoa(s) maiores de idade')
print(f'Você cadastrou {mulheres_menos_vinte} mulher(es) com menos de 20 anos de idade')
