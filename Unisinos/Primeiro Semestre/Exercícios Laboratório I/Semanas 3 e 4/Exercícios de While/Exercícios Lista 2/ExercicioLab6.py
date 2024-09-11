num = int(input('Digite um número positivo e par: '))
soma = 0

while num > 0 and num % 2 == 0:
    soma = soma + num
    num = int(input('Digite um número positivo e par: '))

print(f'A soma de todos números positivos e pares que você digitou é {soma}')
