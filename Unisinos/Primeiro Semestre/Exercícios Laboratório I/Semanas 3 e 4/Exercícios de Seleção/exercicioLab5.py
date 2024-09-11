preco = float(input('Digite o valor de seu produto: '))
if preco <= 0:
    print('Preço inválido')
elif preco <= 30:
    print('Preço baixo')
elif preco <= 50:
    print('Preço médio')
else:
    print('Preço alto')
