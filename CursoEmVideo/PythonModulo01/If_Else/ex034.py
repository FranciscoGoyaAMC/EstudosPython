"""
Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
from time import sleep

salario = float(input('Digite o seu salário: '))

print('Calculando reajuste...')
sleep(2)

if salario <= 1250.00:
    reajuste = salario + (salario * 0.15)
    print(f'Seu novo salário é R$ {reajuste:.2f}')
else:
    reajuste = salario + (salario * 0.10)
    print(f'Seu novo salário é R$ {reajuste:.2f}')
