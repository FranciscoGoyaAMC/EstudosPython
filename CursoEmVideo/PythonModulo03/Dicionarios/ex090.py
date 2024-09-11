"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
boletim = {}

boletim['aluno'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["aluno"]}: '))
while (boletim['media'] < 0 or boletim['media'] > 10):
    print('Valor inválido')
    boletim['media'] = float(input('Média do aluno: '))

if (boletim['media'] >= 7.0):
    boletim['grau'] = 'APROVADO(A)'
elif (boletim['media'] >= 5.0 and boletim['media'] < 7.0):
    boletim['grau'] = 'EM RECUPERAÇÃO'
else:
    boletim['grau'] = 'REPROVADO(A)'
print(f'O(A) aluno(a) {boletim["aluno"]} fico com média {boletim["media"]} logo ele(a) está {boletim["grau"]}')
