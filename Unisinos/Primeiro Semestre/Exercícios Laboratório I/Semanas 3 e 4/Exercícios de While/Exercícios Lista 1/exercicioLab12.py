total = 0
quant = 0

while True:
    valor = int(input('Para sair digite um valor negativo, para seguir digite um valor positivo: '))
    if valor < 0:
        break
    total += valor
    quant += 1
    media = total/quant
print(f'Média dos valores digitados: {media}')
