"""
Faça um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
Quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares.
"""
n0 = int(input('Digite um valor: '))
n1 = int(input('Digite outro valor: '))
n2 = int(input('Digite mais um valor: '))
n3 = int(input('Digite um último valor: '))
numeros = (n0, n1, n2, n3)
for i in range(0,4):
    if numeros[i] == 3:
        print(f'Você digitou o número 3 na posição {i}')
    if numeros[i] % 2 == 0:
        print(f'Você digitou {numeros[i]}, que é um número par')
print(f'Você digitou o número 9 {numeros.count(9)} vez(es)')
