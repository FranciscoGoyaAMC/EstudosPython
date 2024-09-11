"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. 
"""
n = int(input('Digite o número que você gostaria de saber o fatorial: '))
contador = n
fatorial = 1
print(f'Fatorial de {n}:')

while contador > 0:
    print(f'{contador}', end="")
    print(' x ' if contador > 1 else ' = ', end="")
    fatorial *= contador
    contador -= 1
print(fatorial)
