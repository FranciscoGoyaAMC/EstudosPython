"""
Faça um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
"""
from num2words import num2words

n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('O número deve ser entre 0 e 20. Digite um número: '))
n_pt = num2words(n, lang='pt-br')
print(f'Você digitou o número {n_pt}')
