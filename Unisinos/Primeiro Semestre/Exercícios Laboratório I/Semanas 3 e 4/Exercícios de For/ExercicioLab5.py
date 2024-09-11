compras = []
qnt = int(input('Quantos produtos terão na sua lista? '))
cont = 0

while cont < qnt:
    compras.append(input('Digite um produto: '))
    cont = cont + 1

print('Lista de compras:')
for produtos in compras:
    print(produtos)
