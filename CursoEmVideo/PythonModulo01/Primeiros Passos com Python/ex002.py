"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas. De preferência use cores
"""
cores = {'limpa':'\033[m',
         'cianosub':'\033[4;36m'}

nome = input('Digite seu nome: ')

print(f'Olá, {cores["cianosub"]}{nome}{cores["limpa"]}! Seja bem-vindo(a).')
