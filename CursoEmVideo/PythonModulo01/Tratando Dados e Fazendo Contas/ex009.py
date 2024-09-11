"""
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""
from time import sleep

print("\033[1;34m-=\033[m" * 15)
print("\033[1;30mTABUADA AUTOMÁTICA\033[m")
print("\033[1;34m-=\033[m" * 15)

sleep(2)
n = int(input('Digite um valor: '))

print('Calculando...')
sleep(2)

print(f'Tabuada de {n} \n {n} x 1 = {n} \n {n} x 2 = {n*2} \n {n} x 3 = {n*3} \n {n} x 4 = {n*4} \n {n} x 5 = {n*5} \n {n} x 6 = {n*6} \n {n} x 7 = {n*7} \n {n} x 8 = {n*8} \n {n} x 9 = {n*9} \n {n} x 10 = {n*10}')
