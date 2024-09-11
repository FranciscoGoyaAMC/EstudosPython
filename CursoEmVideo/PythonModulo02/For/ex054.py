"""
Faça um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

maiores = 0
menores = 0

for i in range(0,7):
    ano = int(input('Digite o ano em que você nasceu: '))
    if (date.today().year - ano < 18):
        menores += 1
    else:
        maiores += 1
print(f'Nesse grupo temos {maiores} maiores de idade e {menores} menores de idade.')
