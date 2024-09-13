"""
Adicione uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
from ex110 import moedas

num = float(input('Digite quanto você tem disponível: '))
var1 = int(input('Digite quantos por cento quer aumentar: '))
var2 = int(input('Digite quantos por cento quer diminuir: '))
monet = str(input('Quer converter o valor digitado para um padrão de escrita monetário: [S/N] ')).strip().upper()[0]
while monet not in 'SN':
    monet = str(input('Quer converter o valor digitado para um padrão de escrita monetário: [S/N] ')).strip().upper()[0]
if monet == 'N':
    moedas.resumo(num,var1,var2)
else:
    moedas.resumo(num,var1,var2,True)
help(moedas)
