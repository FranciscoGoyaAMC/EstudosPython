"""
Faça um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
"""
n = int(input('Quantos termos você gostaria de saber da Sequencia de Fibonacci: '))
val1 = 0
val2 = 1
val3 = 0
cont = 3

print(f'{val1} > {val2}', end=" ")
while cont <= n:
    val3 = val1 + val2
    print(f'> {val3}', end=" ")
    val1 = val2
    val2 = val3
    cont += 1
print('> FIM')
