"""
Faça um programa que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida 
"""
from time import sleep

nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

print('Calculando...')
sleep(2)

print(f'{nome} seu IMC é de {imc:.1f}.')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 35:
    print('Você está com obesidade classe I.')
elif imc >= 35 and imc < 40:
    print('Você está com obesidade classe II.')
elif imc >= 40:
    print('Você está com obesidade classe III.')
