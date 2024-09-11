cont = 0
valor_total = 0
while cont < 20:
    valor = float(input('Digite um número com ponto flutuante: '))
    valor_total = valor_total + valor
    cont += 1
print(f'{valor_total:.2f}')
