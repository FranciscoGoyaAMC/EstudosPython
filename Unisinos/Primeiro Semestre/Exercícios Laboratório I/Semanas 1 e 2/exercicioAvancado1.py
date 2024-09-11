from time import sleep

A = float(input('Digite o primeiro valor de A: '))
B = int(input('Digite o segundo valor de B(sem casas decimais): '))

print('Calculando...')
sleep(2)

multiplicacao = A * B
divisao = A / B
soma = A + B
subtracao = A - B
potencia = A ** B

print(f'A multiplicado por B é: {multiplicacao}')
print(f'A dividido por B é: {divisao}')
print(f'A soma de A mais B é: {soma} e A menos B é: {subtracao}')
print(f'A elevado a B é: {potencia}')
