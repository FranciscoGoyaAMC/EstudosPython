"""
Faça um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
qual é o total gasto na compra.
quantos produtos custam mais de R$1000.
qual é o nome do produto mais barato. 
"""
total_compra = 0
produto_mais_barato = 0
produtos_custam_mais_mil = 0
nome_produto_barato = " "
c = 1

while True:
    resposta = "A"
    produto = str(input('Insira o nome do produto: ')).strip().upper()
    preco = float(input('Insira o preco do produto: '))
    if preco > 0 and c == 1:
        produto_mais_barato = preco
        nome_produto_barato = produto
        c +=1
    if preco < produto_mais_barato:
        produto_mais_barato = preco
        nome_produto_barato = produto
    if preco > 1000:
        produtos_custam_mais_mil += 1
    total_compra += preco
    while resposta not in "SN":
        resposta = str(input('Deseja seguir cadastrando produtos? [S/N] ')).strip().upper()[0]
    if resposta == "N":
        break
print(f'A sua compra totalizou R$ {total_compra:.2f}')
print(f'O produto mais barato foi {nome_produto_barato} e custou R$ {produto_mais_barato:.2f}')
print(f'Você comprou {produtos_custam_mais_mil} produto(s) que custa(m) mais de mil reais')
