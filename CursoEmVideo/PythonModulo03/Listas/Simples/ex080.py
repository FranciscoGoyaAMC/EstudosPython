"""
Faça um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
numeros = []
for i in range(0,5):
    num = int(input('Digite um número: '))
    if i == 0:
        numeros.append(num)
        print(f'Número {num} inicializando a lista')
    elif num > numeros[-1]:
        numeros.append(num)
        print(f'Número {num} adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Número {num} adicionado na posição {pos} da lista')
                break
            pos += 1
print('Os valores digitados foram:')
print(numeros)
