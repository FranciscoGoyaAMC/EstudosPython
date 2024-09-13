"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
import sys
sys.path.append(r'c:\Users\franc\Desktop\Programação\Python\Exercícios_Guanabara\PythonModulo03\Modularização')
from ex112.utilidadesCeV import moedas
from ex112.utilidadesCeV import dado

num = dado.leia_dinheiro('Digite quanto você tem disponível: ')
var1 = int(input('Digite quantos por cento quer aumentar: '))
var2 = int(input('Digite quantos por cento quer diminuir: '))
monet = str(input('Quer converter o valor digitado para um padrão de escrita monetário: [S/N] ')).strip().upper()[0]
while monet not in 'SN':
    monet = str(input('Quer converter o valor digitado para um padrão de escrita monetário: [S/N] ')).strip().upper()[0]
if monet == 'N':
    moedas.resumo(num,var1,var2)
else:
    moedas.resumo(num,var1,var2,True)

