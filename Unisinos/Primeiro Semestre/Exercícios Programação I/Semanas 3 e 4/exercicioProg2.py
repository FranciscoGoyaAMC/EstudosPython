def divisaoValores(a,b):
    return a / b

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

if valor2 == 0:
    print('Erro, impossível fazer a divisão')
else:
    divisao = divisaoValores(valor1,valor2)
    print(divisao)
