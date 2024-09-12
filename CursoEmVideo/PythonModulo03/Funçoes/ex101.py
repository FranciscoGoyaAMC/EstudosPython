"""
Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
def voto(ano):
    from datetime import date
    if date.today().year - ano < 16:
        return 'NEGADO'
    elif date.today().year - ano < 18 or date.today().year - ano >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


nascimento = int(input('Digite o ano de nascimento para saber se deve votar: '))
print(f'Voto {voto(nascimento)}')
