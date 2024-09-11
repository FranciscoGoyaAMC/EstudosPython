"""
Faça um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
valores = []
while True:
    resposta = "A"
    num = int(input('Digite um número: '))
    valores.append(num)
    while valores.count(num) > 1:
        valores.remove(num)
        print('Valor repetido')
        num = int(input('Digite um número: '))
        valores.append(num)
    while resposta != "S" and resposta != "N":
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == "N":
        break
valores.sort()
print(f'{valores}')
