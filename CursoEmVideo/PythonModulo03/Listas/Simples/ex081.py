"""
Faça um programa que vai ler vários números e colocar em uma lista. E mostre:                                                                                                                                        Quantos números foram digitados.
A lista de valores, ordenada de forma decrescente.
Se o valor 5 foi digitado e está ou não na lista.
"""
numeros = []
c = 0
while True:
    resposta = "a"
    num = int(input('Digite um número: '))
    numeros.append(num)
    c += 1
    while resposta != "S" and resposta != "N":
        resposta = str(input('Deseja continuar digitando números? [S/N] ')).strip().upper()[0]
    if resposta == "N":
        break
print(f'Você digitou {c} números')
print('Os números digitados em ordem decrescente: ')
numeros.sort(reverse=True)
print(numeros)
if 5 in numeros:
    print('Você digitou o número 5 e ele está presente na lista')
else:
    print('Você não digitou o número 5 e ele não está presente na lista')
