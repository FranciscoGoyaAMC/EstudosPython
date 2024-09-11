"""
Faça um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros
"""
from time import sleep

pagamento = 0
preco = float(input('Digite o preço do produto: '))
print('Digite [1] para pagamento à vista (dinheiro/cheque)')
print('Digite [2] para pagamento à vista no cartão')
print('Digite [3] para pagar em até 2x no cartão')
print('Digite [4] para pagar em 3 ou mais vezes no cartão')
pagamento = int(input('Digite a forma de pagamento: '))

while pagamento < 1 or pagamento > 4:
    print('OPÇÃO INVÁLIDA')
    print('Digite [1] para pagamento à vista (dinheiro/cheque)')
    print('Digite [2] para pagamento à vista no cartão')
    print('Digite [3] para pagar em até 2x no cartão')
    print('Digite [4] para pagar em 3 ou mais vezes no cartão')
    pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    preco = preco - (preco * 0.1)
    print(f'O valor fica R$ {preco:.2f}')
elif pagamento == 2:
    preco = preco - (preco * 0.05)
    print(f'O valor fica R$ {preco:.2f}')
elif pagamento == 3:
    print(f'O valor fica R$ {preco:.2f}')
else:
    parcelas = int(input('Em quantas parcelas será feito: '))
    preco = preco + (preco * 0.2)
    parcelado = preco / parcelas
    print(f'O valor total fica R$ {preco:.2f} em {parcelas} parcelas de R$ {parcelado:.2f}')
