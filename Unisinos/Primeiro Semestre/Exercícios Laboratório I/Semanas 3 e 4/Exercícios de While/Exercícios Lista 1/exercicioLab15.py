print('Números primos de 2 a 200')
num = 2
soma_primos = 0
isPrimo = True

while (num <= 200):
    if num == 2:
        print(f'{num} é primo')
        soma_primos += num
    else:
        for i in range(2,num):
            if num % i == 0:
                print(f'{num} não é primo')
                isPrimo = False
                break
            
            else:
                soma_primos += num
                isPrimo = True
        if isPrimo: 
            print(f'{num} é primo')            
    num += 1
print(f' Soma dos números primos de 2 a 200 é: {soma_primos}')
