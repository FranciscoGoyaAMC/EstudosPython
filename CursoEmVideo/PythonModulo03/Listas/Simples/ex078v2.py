"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
for v in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior_valor = valores[0]
posicao_maior_valor = 0
menor_valor = valores[0]
posicao_menor_valor = 0
for v in range(len(valores)):
    if valores[v] > maior_valor:
        maior_valor = valores[v]
        posicao_maior_valor = valores.index(maior_valor) + 1
    if valores[v] < menor_valor:
        menor_valor = valores[v]
        posicao_menor_valor = valores.index(menor_valor) + 1
print(f'O maior valor digitado foi {maior_valor} e ele está na posição {posicao_maior_valor}')
print(f'O menor valor digitado foi {menor_valor} e ele está na posição {posicao_menor_valor}')
