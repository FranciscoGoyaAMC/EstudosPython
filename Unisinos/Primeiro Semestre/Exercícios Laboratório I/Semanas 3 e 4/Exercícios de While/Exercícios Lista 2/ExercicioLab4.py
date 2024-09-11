num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 < num2:
    print(f'Números de {num1} a {num2}')
    while num1 < num2:
        print(num1)
        num1 += 1
        
    print(num2)
else:
    print(f'Números de {num2} a {num1}')
    while num1 >= num2:
        print(num1)
        num1 = num1 - 1
