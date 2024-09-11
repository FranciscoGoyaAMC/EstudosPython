"""
Faça um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""
from time import sleep

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m'}

nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2) / 2

print('Calculando...')
sleep(2)

if media < 5.0:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} sua média é {media:.2f}')
    print(f'Você foi {cores["vermelho"]}REPROVADO{cores["limpa"]}')
elif media >= 5.0 and media < 7.0:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} sua média é {media:.2f}')
    print(f'Você pegou {cores["amarelo"]}RECUPERAÇÃO{cores["limpa"]}')
else:
    print(f'Com as notas {nota1:.2f} e {nota2:.2f} sua média é {media:.2f}')
    print(f'Você foi {cores["verde"]}APROVADO{cores["limpa"]}')
