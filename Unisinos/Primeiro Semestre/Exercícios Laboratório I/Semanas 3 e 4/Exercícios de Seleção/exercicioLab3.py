num1 = int(input('Insira um número de 0 a 10: '))
num2 = int(input('Insira um número de 0 a 10: '))

if num2 == 0:
    print('Erro... não foi possível dividir por 0.')
div = num1 / num2

print(f'O resultado da divisão do primeiro número ({num1}) pelo segundo número ({num2}) é: {div}')
