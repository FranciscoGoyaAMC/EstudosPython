"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
from ex109 import moedas

num = float(input('Digite quanto você tem disponível: '))
var1 = int(input('Digite quantos por cento quer aumentar: '))
var2 = int(input('Digite quantos por cento quer diminuir: '))
monet = str(input('Quer converter o valor digitado para um padrão de escrita monetário: [S/N] ')).strip().upper()[0]
while monet not in 'SN':
    monet = str(input('Quer converter o valor digitado para um padrão de escrita monetário: [S/N] ')).strip().upper()[0]
if monet == 'N':
    print(f'Aumentando o valor {num} em {var1}% fica {moedas.aumentar(num,var1)}')
    print(f'Diminuindo o valor {num} em {var2}% fica {moedas.diminuir(num,var2)}')
    print(f'Dobrando o valor {num} fica {moedas.dobro(num)}')
    print(f'A metade do valor {num} fica {moedas.metade(num)}')
else:
    print(f'Aumentando o valor {moedas.moeda(num)} em {var1}% fica {moedas.aumentar(num,var1,True)}')
    print(f'Diminuindo o valor {moedas.moeda(num)} em {var2}% fica {moedas.diminuir(num,var2,True)}')
    print(f'Dobrando o valor {moedas.moeda(num)} fica {moedas.dobro(num,True)}')
    print(f'A metade do valor {moedas.moeda(num)} fica {moedas.metade(num,True)}')
print(help(moedas))
