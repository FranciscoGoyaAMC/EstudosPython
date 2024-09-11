cont = 0
quant = int(input('Quantos valores serão digitados: '))
while cont < quant:
    valor = int(input('Digite um valor: '))
    if valor < 0:
        print('Valor negativo')
    elif valor == 0:
        print('Zero')
    elif valor > 0:
        print('Valor positivo')
    cont += 1
