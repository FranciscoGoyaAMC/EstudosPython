"""
Faça um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
resposta = "S"
c = 1
total = 0
maior = 0
menor = 0
media = 0

n = int(input('Digite um número: '))
maior = n
menor = n
resposta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

while resposta != "N":
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    total += n
    c += 1
    resposta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
media = total / c
print(f'Ao total você digitou {c} números, o maior número foi {maior}, o menor foi {menor} e a média de todos números digitados é {media}')
