"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
for v in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior_valor = valores[0]
menor_valor = valores[0]
for v in range(len(valores)):
    if valores[v] > maior_valor:
        maior_valor = valores[v]
    if valores[v] < menor_valor:
        menor_valor = valores[v]
print(f'O maior valor digitado foi {maior_valor} na(s) posição(ões) ', end="") 
for c, v in enumerate(valores):
    if v == maior_valor:
        print(f'{c} ', end="")
print()
print(f'O menor valor digitado foi {menor_valor} na(s) posição(ões) ', end="")
for c, v in enumerate(valores):
    if v == menor_valor:
        print(f'{c} ', end="")
