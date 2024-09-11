"""
Faça um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from time import sleep

valor_casa = float(input('Qual o valor do imóvel desejado? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
prestacao = valor_casa / (anos * 12)

print('Calculando...')
sleep(2)

if prestacao <= salario * 0.3:
    print('EMPRÉSTIMO \033[1;32mAPROVADO\033[m!')
else:
    print('EMPRÉSTIMO \033[1;31mNEGADO\033[m!')
