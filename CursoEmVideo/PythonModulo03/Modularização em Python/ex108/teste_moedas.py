"""
 Adapte o código do exercício #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado
"""
from ex108 import moedas

num = float(input('Digite quanto você tem disponível: '))
var1 = int(input('Digite quantos por cento quer aumentar: '))
var2 = int(input('Digite quantos por cento quer diminuir: '))
print(f'Aumentando o valor {moedas.moeda(num)} em {var1}% fica {moedas.moeda(moedas.aumentar(num,var1))}')
print(f'Diminuindo o valor {moedas.moeda(num)} em {var2}% fica {moedas.moeda(moedas.diminuir(num,var2))}')
print(f'Dobrando o valor {moedas.moeda(num)} fica {moedas.moeda(moedas.dobro(num))}')
print(f'A metade do valor {moedas.moeda(num)} fica {moedas.moeda(moedas.metade(num))}')
print(help(moedas))
