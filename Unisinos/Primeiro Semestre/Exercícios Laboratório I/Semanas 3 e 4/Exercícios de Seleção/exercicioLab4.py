num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira um segundo número inteiro: '))
num3 = int(input('Insira um terceiro número inteiro: '))

if num1 <= num2 and num1 <= num3:
    print(f'O menor número digitado foi: {num1}')
elif num2 <= num1 and num2 <= num3:
    print(f'O menor número digitado foi: {num2}')
elif num3 <= num1 and num3 <= num2:
    print(f'O menor número digitado foi: {num3}')
