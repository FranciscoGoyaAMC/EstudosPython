num = int(input('Digite um número para saber se ele é primo: '))
mult = 0

for cont in range(2,num):
    if(num % cont == 0):
        print(f'Múltiplo de {cont}')
        mult += 1
if(mult==0):
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')
