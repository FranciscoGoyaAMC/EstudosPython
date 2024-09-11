def area(largura, comprimento):
    area = largura * comprimento
    return area


largura = float(input('Digite a largura do terreno em metros: '))
comprimento = float(input('Digite o comprimento do terreno metros: '))
print(f'A área do terreno é {area(largura, comprimento):.2f} m²')
