"""
 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER
"""
from time import sleep
from datetime import date

nome = str(input('Digite o nome do atleta: '))
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano

print('Analisando...')
sleep(2)

if idade <= 9:
    print(f'{nome} tem {idade} anos, logo está na categoria mirim')
elif idade > 9 and idade <= 14:
    print(f'{nome} tem {idade} anos, logo está na categoria infantil.')
elif idade > 14 and idade <= 19:
    print(f'{nome} tem {idade} anos, logo está na categoria júnior.')
elif idade > 19 and idade <= 25:
    print(f'{nome} tem {idade} anos, logo está na categoria sênior.')
else:
    print(f'{nome} tem {idade} anos, logo está na categoria master.')
