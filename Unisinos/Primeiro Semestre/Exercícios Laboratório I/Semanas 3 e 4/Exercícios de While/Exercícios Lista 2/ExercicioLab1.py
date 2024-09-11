cont = 0

while cont < 10:
    num = int(input('Digite um número: '))
    if num < 0:
        print('Número negativo.')
    elif num == 0:
        print('Zero.')
    else:
        print('Número positivo.')
    cont += 1
