num = int(input('Digite um número para descobrir seu fatorial: '))
cont = 1
resultado = 1

while cont <= num:
    resultado *= cont
    cont += 1
print(resultado)
