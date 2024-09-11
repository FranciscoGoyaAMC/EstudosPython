preco = float(input('Digite o preço do produto: '))
if preco <= 0:
    print('Erro! Valor inválido.')
elif preco < 100:
   juros = preco * 0.1
   preco_total = preco + juros
   print(f'Aplicado o juros seu valor final ficou: {preco_total:.2f}')
elif preco >= 100 and preco < 300:
    juros = preco * 0.2
    preco_total = preco + juros
    print(f'Aplicado o juros seu valor final ficou: {preco_total:.2f}')
elif preco >= 300 and preco <= 1000:
    juros = preco * 0.5
    preco_total = preco + juros
    print(f'Aplicado o juros seu valor final ficou: {preco_total:.2f}')
