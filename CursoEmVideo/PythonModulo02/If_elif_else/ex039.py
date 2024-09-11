"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
from time import sleep

nascimento = int(input('Digite o ano que você nasceu: '))
atual = date.today().year
anos = atual - nascimento
tempo_alistamento = anos - 18
ano_alistamento = atual - tempo_alistamento

print('Analisando...')
sleep(2)

if (anos == 18):
    print(f'Quem nasceu em {nascimento} tem {anos} anos no ano de {atual}')
    print('\033[31mHora de se alistar\033[m')
elif (anos > 18):
    print(f'Quem nasceu em {nascimento} tem {anos} anos no ano de {atual} e deveria ter se alistado a {abs(tempo_alistamento)} ano(s), no ano de {ano_alistamento}')
    print('\033[33mJá passou do seu período de alistamento\033[m')
elif (anos < 18):
    print(f'Quem nasceu em {nascimento} tem {anos} anos no ano de {atual} e irá se alistar em {abs(tempo_alistamento)} ano(s), no ano de {ano_alistamento}')
    print('\033[32mAproveite! Ainda tem um tempo antes de se alistar\033[m')
